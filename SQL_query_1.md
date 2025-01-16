# SQL Query #1 for ATUS Project

This query extracts data on work-related travel times and combines it with demographic and employment information.

```sql
WITH qual1 AS (
  SELECT resp.TUCASEID AS caseid
  FROM `sandbox-project-418506.ATUS.respondent_file` AS resp
    JOIN `sandbox-project-418506.ATUS.roster_file` AS rost
      ON resp.TUCASEID = rost.TUCASEID
  WHERE rost.TEAGE >= 18 AND rost.TULINENO = 1 AND resp.TRDPFTPT = 1
),

qual2 AS (
  SELECT DISTINCT TUCASEID AS caseid
  FROM `sandbox-project-418506.ATUS.activity_file`
  WHERE TUTIER1CODE = 18 AND TUTIER2CODE = 05
),

qual AS (
  SELECT qual1.caseid AS caseid
  FROM qual1
    JOIN qual2
      ON qual2.caseid = qual1.caseid
),

commute AS (
  SELECT qual.caseid AS caseid, SUM(act.TUACTDUR24) AS work_travel
  FROM qual
    JOIN `sandbox-project-418506.ATUS.activity_file` AS act
      ON act.TUCASEID = qual.caseid
  WHERE (act.TUTIER1CODE = 18 AND act.TUTIER2CODE = 05)
     OR (act.TUTIER1CODE = 18 AND act.TUTIER2CODE = 03 AND act.TUTIER3CODE = 02)
  GROUP BY qual.caseid
)

SELECT
  qual.caseid AS caseid, 
  commute.work_travel AS work_travel, 
  rost.TEAGE AS age, 
  rost.TESEX AS sex,
  resp.TEMJOT AS mult_jobs, 
  resp.TRERNWA AS week_ern,
  cps.HEFAMINC AS year_inc, 
  cps.GTMETSTA AS met_status
FROM qual
  INNER JOIN commute ON commute.caseid = qual.caseid
  INNER JOIN `sandbox-project-418506.ATUS.roster_file` AS rost
    ON rost.TUCASEID = qual.caseid
  INNER JOIN `sandbox-project-418506.ATUS.respondent_file` AS resp
    ON resp.TUCASEID = qual.caseid AND resp.TULINENO = rost.TULINENO
  INNER JOIN `sandbox-project-418506.ATUS.atus_cps` AS cps
    ON cps.TUCASEID = qual.caseid AND cps.TULINENO = rost.TULINENO
ORDER BY qual.caseid;