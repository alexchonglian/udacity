select
standard_amt_usd,
sum(standard_amt_usd) over (order by occurred_at) as running_total
from orders;