select id, account_id, total,
rank() over (partition by account_id order by total desc) as total_rank
from orders;