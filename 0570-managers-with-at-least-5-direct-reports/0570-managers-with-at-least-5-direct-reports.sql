# Write your MySQL query statement below

select E.name from 
(select managerId,count(id) as empId
from Employee 
group by managerId) P, Employee E
where P.empId >=5
and P.managerId = E.id
