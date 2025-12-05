# Write your MySQL query statement below
select W.id from Weather W, Weather W1
where W.recordDate = DATE_ADD(W1.recordDate, INTERVAL 1 DAY)
and W.temperature > W1.temperature