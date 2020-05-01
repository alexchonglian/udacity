--1.Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.


with
SRT as ( -- stands for sales_region_total
    select s.name sales, r.name region, sum(o.total_amt_usd) total_amt
    from orders o
    join accounts a on a.id = o.account_id
    join sales_reps s on s.id = a.sales_rep_id
    join region r on r.id = s.region_id
    group by 1,2
),

RM as ( -- stands for region_max
    select SRT.region as region, max(SRT.total_amt) as max_amt from SRT group by 1
)

select SRT.sales, SRT.region, SRT.total_amt
from RM join SRT on SRT.region = RM.region and SRT.total_amt = RM.max_amt;


--2.For the region with the largest sales total_amt_usd, how many total orders were placed?

with 
T as (
    select r.name rname, count(o.id), sum(o.total_amt_usd) total_amt
    from orders o
    join accounts a on a.id = o.account_id
    join sales_reps s on s.id = a.sales_rep_id
    join region r on r.id = s.region_id
    group by 1
)

select r.name rname, count(o.id), sum(o.total_amt_usd) total_amt
from orders o
join accounts a on a.id = o.account_id
join sales_reps s on s.id = a.sales_rep_id
join region r on r.id = s.region_id
group by 1
having sum(o.total_amt_usd) = (select max(T.total_amt) from T);


--or
with 
T as (
    select r.name rname, count(o.id), sum(o.total_amt_usd) total_amt
    from orders o
    join accounts a on a.id = o.account_id
    join sales_reps s on s.id = a.sales_rep_id
    join region r on r.id = s.region_id
    group by 1
)
select T.rname, T.count, T.total_amt from T
where T.total_amt = (select max(T.total_amt) from T);



--3.How many accounts had more total purchases than the account name which has bought the most standard_qty paper throughout their lifetime as a customer?
with T as (
    select a.name, sum(o.standard_qty) standard, sum(o.total) total
    from orders o join accounts a on o.account_id = a.id
    group by 1
    order by 2 desc
    limit 1
),
    N as (
    select a.name
    from orders o join accounts a on o.account_id = a.id
    group by 1
    having sum(o.total) > (select T.total from T)
)
select count(*)
from N;

--4.For the customer that spent the most (in total over their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel?
with t as (
    select a.id, sum(o.total_amt_usd) total
    from orders o join accounts a on o.account_id = a.id
    group by 1
    order by 2 desc
    limit 1
)
select w.channel, a.name, count(w.id)
from web_events w join accounts a on w.account_id = a.id
where w.account_id = (select id from t)
group by 1, 2
order by 3 desc;

--5.What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts?

with t as (
    select a.id, sum(o.total_amt_usd) total
    from orders o join accounts a on o.account_id = a.id
    group by 1
    order by 2 desc
    limit 10
)
select avg(total) from t;

--6.What is the lifetime average amount spent in terms of total_amt_usd, including only the companies that spent more per order, on average, than the average of all orders.

with t as (
    select o.account_id, avg(o.total_amt_usd) as avg_amt
    from orders o
    group by 1
    having avg(o.total_amt_usd) > (select avg(o.total_amt_usd) from orders o)
)
select avg(avg_amt) from t;