-- Section1
update products
JOIN ( select od.product_id,SUM(quantity) AS TotalItemsOrdered FROM order_details od
GROUP BY od.product_id) AS m
ON m.product_id=products.id
set total_profit=price*m.TotalItemsOrdered
-- Section2
select dc.id from  (
select d.delivery_center_id,AVG(d.delivered_at-d.received_at) avg_dr from deliveries d 
where d.delivered_at is not null 
group by d.delivery_center_id
order by avg_dr
LIMIT 5
) AS jM 
order by jM.avg_dr DESC
LIMIT 5
-- Section3
select p.id from products p
join order_details od on p.id=od.product_id
join orders o on od.order_id=o.id
where o.created_at  <=p.created_at  + INTERVAL 7 DAY and p.created_at<=o.created_at 
group by p.id
having count(p.id)<10