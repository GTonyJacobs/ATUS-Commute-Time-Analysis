## Analysis 2 – Commute Time and Well-Being – Summary

In this analysis, we use work travel time (`work_travel`) as our predictor variable, and we look at its possible influence on a variety of well-being related variables:

* `life_rating` – responses to a survey question about overall life rating
* `gen_health` – respondents' self-reporting of their general health status
* `happy` – weighted average of responses when respondents were asked how happy they felt during three randomly selected activities on their diary day
* `sad` – same as `happy`, but for sadness
* `stress` – same as `happy` and `sad`, but for stress level

For details about how the weighted averages work, please see above, under "Data Preparation: Second Sample"

All of ohat our outcome variables are ordinal, rather than continuous interval vari.tool. "Points on a rating scale" are not measured values in the way that "minutes of travel" Thus, it does not make sense to use linear regression, so instead we use logistic regression, a statistical tool that works well with binary variables. In order to do this, ore, we mare out outcome variables binary by "dichotomizing" tFor details about how we handled these variables, please see above, under "Data Cleaning: Ordinal Variables".

Carrying out the logistic regressions, we find that in each case, `work_travel` has no significant correlation with these measures of well-being.

The significance of this analysis is, interestingly, its lack of significant results. We learn that, if we want to predict whether someone rates their life or health as good or bad, whether they're more likely to feel happy, or sad, or stressed, then simply looking at how long they travel to work gives us no useful information.hem. 
