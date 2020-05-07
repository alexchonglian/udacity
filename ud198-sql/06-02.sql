select
    standard_qty,
    sum(standard_qty) over (order by occurred_at) as running_total
from orders;


select
    standard_qty,
    date_trunc('month', occurred_at) as month,
    sum(standard_qty) over (partition by date_trunc('month', occurred_at) order by occurred_at) as running_total
from orders;