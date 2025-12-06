# Write your MySQL query statement below
select S.student_id, S.student_name, Su.subject_name, count(E.subject_name) as attended_exams
from Subjects Su
CROSS JOIN Students S 
LEFT  JOIN  Examinations E 
ON E.subject_name = Su.subject_name
and E.student_id = S.student_id
group by S.student_id, S.student_name, Su.subject_name
order by S.student_id, Su.subject_name