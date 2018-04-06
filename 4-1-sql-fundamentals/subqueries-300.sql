## 2. Subqueries ##

SELECT Major, Unemployment_rate
FROM recent_grads
WHERE Unemployment_rate < (SELECT AVG(Unemployment_rate) FROM recent_grads)
ORDER BY Unemployment_rate

## 3. Subquery In SELECT ##

SELECT CAST(COUNT(*) AS Float)  / CAST((SELECT COUNT(*) FROM recent_grads) AS FLOAT) AS proportion_abv_avg
FROM recent_grads
WHERE ShareWomen > (SELECT AVG(ShareWomen) FROM recent_grads)

## 4. Returning Multiple Results In Subqueries ##

SELECT Major, Major_category FROM recent_grads
WHERE Major_category IN (select Major_category from recent_grads
group by Major_category
order by SUM(Total) DESC
limit 5)

## 5. Building Complex Subqueries ##

SELECT AVG(CAST(Sample_size AS Float) / CAST(Total AS Float)) AS avg_ratio
FROM recent_grads

## 6. Practice Integrating A Subquery With The Outer Query ##

SELECT Major, Major_category, (CAST(Sample_size as Float) / CAST(Total as Float)) AS ratio
FROM recent_grads
WHERE ratio > (SELECT AVG(CAST(Sample_size AS Float) / CAST(Total AS Float)) AS avg_ratio
FROM recent_grads)
