select 
    a.name as aname,
    a.primary_poc,
    s.name as sname
from accounts a
join sales_reps s on a.sales_rep_id = s.id
and a.primary_poc < s.name;