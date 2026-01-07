# Azure Data Factory Pipelines – Bronze Layer Ingestion

## Purpose
The Bronze layer ingestion pipeline is responsible for extracting raw data
from the source system and landing it into Azure Data Lake Storage Gen2
without applying any transformations.

This ensures auditability, reprocessing capability, and source-level traceability.

---

## Source System
- Simulated on-premise relational database (MySQL / SQL Server)
- Tables contain transactional data such as:
  - customers
  - products
  - orders
  - order_items

---

## Target Storage
- Azure Data Lake Storage Gen2
- Container: `bronze`
- Folder structure:
/bronze/<table_name>/ingestion_date=YYYY-MM-DD/

## Pipeline Design Overview

### Pipeline Name
pl_ingest_bronze_tables

### Pipeline Parameters
| Parameter Name | Description |
|--------------|-------------|
| source_table | Name of the source table |
| ingestion_date | Date of ingestion |
| target_path | ADLS bronze folder path |

---

### Activities Used

1️⃣ **Lookup Activity**
- Fetch list of source tables to ingest
- Enables dynamic ingestion

2️⃣ **ForEach Activity**
- Iterates over each source table

3️⃣ **Copy Data Activity**
- Copies data from source to ADLS Gen2
- Uses parameterized dataset
- Writes data in Delta / Parquet format
---
## Incremental Load Strategy
- Uses watermark column (e.g., `updated_at`)
- Only new or changed records are ingested
- Supports reruns without duplication
---
## Error Handling & Logging
- Activity-level failure tracking
- Retry policy configured
- Failed runs can be reprocessed using ingestion date partitions
---
## Security Considerations
- Connection strings referenced via Azure Key Vault (placeholder)
- No hard-coded credentials
- Managed identity recommended

## Linked Services & Integration Runtime

This project intentionally does not include concrete Azure Data Factory
Linked Service or Self-hosted Integration Runtime configurations.

Reason:
- Linked Services are environment-specific and vary across organizations
- Self-hosted Integration Runtime setup depends on network, firewall,
  and security policies managed by infrastructure teams
- The core focus of this project is pipeline design, control flow,
  parameterization, and data engineering logic

This approach reflects real-world enterprise practices where
data engineering logic and infrastructure configuration
are handled independently.

---
## Outcome
- Reliable raw data ingestion into Bronze layer
- Reusable and scalable pipeline design
- Production-style ADF implementation
- Interview-ready explanation of ingestion logic
