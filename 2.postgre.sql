-- 2.1 --
select
    rep.user_id,
    (
        select
            sum(rep.reward)
        from
            reports rep
        where
            rep.created_at between '2022-01-01'
            and '2022-12-31'
    )
from
    reports rep
where
    rep.created_at between '2021-01-01'
    and '2022-01-01';

-- 2.2 --
select
    array_agg(rep.barcode),
    array_agg(rep.price)
FROM
    reports rep
    left join pos on rep.pos_id = pos.id
group by
    pos.title


-- без джоинов

-- select array_agg(rep.barcode), array_agg(rep.price)
-- FROM reports rep
-- group by rep.pos_id