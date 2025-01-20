# Data Cleaning and Preparation

## Missing Values

Certain instances of missing values were handled at the query level. For instance, in the second and third queries, we looked at reported moods. Respondents reported their levels of happiness, sadness, etc., on a 7-point Likert scale that was coded with the numbers 0 through 6. In some cases, there was a negative value in the data, which indicated a missing response. The above queries were written in a way to exclude those numbers when calculating averages.

Next, looking at the results of the first query in our spreadsheet, we noted anomalies with two of the variables.

First, there were missing values in the weekly earnings data. Of the N=1574 records in the sample, 128 had no response for this variable. We checked whether the exclusion of those results changed the summary statistics for any of the other variables, and there were no significant changes. We also looked at the occupatoinal codes of those not reporting weekly income, to see whether there were any patterns there. We saw that the response was omitted for a variety of reasons, ranging from volunteer work, to "gig" work, to self-employed respondents whose pay simply doesn't come on a regular enough basis to report a weekly average. Based on the fairly small number of affected records (≈8%) and the lack of strong systematic bias, we chose to exclude these records from the analysis, bringing our sample size down to N=1446.

Next there was a minor issue with the metropolitan status data. Of the remaining N=1446 records in the data, 13 had their metropolitan status listed as neither metropolitan nor non-metropolitan, but "other". We noted these as anomalous, but in doing the overall regression and the regressions stratified by sex, we left them in. They were, of course, excluded in the regressions that included metropolitan versus non-metropolitan in the stratification. Thus, the totals for the different stratified subsets in the first analysis don't always add up to N, but since the discrepancy is less than 1% of the total sample, we treat it as negligible.

## Ordinal Variables

In the first analysis, one of our predictor variables was family income, which was reported in the data in a coded manner, with numbers 1-16 representing income brackets. Since the brackets were not of equal width, it would be misleading to use these numbers in a linear regression, so we replaced each number 1-15 with the midpoint of its respective bracket. The final bracket, representing an annual family income "over `$150,000`" had no midpoint, so we looked at US Census Bureau data on US household incomes. Based on their numbers, the median for household incomes over `$150,000` is about `$225,000`, so we assigned bracket 16 to that number.

In our second analysis, all outcome variables were either ordinal, or based on ordinal variables:

* Life rating was given on a scale of 0 (bad) to 10 (good)
* General health was given on a scale of 1 (poor) to 5 (excellent)
* Happiness, Sadness, and Stress were all averaged from 1 to 3 observations each, with each observation being given on a scale of 0 (not feeling it) to 6 (feeling it strongly)

Since all of these data were reported on Likert scales, on which the numbers represent a real order, but not real measurements or quantities, we mostly opted to rework them as binary variables, that is, 0 or 1.

* Life rating values were distributed in such a way that about half of respondents reported 0-7, and half reported 8-10. We assigned all responses 0-7 to the value 0 (lower life rating), and all responses 8-10 to the value 1 (high life rating).
* General health values were distributed with roughly half reporting ratings 1-3, and about half reporting 4 or 5. As with life rating, we assigned values 1-3 to the value 0 (poorer general health), and 4 and 5 to the value 1 (better general health).
* Happiness averages were distributed with a median of about 4.3. We chose to assign happiness averages below 4 to the value 0 (moderatly happy at best), and averages of 4 or more to the value 1 (quite happy).
* Sadness averages, by contrast, had a very skewed distribution, with 2/3 of the respondents reporting no sadness at all during their selected activities. Therefore, we kept the average 0 at 0 (no sadness), and assigned any average above 0 to the value 1 (some sadness).
* Stress averages were not as skewed as sadness averages, but still highly imbalanced, with a great many participants reporting no stress, or very little stress. We assigned any average stress ratings less than 2 to the value 0 (very little stress), and any averages 2 or above to the value 1 (moderate or high stress)
