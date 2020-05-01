--===================================================================================================
--1.Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.

---- step 1. total_amt_usd totals associated with each sales rep, and their region
select s.name sname, r.name rname, sum(o.total_amt_usd) total_amt
from orders o
join accounts a on a.id = o.account_id
join sales_reps s on s.id = a.sales_rep_id
join region r on r.id = s.region_id
group by 1,2
order by 3 desc;

---- step 2. max total amount for each region
select t1.rname, max(t1.total_amt)
from (
    select s.name sname, r.name rname, sum(o.total_amt_usd) total_amt
    from orders o
    join accounts a on a.id = o.account_id
    join sales_reps s on s.id = a.sales_rep_id
    join region r on r.id = s.region_id
    group by 1,2
) t1
group by 1;

-- Midwest   675637.19
-- Southeast 1098137.72
-- Northeast 1010690.60
-- West      886244.12

---- step 3. join result of step 1 and step 2, matching region and amount

select SRT.sales, SRT.region, SRT.total_amt

from (
    select t.region as region, max(t.total_amt) as max_amt
    from (
        select s.name sales, r.name region, sum(o.total_amt_usd) total_amt
        from orders o
        join accounts a on a.id = o.account_id
        join sales_reps s on s.id = a.sales_rep_id
        join region r on r.id = s.region_id
        group by 1,2
    ) t
    group by 1
) as RM -- stands for region_max

inner join (
    select s.name sales, r.name region, sum(o.total_amt_usd) total_amt
    from orders o
    join accounts a on a.id = o.account_id
    join sales_reps s on s.id = a.sales_rep_id
    join region r on r.id = s.region_id
    group by 1,2
) as SRT -- stands for sales_region_total

on SRT.region = RM.region and SRT.total_amt = RM.max_amt;


-- Charles Bidwell      Midwest     675637.19
-- Earlie Schleusner    Southeast   1098137.72
-- Georgianna Chisholm  West        886244.12
-- Tia Amato            Northeast   1010690.60



--===================================================================================================
--2.For the region with the largest (sum) of sales total_amt_usd, how many total (count) orders were placed?

----step 1
select r.name rname, count(o.id), sum(o.total_amt_usd) total_amt
from orders o
join accounts a on a.id = o.account_id
join sales_reps s on s.id = a.sales_rep_id
join region r on r.id = s.region_id
group by 1
order by 3 desc;

----step 2
select max(T.total_amt)
from (
    select r.name rname, sum(o.total_amt_usd) total_amt
    from orders o
    join accounts a on a.id = o.account_id
    join sales_reps s on s.id = a.sales_rep_id
    join region r on r.id = s.region_id
    group by 1
) as T

----step 3
select r.name rname, count(o.id), sum(o.total_amt_usd) total_amt
from orders o
join accounts a on a.id = o.account_id
join sales_reps s on s.id = a.sales_rep_id
join region r on r.id = s.region_id
group by 1
having sum(o.total_amt_usd) = (
    select max(T.total_amt)
    from (
        select r.name rname, sum(o.total_amt_usd) total_amt
        from orders o
        join accounts a on a.id = o.account_id
        join sales_reps s on s.id = a.sales_rep_id
        join region r on r.id = s.region_id
        group by 1
    ) as T
)


--===================================================================================================
--3.How many accounts had more total purchases than the account name which has bought the most standard_qty paper throughout their lifetime as a customer?

---- step 1
select a.name, sum(o.standard_qty) standard, sum(o.total) total
from orders o join accounts a on o.account_id = a.id
group by 1
order by 2 desc
limit 1;

---- step 2. accounts with more total sales
select a.name
from orders o join accounts a on o.account_id = a.id
group by 1
having sum(o.total) > (
    select T.total 
    from (
        select a.name, sum(o.standard_qty) standard, sum(o.total) total
        from orders o join accounts a on o.account_id = a.id
        group by 1
        order by 2 desc
        limit 1
    ) as T);

---- step 3. get the count
select count(*)
from (
    select a.name
    from orders o join accounts a on o.account_id = a.id
    group by 1
    having sum(o.total) > (
        select T.total 
        from (
            select a.name, sum(o.standard_qty) standard, sum(o.total) total
            from orders o join accounts a on o.account_id = a.id
            group by 1
            order by 2 desc
            limit 1
        ) as T)
) N;


--===================================================================================================
--4.For the customer that spent the most (in total over their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel?

----step 1 select account id for the one with most total amount 
select a.id, sum(o.total_amt_usd) total
from orders o join accounts a on o.account_id = a.id
group by 1
order by 2 desc
limit 1;

----step 2 keep id only
select id from (
    select a.id, sum(o.total_amt_usd) total
    from orders o join accounts a on o.account_id = a.id
    group by 1
    order by 2 desc
    limit 1
);


----step 3 filter by that id
select w.channel, count(w.id)
from web_events w
where w.account_id = (
    select id from (
        select a.id, sum(o.total_amt_usd) total
        from orders o join accounts a on o.account_id = a.id
        group by 1
        order by 2 desc
        limit 1
    ) t
)
group by 1
order by 2 desc;

---- or 
select w.channel, a.name, count(w.id)
from web_events w join accounts a on w.account_id = a.id
where w.account_id = (
    select id from (
        select a.id, sum(o.total_amt_usd) total
        from orders o join accounts a on o.account_id = a.id
        group by 1
        order by 2 desc
        limit 1
    ) t
)
group by 1, 2
order by 3 desc;

--5.What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts?

----step 1, top 10 total spending
select a.id, sum(o.total_amt_usd) total
from orders o join accounts a on o.account_id = a.id
group by 1
order by 2 desc
limit 10;

----step 2, get their average
select avg(total) from (
    select a.id, sum(o.total_amt_usd) total
    from orders o join accounts a on o.account_id = a.id
    group by 1
    order by 2 desc
    limit 10
) t;

--6.What is the lifetime average amount spent in terms of total_amt_usd, including only the companies that spent more per order, on average, than the average of all orders.

----step 1 lifetime avg
select avg(o.total_amt_usd) from orders o;

----step 2 find accounts spend more per order than average
select o.account_id, avg(o.total_amt_usd) as avg_amt
from orders o
group by 1
having avg(o.total_amt_usd) > (select avg(o.total_amt_usd) from orders o);

----step 3
select avg(avg_amt) from (
    select o.account_id, avg(o.total_amt_usd) as avg_amt
    from orders o
    group by 1
    having avg(o.total_amt_usd) > (select avg(o.total_amt_usd) from orders o)
) t;

