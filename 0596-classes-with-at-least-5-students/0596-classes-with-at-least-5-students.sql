# Write your MySQL query statement below
select distinct C1.class
from Courses C1, 
(select class, count(student) as studs
from Courses
group by class) C2
where C1.class = C2.class
and C2.studs >= 5