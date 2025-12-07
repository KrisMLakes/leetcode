# Write your MySQL query statement below

select round(100*sum( case  when D.order_date = D.customer_pref_delivery_date then 1 else 0 end)/count(D.customer_id),2)
as immediate_percentage
from
Delivery D,
(select customer_id, min(order_date) order_date
from Delivery
group by customer_id) F
where D.customer_id = F.customer_id
and D.order_date = F.order_date