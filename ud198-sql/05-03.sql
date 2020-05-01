--1. In the accounts table, there is a column holding the website for each company. The last three digits specify what type of web address they are using. A list of extensions (and pricing) is provided here. Pull these extensions and provide how many of each website type exist in the accounts table.
select right(website, 3) ext, count(*) from accounts group by 1;

--2. There is much debate about how much the name (or even the first letter of a company name) matters. Use the accounts table to pull the first letter of each company name to see the distribution of company names that begin with each letter (or number).
select left(name, 1), count(*) from accounts group by 1 order by 2 desc;

--3. Use the accounts table and a CASE statement to create two groups: one group of company names that start with a number and a second group of those company names that start with a letter. What proportion of company names start with a letter?
select sum(num) nums, sum(alp) alps
from (
    select name,
    (left(name, 1) ~    '\d')::integer as num, 
    (left(name, 1) ~ '[^\d]')::integer as alp
    from accounts
) t;

select avg(num) nums, avg(alp) alps
from (
    select name,
    (left(name, 1) ~    '\d')::integer as num, 
    (left(name, 1) ~ '[^\d]')::integer as alp
    from accounts
) t;

select sum(num) nums, sum(letter) letters
from (
    select name,
    case when left(name, 1) in ('0','1','2','3','4','5','6','7','8','9') then 1 else 0 end as num, 
    case when left(name, 1) in ('0','1','2','3','4','5','6','7','8','9') then 0 else 1 end as letter
    from accounts
) t;

--4. Consider vowels as a, e, i, o, and u. What proportion of company names start with a vowel, and what percent start with anything else?
select sum(vowels) vowels, sum(consonant) consonant
from (
    select name,
    (left(name, 1) ~ '[aeiouAEIOU]' )::integer as vowels,
    (left(name, 1) ~ '[^aeiouAEIOU]')::integer as consonant
    from accounts
) t;

select sum(vowels) vowels, sum(other) other
from (
    select name,
    case when left(lower(name), 1) in ('a','e','i','o','u') then 1 else 0 end as vowels, 
    case when left(lower(name), 1) in ('a','e','i','o','u') then 0 else 1 end as other
    from accounts
) t;