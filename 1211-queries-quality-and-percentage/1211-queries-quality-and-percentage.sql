# Write your MySQL query statement below

select Q1.query_name, round(avg(Q1.rating/Q1.position),2) as quality, 
round(100*(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)/count(*)),2) 
as poor_query_percentage
from Queries Q1
group by Q1.query_name