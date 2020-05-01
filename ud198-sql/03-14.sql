--1. Which account (by name) placed the earliest order? Your solution should have the account name and the date of the order.
select a.name, o.occurred_at from accounts a inner join orders o on o.account_id = a.id order by o.occurred_at limit 1;

select name from accounts where id = 
(
    select account_id from orders where occurred_at = (select min(occurred_at) from orders)
);

--2. Find the total sales in usd for each account. You should include two columns - the total sales for each company's orders in usd and the company name.
select a.name, sum(o.total_amt_usd) from accounts a inner join orders o on o.account_id = a.id group by 1;

--3. Via what channel did the most recent (latest) web_event occur, which account was associated with this web_event? Your query should return only three values - the date, channel, and account name.

select w.occurred_at, w.channel, a.name
from web_events w
inner join accounts a on a.id = w.account_id
where w.occurred_at = (select max(occurred_at) from web_events);

-- better performance
select w.occurred_at, w.channel, a.name
from (
    select * from web_events w where w.occurred_at = (select max(occurred_at) from web_events)
) as w
inner join accounts a on a.id = w.account_id;


--4. Find the total number of times each type of channel from the web_events was used. Your final table should have two columns - the channel and the number of times the channel was used.
select w.channel, count(*)
from web_events w
group by w.channel

--5. Who was the primary contact associated with the earliest web_event?
select a.primary_poc
from (
    select * from web_events w where w.occurred_at = (select min(occurred_at) from web_events)
) as w
inner join accounts a on a.id = w.account_id;

select a.primary_poc
from web_events w join accounts a on a.id = w.account_id
order by w.occurred_at
limit 1;

--6. What was the smallest order placed by each account in terms of total usd. Provide only two columns - the account name and the total usd. Order from smallest dollar amounts to largest.
select a.name, min(total_amt_usd)
from accounts a join orders o on a.id = o.account_id
group by 1 order by 2;

--7. Find the number of sales reps in each region. Your final table should have two columns - the region and the number of sales_reps. Order from fewest reps to most reps.
select r.name, count(*)
from sales_reps s inner join region r on r.id = s.region_id
group by 1 order by 2;
