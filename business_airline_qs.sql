1 "Find total ticket revenue per month yearwise"


SELECT EXTRACT(YEAR FROM p.travel_date::date) AS year,SUM(r.amount)/12 AS total_avg_monthly_revenue  from passengers p
 join revenue_transactions r
on r."PNR"=p.passenger_id
where revenue_type = 'Ticket' 
group by year
order by year

2 "Identify the top 10 routes by total revenue."

WITH route_revenue AS (
    SELECT
        CONCAT(p.origin_airport, '-', p.destination_airport) AS route,
        SUM(r.amount) AS total_revenue,
        DENSE_RANK() OVER (
            ORDER BY SUM(r.amount) DESC
        ) AS rnk
    FROM passengers p
    JOIN revenue_transactions r
        ON r."PNR" = p.passenger_id
    GROUP BY
        CONCAT(p.origin_airport, '-', p.destination_airport)
)

SELECT
    route,
    total_revenue
FROM route_revenue
WHERE rnk <= 10
ORDER BY rnk, total_revenue DESC;

'3 Calculate average ticket price by travel class across each route.'

select origin_airport,destination_airport,
travel_class,round(avg(ticket_price),0) as Average_ticket_price from passengers
group by travel_class, origin_airport,destination_airport
order by round(avg(ticket_price),0) desc

"4 Find flights where baggage revenue exceeds ticket revenue."


"5 Compute revenue split between tickets, meals, and baggage."

SELECT revenue_type,round(SUM(AMOUNT)/(select sum(amount) from revenue_transactions),4)*100 AS Total_revenue_percentage FROM revenue_transactions
GROUP BY revenue_type
order by Total_revenue_percentage desc

"6 Find top 5 airports generating highest ancillary revenue."


SELECT origin_airport, ancilliary_revenue
FROM (
    SELECT
        p.origin_airport,
        SUM(r.amount) AS ancilliary_revenue,
        DENSE_RANK() OVER (ORDER BY SUM(r.amount) DESC) AS rnk
    FROM passengers p
    JOIN revenue_transactions r
        ON p.passenger_id = r."PNR"
    WHERE r.revenue_type <> 'Ticket'
    GROUP BY p.origin_airport
) t
WHERE rnk <= 5
ORDER BY ancilliary_revenue DESC;


"7 Count domestic vs international passengers per year."

select travel_type,EXTRACT(YEAR FROM travel_date::date) as YEAR,count(*) as total_passengers from passengers 
group by travel_type,YEAR
order by YEAR

"8 Identify passengers who traveled more than 5 times in a year.
(here it is considered that passengers with same name are one and the same since no such unique passsenger id is recorded , though not an real life scenario,since PNR is unique and no other passenger_id)"

select passenger_name,EXTRACT(YEAR FROM travel_date::date) as year,count(*) from passengers 
group by passenger_name,year
having count(*)>=5
order by count(*)

"9 Find loyalty tier–wise passenger distribution."

SELECT 
    COALESCE(loyalty_tier, 'None') AS loyalty_tier,
    ROUND(
        COUNT(*) * 100.0 
        / SUM(COUNT(*)) OVER (),
        2
    ) AS loyalty_tier_percentage
FROM passengers
GROUP BY COALESCE(loyalty_tier, 'None')
ORDER BY loyalty_tier_percentage DESC;


10 Calculate average baggage weight per passenger by class.
11 Find top 5 destination countries by passenger volume.
