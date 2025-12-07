# Write your MySQL query statement below

select S.user_id, ROUND(IFNULL(R.rate, 0),2) as confirmation_rate
from
Signups S
LEFT JOIN 
(select C.user_id, C.confirms/T.totals as rate
from 
(select user_id, count(action) as confirms
from Confirmations
where action = 'confirmed'
group by user_id ) C,
(select user_id, count(action) as totals
from Confirmations
group by user_id ) T
where C.user_id = T.user_id) R
ON S.user_id = R.user_id
