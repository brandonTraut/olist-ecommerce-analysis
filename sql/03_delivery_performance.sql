CREATE VIEW v_delivery_performance
AS
SELECT order_id
	,order_date
	,delivered_date
	,estimated_delivery_date
	,CASE 
		WHEN delivered_date <= estimated_delivery_date
			THEN 'On Time'::TEXT
		ELSE 'Late'::TEXT
		END AS delivery_status
	,EXTRACT(day FROM delivered_date - order_date) AS actual_days
	,EXTRACT(day FROM estimated_delivery_date - order_date) AS estimated_days
FROM v_orders_complete;
