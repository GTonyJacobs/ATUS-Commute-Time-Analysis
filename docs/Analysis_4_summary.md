## Analysis 4 – Commuting and Sleep – Summary

After the previous analyses, we put this study to bed by examining the effects of commuting on sleep. From the ATUS, we have data on how many minutes respondents slept during the 24-hour period of their diary day. We are looking, in this analysis, to see whether there are correlations between sleep time and commuting time, and between sleep time and commuting stress. The sample we use for this analysis is the same one we use in the third analysis.

We carry out a linear regression, with one response variable (`sleep_time`) and two predictor variables (`work_travel` and `commute_stress`). We treat `commute_stress` as a binary variable: 0 = commuting without stress (average stress rating for commuting less than 2), and 1 = commuting with stress (average stress rating for commuting between 2 and 6).

Running our linear regression, we find that most variance in sleep time is due to factors other than those considered here. Sleep time can be affected by nearly anything going on in one's life, including physical and mental health, lifestlye and habits, obligations that arise, family affairs, or just the fact that a good movie is on that night. We find that only about 1.36% of the variance in sleep time is explained by variances in commute time and commute stress.

However, when it comes to explaining that 1.36%, the relationships that are present are quite clear. Commute time is, once again, not the factor that matters; we find no significant correlation between commute time and sleep time. However, those who rated work travel as stressful slept an average of 22.5 minutes less than those who rated it as low-stress.

![Side-by-side boxplots of sleep time for the two groups: those who reported low-stress commutes, and those who reported commuting with stress. There is a visible decrease in sleep time for the group with stressful commutes.](/images/sleep_time_vs_commute_stress_boxplot.png)

It is perhaps surprising that commute time is not a significant factor, considering that time spent traveling to work cannot be spent sleeping. However, we see in the data that those with longer commutes find, on average, the same amount of time to sleep as those with shorter commutes. However, those with stressful commutes are missing out on valuable sleep. The causal relationship here is not necessarily clear: Does the stress of commuting impact sleep, or does a lack of sleep make commutes more stressful? Our result here suggests further questions, which we explore in our final discussion.
