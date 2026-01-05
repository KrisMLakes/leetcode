# Write your MySQL query statement below

select sell_date, count(product) as num_sold, group_concat(product ORDER BY product SEPARATOR ",") as products
from (select distinct sell_date, product from Activities)  Activities
group by sell_date