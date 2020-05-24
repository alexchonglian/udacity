select a.id, s.id from accounts a
full outer join sales_reps s
on a.sales_rep_id = s.id
where a.sales_rep_id is null or s.id is null;