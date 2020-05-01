--1. How many of the sales reps have more than 5 accounts that they manage?
select sales_rep_id, count(*) as c
from accounts
group by sales_rep_id
having count(*) > 5
order by c;

--2. How many accounts have more than 20 orders?
select a.id, count(o.id)
from orders o
inner join accounts a on a.id = o.account_id
group by 1
having count(o.id) > 20
order by 2;

select a.id, a.name, count(*) num_orders
from accounts a
join orders o on a.id = o.account_id
group by a.id, a.name
having count(*) > 20
order by num_orders;

--3. Which account has the most orders?
select account_id, count(*)
from orders
group by 1
order by 2 desc
limit 1;

--4. Which accounts spent more than 30,000 usd total across all orders?
select o.account_id, sum(o.total_amt_usd)
from orders o
group by 1
having sum(o.total_amt_usd) > 30000
order by 2;

select a.id, sum(o.total_amt_usd) total_spent
from accounts a
join orders o on a.id = o.account_id
group by 1
having sum(o.total_amt_usd) > 30000
order by 2;


--5. Which accounts spent less than 1,000 usd total across all orders?


--6. Which account has spent the most with us?


--7. Which account has spent the least with us?


--8. Which accounts used facebook as a channel to contact customers more than 6 times?
select account_id, count(*) as c
from web_events w
where channel = 'facebook'
group by 1
having count(*) > 6
order by 2;

--9. Which account used facebook most as a channel?
select account_id, count(*) as c
from web_events w
where channel = 'facebook'
group by 1
order by 2 desc
limit 1;

--10. Which channel was most frequently used by most accounts?
select channel, count(*) as c
from web_events w
group by 1
order by 2 desc
limit 1;
