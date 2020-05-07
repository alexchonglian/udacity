select
id,
account_id,
occurred_at,
row_number() over (order by id) as row_num
from orders;

select
id,
account_id,
occurred_at,
row_number() over (order by occurred_at) as row_num
from orders;

select
id,
account_id,
occurred_at,
row_number() over (partition by account_id order by occurred_at) as row_num
from orders;

select
id,
account_id,
occurred_at,
rank() over (partition by account_id order by occurred_at) as row_num
from orders;

-- differences between row_number(), rank(), dense_rank()
-- 2 rows have same value
-- same rank, row_number increments
-- rank skip value, dense_rank doesn't
-- e.g.
value, row_num, rank, dense_rank
  11      1      1      1
  12      2      2      2
  12      3      2      2
  15      4      4      3
  15      5      4      3
  16      6      6      4
