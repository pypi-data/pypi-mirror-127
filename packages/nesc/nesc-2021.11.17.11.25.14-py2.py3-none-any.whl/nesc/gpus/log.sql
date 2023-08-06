WITH log AS (
    SELECT distinct_id,
       anonymous_id,
       user_id,
--     time,
       recv_time,
       proc_time,
       type,
       event,
       properties['prod_code']  AS prod_code,
       properties['prod_name']  AS prod_name,
       properties['prod_type']  AS prod_type,
       properties['Mobile_tel'] AS Mobile_tel

FROM smartdata.ods_events
)
SELECT *
FROM log
WHERE prod_name IS NOT NULL

LIMIT 10
