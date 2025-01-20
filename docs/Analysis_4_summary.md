## Analysis 4 – Commuting and Sleep – Summary

After the previouis analyses, we put this study to bed with a look at the effects of commuting on sleep. From the ATUS, we have data on how many minutes respondents slept during the 24-hour period of their diary day. We are looking, in this analysis, to see whether there is are correlations between sleep time and commuting time, and between sleep time and commuting stress.

We carry out a linear regression, with one response variable (`sleep_time`) and two predictor variables (`work_travel` and `commute_stress`). We treat `commute_stress` as a binary variable: 0 = commuting without stress (average stress rating for commuting less than 2), and 1 = commuting with stress (average stress rating for commuting 2-6).

Running this analysis, we find that most variance in sleep time is due to factors other than those considered here. Sleep time can be affected by nearly anything going on in one's life, including physical and mental health, lifestlye and habits, obligations that arise, family affairs, or just the fact that a good movie was on that night. We find that only about 1.36% of the variance in sleep time is explained by variances in commuting time and stress.

However, when it comes to explaining that 1.36%, the relationships that are present are quite clear. Commute time is, once again, not the factor that matters, with no significant correlation between commute time and sleep time. However, those who rated work travel as stressful slept an average of 22.5 minutes less than those who rated it as low-stress.

![Side-by-side boxplots of sleep time for the two groups: commute stress=0 and commute stress=1. There is a visible decrease in sleep time for the group with stressful commutes.](/images/sleep_time_vs_commute_stress.png)
