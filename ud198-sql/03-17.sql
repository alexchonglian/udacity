-- 1. For each account, determine the average amount of each type of paper they purchased across their orders. Your result should have four columns - one for the account name and one for the average quantity purchased for each of the paper types for each account.
select a.name, avg(standard_qty) mean_standard, avg(gloss_qty) mean_gloss, avg(poster_qty) mean_poster
from accounts a inner join orders o on o.account_id = a.id
group by 1;

-- 2. For each account, determine the average amount spent per order on each paper type. Your result should have four columns - one for the account name and one for the average amount spent on each paper type.
select a.name, avg(standard_amt_usd) mean_standard, avg(gloss_amt_usd) mean_gloss, avg(poster_amt_usd) mean_poster
from accounts a inner join orders o on o.account_id = a.id
group by 1;

-- 3. Determine the number of times a particular channel was used in the web_events table for each sales rep. Your final table should have three columns - the name of the sales rep, the channel, and the number of occurrences. Order your table with the highest number of occurrences first.
select s.name, w.channel, count(*) num_events
from accounts a
join web_events w on a.id = w.account_id
join sales_reps s on s.id = a.sales_rep_id
group by s.name, w.channel
order by num_events desc;

-- 4. Determine the number of times a particular channel was used in the web_events table for each region. Your final table should have three columns - the region name, the channel, and the number of occurrences. Order your table with the highest number of occurrences first.
select r.name, w.channel, count(*) num_events
from accounts a
join web_events w on a.id = w.account_id
join sales_reps s on s.id = a.sales_rep_id
join region r on r.id = s.region_id
group by r.name, w.channel
order by num_events desc;