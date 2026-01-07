-- Sales Amount Reconciliation: Silver vs Gold

SELECT
  (SELECT SUM(order_amount) FROM silver_orders) AS silver_total,
  (SELECT SUM(total_sales_amount) FROM gold_daily_sales_summary) AS gold_total;
