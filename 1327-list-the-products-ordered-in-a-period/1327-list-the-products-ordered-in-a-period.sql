# Write your MySQL query statement below
select product_name, sum(unit) as unit
from Products P JOIN Orders O
ON P.product_id = O.product_id
Where O.order_date between "2020-02-01" and "2020-02-29"
group by product_name
having unit >=100