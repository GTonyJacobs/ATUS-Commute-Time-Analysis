# SQL Query #3 for ATUS Project

This query extracts data on work-related travel stress for ATUS participants who took part in the Well-Being Module and reported on their mood during work travel.

```sql
WITH qual1 AS (
  SELECT resp.TUCASEID AS caseid
  FROM `atus-travel-data-analysis.ATUS_tables.respondent_file` AS resp
    JOIN `atus-travel-data-analysis.ATUS_tables.roster_file` AS rost
      ON resp.TUCASEID=rost.TUCASEID
  WHERE rost.TEAGE>=18 AND rost.TULINENO=1 AND resp.TRDPFTPT=1
),

qual2 AS (
  SELECT DISTINCT TUCASEID AS caseid
  FROM `atus-travel-data-analysis.ATUS_tables.activity_file`
  WHERE TUTIER1CODE=18 AND TUTIER2CODE=05
),

qual AS (
  SELECT
    qual1.caseid AS caseid
  FROM qual1
    JOIN qual2
      ON qual2.caseid=qual1.caseid
),

stress_avg AS (
  SELECT 
    main_act.TUCASEID,
    ROUND(
      SUM(wb_act.WUSTRESS * main_act.TUACTDUR24) / NULLIF(SUM(main_act.TUACTDUR24), 0), 3
    ) AS stress_avg
  FROM qual
    JOIN `atus-travel-data-analysis.ATUS_tables.activity_file` AS main_act
      ON main_act.TUCASEID = qual.caseid
    JOIN `atus-travel-data-analysis.ATUS_tables.wb_activity` AS wb_act
      ON wb_act.TUCASEID = qual.caseid
      AND wb_act.TUACTIVITY_N = main_act.TUACTIVITY_N
  WHERE wb_act.WUSTRESS >= 0
  GROUP BY main_act.TUCASEID
),

commute AS(
  SELECT
    qual.caseid AS caseid, SUM(act.TUACTDUR24) AS work_travel
  FROM qual
    JOIN `atus-travel-data-analysis.ATUS_tables.activity_file` AS act
      ON act.TUCASEID=qual.caseid
  WHERE
    (act.TUTIER1CODE=18 AND act.TUTIER2CODE=05) 
  GROUP BY qual.caseid
),

sleep AS (
  SELECT
    qual.caseid AS caseid,
    COALESCE(SUM(CASE WHEN act.TUTIER1CODE=01 AND act.TUTIER2CODE=01 THEN act.TUACTDUR24 END), 0) AS sleep_time
  FROM qual
  LEFT JOIN `atus-travel-data-analysis.ATUS_tables.activity_file` AS act
    ON act.TUCASEID = qual.caseid
  GROUP BY qual.caseid
),

subset AS (
  SELECT
    qual.caseid AS caseid, AVG(wb_act.WUSTRESS) AS stress
  FROM qual
    JOIN `atus-travel-data-analysis.ATUS_tables.activity_file` AS act
      ON act.TUCASEID=qual.caseid
    JOIN `atus-travel-data-analysis.ATUS_tables.wb_activity` AS wb_act
      ON wb_act.TUCASEID=qual.caseid AND wb_act.TUACTIVITY_N=act.TUACTIVITY_N
  WHERE (act.TRCODE=180301 OR TRCODE=180302 OR TRCODE=180501) AND wb_act.WUSTRESS>=0
  GROUP BY qual.caseid
)

SELECT
  qual.caseid, commute.work_travel,
  sleep.sleep_time AS sleep_time,
  wbresp.WECANTRIL AS life_rating,
  wbresp.WEGENHTH AS gen_health,
  wbresp.WEHBP AS hyper_tens,
  stress_avg.stress_avg AS stress,
  subset.stress AS car_stress
FROM qual
  JOIN commute
    ON commute.caseid=qual.caseid
  JOIN sleep
    ON sleep.caseid=qual.caseid
  JOIN `atus-travel-data-analysis.ATUS_tables.wb_resp` AS wbresp
    ON wbresp.TUCASEID=qual.caseid
  JOIN stress_avg
    ON stress_avg.TUCASEID = qual.caseid
  JOIN subset
    ON subset.caseid=qual.caseid
  ORDER BY qual.caseid