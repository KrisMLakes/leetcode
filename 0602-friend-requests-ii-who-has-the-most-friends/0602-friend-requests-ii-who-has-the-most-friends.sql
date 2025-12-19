select id, sum(num1) as num from
((select accepter_id as id , count(requester_id) num1
from RequestAccepted 
group by accepter_id)
union all
(select requester_id as id , count(accepter_id) num1
from RequestAccepted 
group by requester_id)) A
group by A.id
order by sum(A.num1) desc
limit 1
