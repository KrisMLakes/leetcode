# Write your MySQL query statement below
select max(N1.num) as num
from MyNumbers N1,
(select num, count(num) cnt
from MyNumbers
group by num) N2
where N1.num = N2.num
and N2.cnt = 1