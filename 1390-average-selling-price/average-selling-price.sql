# Write your MySQL query statement below
SELECT a.product_id , 
            CASE 
                WHEN SUM(b.units) IS NULL THEN 0
                ELSE ROUND((SUM(a.price*b.units)/SUM(b.units)),2)
            END AS average_price
FROM Prices a
LEFT JOIN UnitsSold b
ON a.product_id=b.product_id 
AND b.purchase_date BETWEEN a.start_date AND a.end_date
GROUP BY product_id;
