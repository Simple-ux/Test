-- 2.1 --
select rep.user_id, 
(
select  sum(rep.reward)
from reports rep 
where rep.created_at between  '2022-01-01' and  '2022-12-31'
)

from reports rep
where rep.created_at between  '2021-01-01' and  '2022-01-01';


-- 2.2 --

SELECT rep.barcode, rep.price, pos.title  
FROM reports rep
left join pos
on rep.pos_id = pos.id;  

-- Не понятно что необходимо сделать во второй задаче по условию, поэтому сделал просто join