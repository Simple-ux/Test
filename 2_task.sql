-- PostgreSQL

select * from table_1
where id not in 
	(select * from 
		(select min(id) from table_1 group by марка, дилер) as d)