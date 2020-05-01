select date_trunc('day', occurred_at), channel, count(*) as c
from web_events
group by 1, 2
order by c desc;


select channel, avg(c) from 
(select date_trunc('day', occurred_at) as day, channel, count(*) as c
from web_events
group by 1, 2) as web_events_count_by_day_channel
group by 1
order by 2 desc;


-- direct  4.8964879852125693
-- organic 1.6672504378283713
-- facebook    1.5983471074380165
-- adwords 1.5701906412478336
-- twitter 1.3166666666666667
-- banner  1.2899728997289973