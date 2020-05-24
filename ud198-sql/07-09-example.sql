self join with aid
想象同一个表，copy两份，再join

create table web (id varchar, aid varchar);

insert into web (id, aid) values 
('w1', 'a1'),
('w2', 'a1'),
('w3', 'a1'),
('w4', 'a2'),
('w5', 'a2');

select w1.id, w2.id from web w1 left join web w2 on w1.aid = w2.aid;
 id | id 
----+----
 w1 | w3
 w1 | w2
 w1 | w1
 w2 | w3
 w2 | w2
 w2 | w1
 w3 | w3
 w3 | w2
 w3 | w1
 w4 | w5
 w4 | w4
 w5 | w5
 w5 | w4
(13 rows)

create table web2 (id varchar, aid varchar);

insert into web2 (id, aid) values 
('w1', 'a4'),
('w2', 'a4'),
('w3', 'a4'),
('w4', 'a5'),
('w5', 'a5');


select aid from web union     select aid from web2;
select aid from web union all select aid from web2;

select * from web union select * from web2;