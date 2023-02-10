-- PostgreSQL

select distinct
    count(марка) over (partition by t.дата, t.тип) as кол_во_авто,
    t.тип,
    sum(стоимость) over (partition by t.дата, t.тип) as итоговые_сборы,
    round(sum(стоимость) over (partition by t.дата, t.тип) - sum(стоимость * t2.comission) over (partition by t.дата, t.тип)) as после_вычета,
    max(дилер) over(partition by t.дата order by count(дилер) desc),
    round((sum(стоимость) over (partition by t.дата, t.тип) - sum(стоимость * t2.comission) over (partition by t.дата, t.тип)) / t3.значение) as в_валюте,
    t.дата 
from table_1 t 
    join table_2 t2
        on t2.primary_key like CONCAT('%', t.дилер  ,'%') and 
        t2.primary_key like CONCAT('%', t.марка  ,'%')
    join table_3 t3
        on t3.дата = t.дата
group by дилер,t.марка,t.тип,t.стоимость,t2.comission,t3.значение,t.дата
order by дата
