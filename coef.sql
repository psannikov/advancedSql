with t1 as
(select data from additionalhw2 where genome='genom1' and split=2),
t2 as
(select data from additionalhw2 where genome='genom2' and split=2),
t3 as
(select count(distinct t1.data) from t1
inner join t2 on t1.data=t2.data),
t4 as
(select count(*) from
(select * from t1 union select * from t2) as B)
select (select * from t3)/(select * from t4)::numeric;