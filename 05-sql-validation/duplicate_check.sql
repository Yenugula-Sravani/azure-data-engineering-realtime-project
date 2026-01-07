-- Duplicate Order ID Check

SELECT order_id, COUNT(*) AS duplicate_count
FROM silver_orders
GROUP BY order_id
HAVING COUNT(*) > 1;
