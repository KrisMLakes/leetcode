# Write your MySQL query statement below
select product_name, unit from 
(select product_name, sum(unit) as unit
from Products P, Orders O
where P.product_id = O.product_id
and O.order_date like "2020-02%" 
group by product_name) T
where unit >=100