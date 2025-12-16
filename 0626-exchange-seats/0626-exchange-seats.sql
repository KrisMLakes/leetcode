# Write your MySQL query statement below
select max(s3.id) as id, s3.student from 
(select (S1.id-1) as id , S1.student
from Seat S2, 
(select id, student
from Seat 
where mod(id,2) = 0 ) S1
where S1.id-1 = S2.id
union
select (S1.id+1) as id , S1.student
from Seat S2, 
(select id, student
from Seat 
where mod(id,2) = 1 ) S1
where S1.id+1 = S2.id
union
select max(S5.id) as id, S5.student
from Seat S5,
(select max(id) as id, student
from Seat
where mod(id,2)=1) S6
where S6.id = S5.id
group by S5.student
) S3
group by S3.student
order by S3.id 