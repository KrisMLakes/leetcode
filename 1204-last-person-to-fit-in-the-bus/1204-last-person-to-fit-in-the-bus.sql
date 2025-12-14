# Write your MySQL query statement below
WITH AcQueue AS (
SELECT 
person_name,
sum(weight) OVER (ORDER BY turn) as Total_weight
from Queue

)
select person_name from AcQueue
where Total_weight <=1000
order by Total_weight desc
limit 1


