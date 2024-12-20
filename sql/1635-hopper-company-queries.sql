# Write your MySQL query statement below
-- output: month , active_drivers (incrementing) , accepted_rides

-- noticed some months missing , making a cte of all months to be safe
with year_months as (
    select 1 as month
    union
    select 2 as month
    union
    select 3 as month
    union
    select 4 as month
    union
    select 5 as month
    union
    select 6 as month
    union
    select 7 as month
    union
    select 8 as month
    union
    select 9 as month
    union
    select 10 as month
    union
    select 11 as month
    union
    select 12 as month
),

driver_join_months as (
	select driver_id, 
	(case when year(join_date)=2019 then '1' else month(join_date) end) `month`
	from Drivers 
	where year(join_date)<=2020
),

accepted_ride_months as (

    select month(requested_at) as `month`, a.ride_id
    from AcceptedRides a 
    join Rides r
    on r.ride_id = a.ride_id
    where year(requested_at)=2020
)

select t.month, 
count(distinct driver_id) active_drivers,
count(distinct rides.ride_id) accepted_rides 
from
    year_months as t
left join

    driver_join_months as d
on d.month <= t.month
left join
accepted_ride_months rides
on t.month = rides.month
group by t.month 
order by t.month 


-- referred to another solution for this one,
-- was using window function and getting weird results on edge cases
-- this joins on <= month to do like a window function & works well!