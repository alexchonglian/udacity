select
standard_amt_usd,
occurred_at,
sum(standard_amt_usd) over (partition by date_trunc('year', occurred_at) order by occurred_at) as running_total
from orders order by 2;

select
standard_amt_usd,
date_part('year', occurred_at) as year,
occurred_at,
sum(standard_amt_usd) over (partition by 2 order by occurred_at) as running_total
from orders order by 2;