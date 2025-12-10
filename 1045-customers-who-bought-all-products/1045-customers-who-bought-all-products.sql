# Write your MySQL query statement below


select customer_id from
(select customer_id, count(pk) as cnt1
from 
(select distinct customer_id,  product_key as pk
from Customer ) C
group by customer_id) C1,
(select count(*) as cnt2 
from Product P) P
where C1.cnt1 = P.cnt2