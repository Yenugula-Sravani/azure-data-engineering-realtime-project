# Interview Guide – Real-Time Azure Data Engineering Project

This document helps candidates explain the project confidently during
Azure Data Engineer interviews by mapping real-world questions to
practical design decisions implemented in this project.

---

## 1️⃣ Project Overview (How to Explain)

**Interview Answer:**

“This project implements a production-style Azure Data Engineering pipeline
to ingest data from an on-premise relational database into Azure using
Azure Data Factory, Databricks, and ADLS Gen2 following the Medallion
Architecture (Bronze, Silver, Gold).

The goal was to build a scalable, reusable, and analytics-ready data platform
with proper validation and error handling.”

---

## 2️⃣ Why Medallion Architecture?

**Interview Answer:**

“Medallion Architecture helps separate raw ingestion, cleansing, and
business transformations.  
Bronze ensures traceability, Silver ensures clean data, and Gold provides
analytics-ready datasets.

This separation improves maintainability, reprocessing capability,
and data quality.”

---

## 3️⃣ How Did You Ingest Data?

**Interview Answer:**

“I used Azure Data Factory with a parameterized pipeline that dynamically
ingests multiple source tables into the Bronze layer.  
Lookup and ForEach activities enable scalable ingestion, and incremental
loading is handled using a watermark column.”

---

## 4️⃣ How Did You Handle Incremental Loads?

**Interview Answer:**

“I used a timestamp-based watermark column such as `updated_a_
