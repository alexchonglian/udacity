SELECT account_id,
       standard_sum,
       LAG( standard_sum) OVER (ORDER BY standard_sum) AS lag,
       LEAD(standard_sum) OVER (ORDER BY standard_sum) AS lead,
       standard_sum - LAG(standard_sum) OVER (ORDER BY standard_sum)  AS lag_diff,
       LEAD(standard_sum) OVER (ORDER BY standard_sum) - standard_sum AS lead_diff
FROM (
    select
    account_id,
    sum(standard_qty) as standard_sum
    from orders
    group by 1
) as sub