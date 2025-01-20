## Analysis 2 – Commute Time and Well-Being – Summary

In this analysis, we use work travel time (`work_travel`) as our predictor variable, and we look at its possible influence on a variety of well-being related variables:

* `life_rating` – responses to a survey question about overall life rating
* `gen_health` – respondents' self-reporting of their general health status
* `happy` – weighted average of responses when respondents were asked how happy they felt during three randomly selected activities on their diary day
* `sad` – same as `happy`, but for sadness
* `stress` – same as `happy` and `sad`, but for stress level

For details about how the weighted averages work, please see our discussion of the second sample in [Data Extraction](/docs/Discussion_of_queries.md).

All of our outcome variables are ordinal, rather than continuous interval variables. "Points on a rating scale" are not measured values in the way that "minutes of travel" are. Thus, it does not make sense to use linear regression; instead we use logistic regression, a statistical tool that works well with binary variables. In order to do this, make out outcome variables binary by "dichotomizing" them. For details about how we handled this task, please see [Data Cleaning and Preparation](/docs/Preparation_and_cleaning.md).

Carrying out the logistic regressions, we find that in each case, `work_travel` has no significant correlation with these measures of well-being. Here, we can see plots of three of the regressions, including best-fit curves and 95% confidence intervals. Note that, within the 95% confidence intervals (the pink regions) it's impossible to say whether the best-fit line is really increasing or decreasing. It's not clear whether greater work travel corresponds with higher or lower general health, more or less happiness, more or less stress:

<p align="center">
  <img src="/images/gen_health_vs_work_travel.png" width="30%" />
  <img src="/images/happy_vs_work_travel.png" width="30%" />
  <img src="/images/stress_vs_work_travel.png" width="30%" />
</p>

The significance of this analysis is, interestingly, its lack of significant results. Hearing people complain about extended commutes, anecdotally, we might expect long commute times to predict all sorts of negative effects in terms of well-being. We learn instead, that we need to look at factors other than commute time if we want to have any power to predict whether someone rates their life or health as good or bad, or whether they're more likely to feel happy, or sad, or stressed.
