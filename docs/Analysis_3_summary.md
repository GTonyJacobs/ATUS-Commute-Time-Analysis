## Analysis 3 – Commuting Stress and Well-Being – Summary

Having seen in our second analysis the lack of relation between commute time and well-being, we turn from the quantity of work travel to its quality, in particular, how stressful the commuters find it to be. To examine this aspect, we consider the subset of our sample who not only participated in the Well-Being Module of the ATUS, but for whom commuting was among the three randomly selected activities for which they were asked to rate their moods. The sample we obtain in this way is smaller than the previous samples (N=533), but still large enough for meaningful analysis.

For these participants, we focus on the three outcome variables `life_rating`, `gen_health`, and `hyper_tens`, much as in the previous analysis. We have seen the first two of these already, and `hyper_tens` is based on the survey question, "In the last five years, were you ever told by a doctor or other health professional that you have hypertension, also called high blood pressure, or borderline hypertension?"

This time, however, our predictor variable is categorical, based on membership in the following groups:

* Group 1 - Those who did not report feeling stress, either commuting or otherwise (N=138)
* Group 2 - Those who reported commuting stress at a *lower* level than general stress (N=132)
* Group 3 - Those who reported commuting stress at *about the same* level as general stress (N=127)
* Group 4 - Those who reported commuting stress at a *higher* level than general stress (N=136)

Our logistic regression compares Groups 2, 3, and 4 to Group 1, evaluating the extent to which membership in each of the more stressed groups is correlated with increased odds of low life rating, poor general health rating, or hypertension.

In the cases of life rating and general health, we found significant increases for members of the stress groups, which is unsurprising. What is interesting is that this effect was more pronounced for members of Group 4, those for whom commuting was more stressful that the rest of the day. This effect is even more striking when we note that overall stress levels for Group 4 were lower than for Groups 2 and 3.

In the following visualization, we can see the difference between Group 4 and the other groups. While Groups 2 and 3 are twice as likely as Group 1 to report a lower life rating, Group 4 is nearly three times as likely as Group 1 to do so. Similarly, Group 4's odds of reporting poor general health are elevated above the odds for Group 1 even more than they are for Groups 2 and 3.

![Increased odds of negative outcomes due to commuting stress](/images/Increased_odds_of_negative_outcome.png)
