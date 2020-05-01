select min(date_trunc('month', occurred_at)) from orders;

select avg(standard_qty)
from orders
where date_trunc('month', occurred_at) = (
    select min(date_trunc('month', occurred_at)) from orders
);

select avg(gloss_qty)
from orders
where date_trunc('month', occurred_at) = (
    select min(date_trunc('month', occurred_at)) from orders
);

select avg(poster_qty)
from orders
where date_trunc('month', occurred_at) = (
    select min(date_trunc('month', occurred_at)) from orders
);

select sum(total_amt_usd)
from orders
where date_trunc('month', occurred_at) = (
    select min(date_trunc('month', occurred_at)) from orders
);