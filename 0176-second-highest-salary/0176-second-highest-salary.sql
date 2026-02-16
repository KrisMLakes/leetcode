# Write your MySQL query statement below
Select (select salary  from 
(select salary, DENSE_RANK() OVER (ORDER BY salary desc) rnk
from Employee) as salary_rank
where rnk = 2 limit 1) as SecondHighestSalary