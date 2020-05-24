--Quiz 1:
SELECT * FROM accounts
UNION ALL
SELECT * FROM accounts


--Quiz 2:
SELECT * FROM accounts WHERE name = 'Walmart'
UNION ALL
SELECT * FROM accounts WHERE name = 'Disney'


--Quiz 3:
WITH double_accounts AS (
    SELECT * FROM accounts
    UNION ALL
    SELECT * FROM accounts
)
SELECT name, COUNT(*) AS name_count FROM double_accounts 
GROUP BY 1
ORDER BY 2 DESC