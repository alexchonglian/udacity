select
    id,
    account_id,
    occurred_at,
    standard_qty,
    ntile(4) over w as quartile,
    ntile(5) over w as quintile,
    ntile(100) over w as percentile
from orders
window w as (order by standard_qty)
order by standard_qty desc;
