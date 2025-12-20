# Write your MySQL query statement below

select ROUND(sum(tiv_2016),2) as tiv_2016
from Insurance I,
(select lat, lon from Insurance 
group by lat, lon
having count(lat) = 1 and count(lon) = 1) P1
where I.lat = P1.lat
and I.lon = P1.lon 
and I.pid in 
(select pid from Insurance 
where tiv_2015 in (select tiv_2015  from Insurance
group by tiv_2015
having count(tiv_2015) > 1)
)






