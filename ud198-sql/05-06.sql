--Use the accounts table to create first and last name columns that hold the first and last names for the primary_poc.
select
left(primary_poc, strpos(primary_poc, ' ')-1),
right(primary_poc, length(primary_poc)-strpos(primary_poc, ' '))
from accounts limit 2;

--Now see if you can do the same thing for every rep name in the sales_reps table. Again provide first and last name columns.
select
left(name, strpos(name, ' ')-1),
right(name, length(name)-strpos(name, ' '))
from sales_reps limit 2;