-- Section1
select id as order_id from orders
where status='warehouse'
order by order_id desc
-- Section2
select c.id as customer_id, c.name as customer_name  from customers c
where (select customer_id from orders o where o.customer_id)<>c.id
order by customer_name
-- Section3
with c as(
select o.data,count(*) from orders o
inner join customers c on c.id=o.customer_id and o.is_blocked<>1
group by o.data
),
c2 as(
select o.data,count(*) from orders o
inner join customers c on c.id=o.customer_id and o.is_blocked<>1
where o.status='canceled'
group by o.data
)
select c.data,format(c.count/c2.count*100,'0##') as cancellation_rate  from c

