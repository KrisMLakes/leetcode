# Write your MySQL query statement below
WITH DailySum AS (
    select visited_on, sum(amount) as dailysum
    from Customer 
    group by visited_on
), 
RollingAverage AS (
    select visited_on, 
    sum(dailysum) over (Order by visited_on ROWS 6 preceding) as amount,
    round(avg(dailysum) over (Order by visited_on ROWS 6 preceding),2 )as average_amount,
    ROW_NUMBER() over (order by visited_on) as rn
    from DailySum
)
select visited_on, amount, average_amount from RollingAverage
where rn >= 7