# ============================================
# Bronze to Silver Transformation
# Author: Sravani Data Studio
# ============================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, current_timestamp
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

spark = SparkSession.builder.appName("BronzeToSilver").getOrCreate()

# ----------------------------
# Configuration
# ----------------------------
BRONZE_PATH = "/mnt/bronze/orders/"
SILVER_PATH = "/mnt/silver/orders/"

# ----------------------------
# Read Bronze Data
# ----------------------------
bronze_df = spark.read.format("delta").load(BRONZE_PATH)

# ----------------------------
# Data Cleansing
# ----------------------------

# Remove duplicate records using business key
window_spec = Window.partitionBy("order_id").orderBy(col("updated_at").desc())

dedup_df = (
    bronze_df
    .withColumn("row_num", row_number().over(window_spec))
    .filter(col("row_num") == 1)
    .drop("row_num")
)

# Handle null values
clean_df = (
    dedup_df
    .fillna({
        "order_status": "UNKNOWN",
        "payment_mode": "UNKNOWN"
    })
)

# Standardize timestamp columns
final_silver_df = (
    clean_df
    .withColumn("order_date", to_timestamp(col("order_date")))
    .withColumn("processed_at", current_timestamp())
)

# ----------------------------
# Write to Silver Layer
# ----------------------------
(
    final_silver_df
    .write
    .format("delta")
    .mode("overwrite")
    .save(SILVER_PATH)
)

