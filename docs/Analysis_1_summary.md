## Analysis 1 – Socioeconomic Factors and Commute Time – Summary

This analysis is a linear regression: We test whether the predictor variables:

* `age`
* `week_ern` – weekly earnings
* `year_inc` – yearly household income
* `mult_jobs` – having multiple jobs

predict anything about the outcome variable, `work_travel`, which is the total time a respondent spent in "travel related to work" on their diary day.

Now, we know that both work travel and some of the socioeconomic factors differ across demographics. Therefore, in order to see the effects of the predictor variables without confounding effects, we divided our sample up into groups, separating women from men, and metropolitan residents from non-metropolitan residents.

We then ran the same analysis nine times, for different subsets of the sample. In this way, we tested whether the predictors influenced the outcome differently for different demographic groups.

The nine subsets were:

1. Entire sample
2. Men
3. Women
4. Metropolitan residents
5. Non-metropolitan residents
6. Metropolitan men
7. Metropolitan women
8. Non-metropolitan men
9. Non-metropolitan women

Overall, we found that the socioeconomic factors we tested had little influence on variation in commute time, with a couple of notable exceptions in certain groups:

* **Among non-metropolitan women, higher age is correlated with less work travel.** On average, work travel in this group decreases by about one minute for each additional two years of age.

  ![Scatterplot_of_age_v_work_travel](/images/scatterplot.png)
  
* **Among residents of metropolitan areas, having multiple jobs is correlated with slightly more work travel**, with multiple-job workers traveling an average of 7.5 minutes longer than single-job workers.
