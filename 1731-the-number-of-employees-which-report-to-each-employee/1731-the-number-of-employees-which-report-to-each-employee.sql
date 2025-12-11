# Write your MySQL query statement below
select E2.employee_id, E2.name, E1.cnt as reports_count, E1.age1 as average_age
from Employees E2,
(select reports_to, count(reports_to) cnt, round(avg(age),0) age1
from Employees
group by reports_to) E1
where E2.employee_id = E1.reports_to
order by employee_id