## Analysis 1 – Socioeconomic Factors and Commute Time – Summary

This analysis is a multilinear regression. We consider the following predictor variables:

* `age` – in years
* `week_ern` – weekly earnings
* `year_inc` – yearly household income
* `mult_jobs` – having multiple jobs

Our regression tests whether any of these predictors are correlated with the outcome variable, `work_travel`, which is the total time a respondent spent in "travel related to work" on their diary day.

We know at the outset that both work travel and some of the socioeconomic factors differ across demographics. Therefore, in order to see the effects of the predictor variables without confounding effects, we divide our sample into groups, separating men from women, and metropolitan residents from non-metropolitan residents.

We then run the same analysis nine times, for different subsets of the sample. In this way, we test whether the predictors influence the outcome differently for different demographic groups.

The nine subsets are:

1. Entire sample
2. Men
3. Women
4. Metropolitan residents
5. Non-metropolitan residents
6. Metropolitan men
7. Metropolitan women
8. Non-metropolitan men
9. Non-metropolitan women

Overall, we find that the socioeconomic factors we tested have little influence on variation in commute time, with two notable exceptions in certain groups:

* **Among non-metropolitan women, higher age is correlated with less work travel.** On average, work travel in this group decreases by about one minute for each additional two years of age.

  ![Scatterplot_of_age_v_work_travel](/images/age_vs_work_travel_scatterplot.png)
  
* **Among residents of metropolitan areas, having multiple jobs is correlated with slightly more work travel**, with multiple-job workers traveling an average of 7.5 minutes longer than single-job workers.
  
  ![Boxplots of work travel by multiple job status for metropolitan residents](/images/mult_jobs_vs_work_travel_boxplot.png)
