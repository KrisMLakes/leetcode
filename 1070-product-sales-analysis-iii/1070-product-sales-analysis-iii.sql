# Write your MySQL query statement below
select S1.product_id, S2.first_year, S1.quantity, S1.price
from Sales S1,
(select product_id, min(year) as first_year
from Sales 
group by product_id) S2
where S1.product_id = S2.product_id
and S1.year = S2.first_year
