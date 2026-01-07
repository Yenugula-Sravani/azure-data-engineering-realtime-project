# ============================================
# Silver to Gold Transformation
# Author: Sravani Data Studio
# ============================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, to_date

spark = SparkSession.builder.appName("SilverToGold").getOrCreate()

# ----------------------------
# Configuration
# ----------------------------
SILVER_PATH = "/mnt/silver/orders/"
GOLD_PATH = "/mnt/gold/daily_sales_summary/"

# ----------------------------
# Read Silver Data
# ----------------------------
silver_df = spark.read.format("delta").load(SILVER_PATH)

# ----------------------------
# Business Aggregations
# ----------------------------
gold_df = (
    silver_df
    .withColumn("order_day", to_date(col("order_date")))
    .groupBy("order_day")
    .agg(
        count("order_id").alias("total_orders"),
        sum("order_amount").alias("total_sales_amount")
    )
)

# ----------------------------
# Write to Gold Layer
# ----------------------------
(
    gold_df
    .write
    .format("delta")
    .mode("overwrite")
    .save(GOLD_PATH)
)
