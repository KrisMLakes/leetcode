# Write your MySQL query statement below
select P.product_name, s.year, s.price from Product P, Sales s
where P.product_id = s.product_id