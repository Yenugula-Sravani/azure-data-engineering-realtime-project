# SQL Validation and Reconciliation

## Purpose
SQL validation scripts are used to ensure data accuracy, completeness,
and consistency after data ingestion and transformation.

These checks help verify that data migrated from source systems into
the Bronze, Silver, and Gold layers is reliable and trustworthy.

---

## Validation Scenarios Covered

### 1️⃣ Record Count Validation
- Compare source vs target record counts
- Detect missing or duplicate records

### 2️⃣ Duplicate Record Checks
- Identify duplicate business keys
- Ensure deduplication logic worked as expected

### 3️⃣ Null Value Validation
- Detect unexpected nulls in critical columns
- Validate mandatory fields

### 4️⃣ Data Reconciliation
- Compare aggregated values between layers
- Ensure numerical consistency (e.g., total sales)

---

## When These Checks Are Used
- Post-ingestion validation (Bronze layer)
- Post-transformation validation (Silver layer)
- Post-aggregation validation (Gold layer)
- During reprocessing or reruns

---

## Benefits
- Improves data trust and reliability
- Enables early detection of data issues
- Supports audit and compliance requirements
- Strengthens production readiness

---

## Outcome
- Verified and trusted datasets
- Clear validation strategy for interviews
- Reusable SQL validation patterns

