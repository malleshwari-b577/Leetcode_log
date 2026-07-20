# Write your MySQL query statement below
SELECT a.name 
FROM Employee a
JOIN Employee b
ON b.managerId=a.id
GROUP BY b.managerId 
HAVING COUNT(*)>=5;