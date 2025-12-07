# Write your MySQL query statement below
select

ROUND(COUNT(DISTINCT A1.player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity),2)
as fraction
from 
Activity A1 JOIN
(select player_id, min(event_date) first
from Activity A
group by player_id) A2
ON A1.player_id = A2.player_id
AND a1.event_date = DATE_ADD(a2.first, INTERVAL 1 DAY);
