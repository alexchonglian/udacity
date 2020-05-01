--Use DISTINCT to test if there are any accounts associated with more than one region.

select a.name, count(r.id)
from accounts a
join sales_reps s on s.id = a.sales_rep_id
join region r on r.id = s.region_id
group by a.name
having count(r.id) > 1;


--Have any sales reps worked on more than one account?

select s.name, count(a.id)
from sales_reps s
join accounts a on s.id = a.sales_rep_id
group by 1
having count(a.id) > 1;