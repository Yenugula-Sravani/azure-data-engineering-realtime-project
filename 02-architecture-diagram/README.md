# Azure Data Engineering Architecture – Medallion Design

## Architecture Overview
This project follows a **production-style Azure Data Engineering architecture**
using a **Medallion pattern (Bronze, Silver, Gold)** to ensure scalability,
data quality, and analytics readiness.

The architecture separates ingestion, transformation, and consumption
to avoid tight coupling and improve maintainability.

---

## Azure Services Used

- **Azure Data Factory (ADF)**  
  Used for orchestration and ingestion of source data into the data lake.

- **Azure Data Lake Storage Gen2 (ADLS Gen2)**  
  Centralized storage layer implementing Bronze, Silver, and Gold zones.

- **Azure Databricks**  
  Used for data cleansing, transformation, and enrichment using PySpark.

- **Delta Lake**  
  Provides ACID transactions, versioning, and optimized storage.

- **Azure Key Vault (Design Reference)**  
  Used to securely manage secrets such as connection strings (represented
  as placeholders in this project).

---

## Data Flow Architecture

### 1️⃣ Source Layer
- Simulated on-premise MySQL / relational database
- Contains transactional data (orders, customers, products)

---

### 2️⃣ Bronze Layer (Raw Data)
- Raw data ingested by ADF into ADLS Gen2
- No transformations applied
- Maintains source-level granularity
- Stored in Delta format

**Purpose:**  
Auditability, reprocessing, and historical traceability

---

### 3️⃣ Silver Layer (Cleansed Data)
- Data processed using Databricks (PySpark)
- Cleansing applied:
  - Null handling
  - Deduplication
  - Data type normalization
- Stored as optimized Delta tables

**Purpose:**  
Clean, standardized datasets for downstream use

---

### 4️⃣ Gold Layer (Business-Ready Data)
- Aggregated and business-focused datasets
- Optimized for analytics and reporting
- Example outputs:
  - Daily sales summary
  - Customer-level metrics

**Purpose:**  
Consumption by BI tools and analytics teams

---

## Orchestration Strategy
- Azure Data Factory triggers ingestion pipelines
- Databricks notebooks are executed as transformation steps
- Pipelines are parameterized to support reusability
- Incremental load patterns are followed where applicable

---

## Design Principles Followed
- Separation of concerns
- Idempotent pipeline design
- Scalable storage and compute
- Production-oriented folder structure
- Interview-ready architecture decisions

---

## Outcome
- Clean and maintainable Azure Data Engineering architecture
- Clear separation between raw, processed, and business data
- Real-world design suitable for interviews and reusable templates

