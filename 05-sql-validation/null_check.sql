-- Null Value Validation for Critical Columns

SELECT *
FROM silver_orders
WHERE order_id IS NULL
   OR order_date IS NULL
   OR order_amount IS NULL;
