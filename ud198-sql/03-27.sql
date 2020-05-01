-- 1. Find the sales in terms of total dollars for all orders in each year, ordered from greatest to least. Do you notice any trends in the yearly sales totals?
select date_trunc('year', o.occurred_at), sum(o.total_amt_usd)
from orders o
group by 1
order by 1;

-- 2. Which month did Parch & Posey have the greatest sales in terms of total dollars? Are all months evenly represented by the dataset?
select date_part('month', o.occurred_at), sum(o.total_amt_usd)
from orders o
group by 1
order by 2 desc
limit 1;

-- 3. Which year did Parch & Posey have the greatest sales in terms of total number of orders? Are all years evenly represented by the dataset?
select date_trunc('year', o.occurred_at), count(o)
from orders o
group by 1
order by 2 desc
limit 1;


-- 4. Which month did Parch & Posey have the greatest sales in terms of total number of orders? Are all months evenly represented by the dataset?
select date_part('month', o.occurred_at), count(o)
from orders o
group by 1
order by 2 desc
limit 1;

-- 5. In which month of which year did Walmart spend the most on gloss paper in terms of dollars?
select
    date_part('year', o.occurred_at) as y,
    date_part('month', o.occurred_at) as m,
    sum(gloss_amt_usd) as amt
from orders o inner join accounts a on o.account_id = a.id 
where a.name = 'Walmart'
group by 1, 2
order by 3 desc;