# Write your MySQL query statement below
select d.name as Department,  R.name as Employee, salary as Salary 
from (select name, salary, departmentId ,  DENSE_RANK() OVER (PARTITION BY departmentID ORDER BY salary desc ) as rnk
from Employee) R JOIN Department d
ON R.departmentId  = d.id
where rnk <=3

