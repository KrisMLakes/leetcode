# Write your MySQL query statement below





(select name as results
from Users join MovieRating using (user_id)
group by user_id
order by (count(rating)) desc, name asc
limit 1)

union all

(select title as results
from Movies join MovieRating using(movie_id)
where created_at like "2020-02%"
group by movie_id
order by avg(rating) desc, title asc
limit 1)