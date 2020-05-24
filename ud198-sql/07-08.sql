select
    o1.id as o1_id,
    o1.account_id as o1_account_id,
    o1.occurred_at as o1_occurred_at,
    o2.id as o2_id,
    o2.account_id as o2_account_id,
    o2.occurred_at as o2_occurred_at
from orders o1
left join orders o2
on o1.account_id = o2.account_id
and o1.occurred_at < o2.occurred_at
and o2.occurred_at <= o1.occurred_at + interval '28 days'
order by o1.account_id, o1.occurred_at;