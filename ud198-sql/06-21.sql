--Use the NTILE functionality to divide the accounts into 4 levels in terms of the amount of standard_qty for their orders. Your resulting table should have the account_id, the occurred_at time for each order, the total amount of standard_qty paper purchased, and one of four levels in a standard_quartile column.

select 
account_id,
occurred_at,
standard_qty,
ntile(4) over (partition by account_id order by standard_qty) as quantile
from orders
order by account_id desc

--Use the NTILE functionality to divide the accounts into two levels in terms of the amount of gloss_qty for their orders. Your resulting table should have the account_id, the occurred_at time for each order, the total amount of gloss_qty paper purchased, and one of two levels in a gloss_half column.

select 
account_id,
occurred_at,
gloss_qty,
ntile(2) over (partition by account_id  order by gloss_qty) as binary
from orders
order by account_id desc

--Use the NTILE functionality to divide the orders for each account into 100 levels in terms of the amount of total_amt_usd for their orders. Your resulting table should have the account_id, the occurred_at time for each order, the total amount of total_amt_usd paper purchased, and one of 100 levels in a total_percentile column.

select 
account_id,
occurred_at,
total_amt_usd,
ntile(100) over (partition by account_id order by total_amt_usd) as percentile
from orders
order by account_id desc