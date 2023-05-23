--  script that displays the max temperature of each state (ordered by State name).
-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY STATE
ORDER BY STATE ASC;
