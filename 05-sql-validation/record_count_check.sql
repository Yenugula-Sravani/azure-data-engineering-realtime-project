-- Record Count Validation: Source vs Bronze

SELECT 'SOURCE' AS layer, COUNT(*) AS record_count
FROM source_orders
UNION ALL
SELECT 'BRONZE' AS layer, COUNT(*) AS record_count
FROM bronze_orders;
