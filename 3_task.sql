-- PostgreSQL

select 
    дилер,
    sum(стоимость) over (partition by дилер order by дилер, дата 
        rows between unbounded preceding and current row) as нарастающий_итог,
    дата
from table_1