## Analysis 4 – Commuting and Sleep – Summary

After the previouis analyses, we put this study to bed with a look at the effects of commuting on sleep. From the ATUS, we have data on how many minutes respondents slept during the 24-hour period of their diary day. We are looking, in this analysis, to see whether there is are correlations between sleep time and commuting time, and between sleep time and commuting stress.

We carry out a linear regression, with one response variable (`sleep_time`) and two predictor variables (`work_travel` and `car_stress`). We treat `car_stress` as a binary variable: commuting without stress (average stress rating less than 2) versus commuting with stress (average stress rating 2-6).

Running this analysis, we find that most variance in sleep time is due to factors other than those considered here. Sleep time can be affected by nearly anything going on in one's life, including physical and mental health, lifestlye and habits, obligations that arise, family affairs, or just the fact that a good movie was on that night. We find that only about 1.5% of the variance in sleep time is explained by commuting time and stress.

However, when it comes to explaining that 1.5%, there are clear, significant correlations of both predictor variables with sleep time. Indeed, for 5 minutes of increase in work travel time, we see that the average amount of sleep decreases by 1 minute. Furthermore, those who rated work travel as stressful slept an average of 21 minutes less than those whose did not rate work travel as stressful.
