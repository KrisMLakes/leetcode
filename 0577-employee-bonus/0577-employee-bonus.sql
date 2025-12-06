# Write your MySQL query statement below
select E.name , B.bonus
from Employee E LEFT OUTER JOIN Bonus B
ON E.empID = B.empID
where B.bonus < 1000 or B.bonus is null