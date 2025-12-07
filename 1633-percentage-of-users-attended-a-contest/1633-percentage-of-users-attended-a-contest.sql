# Write your MySQL query statement below




select contest_id, round((count(R.user_id)/user_count)*100,2)  as percentage
from Register R,
(select  count(user_id) as user_count 
from Users) C
group by contest_id
order by percentage desc, contest_id asc