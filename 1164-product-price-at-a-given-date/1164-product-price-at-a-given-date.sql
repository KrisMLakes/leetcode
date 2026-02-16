# Write your MySQL query statement below
select product_id, new_price as price from 
(select product_id, new_price, DENSE_RANK() OVER (PARTITION by product_id ORDER BY change_date desc) as rnk
from Products
where change_date <= "2019-08-16" ) as ranked_prod 
where rnk = 1


union 
select product_id, 10 as price
from Products
group by product_id
having min(change_date) > "2019-08-16"