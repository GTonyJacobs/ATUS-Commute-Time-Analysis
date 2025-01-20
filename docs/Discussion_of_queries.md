# Data Preparation

Our first step was to filter the large ATUS datasets for the purposes of considering our questions. We chose to only look at data from adults (18+), with full time jobs, who reported commuting ("Travel related to work") on their diary days. We ended up using three different samples from this group, due to the nature of information needed for each analysis.

In the following sections, we discuss how each sample was selected, based on the presence of needed data.

## First Sample

To investigate **Socioeconomic Factors and Commute Time**, we were able to look at nearly all respondents from our filtered dataset, because data for age, multiple jobs, income level, sex, and metropolitan status was available for every respondent. Of course, within our filtered group, every respondent had a non-zero commute time.

We obtained this sample using the following SQL query, run in BigQuery. In this query, we first filter for commuting adults with full-time jobs, then calculate total commute time, and then select the sample for export and analysis. We obtained a sample of N=1574 respondents. After uploading the sample to a spreadsheet, we performed additional minor filtering for anomalies, which we discuss in our data cleaning document.

* [Query #1](/../scripts/SQL_query_1.md)

## Second sample

To investigate **Commute Time and Well-Being** we restricted our attention to respondents who had been administered the Well-Being Module of the survey. On this module, respondents reported a life rating, a general health rating, and their moods during three randomly selected activities. We will say more about the reporting and coding of these questions when we talk about data cleaning and analysis below.

The following SQL query does the same filtering as the previous one, and also calculates average reported moods during each respondent's three selected activities. The averages are weighted according to the duration of each activity. Thus, for example, an hour-long activity at happiness level 6 influences the average than a 10-minute activity at happiness level 2.

With this query, we initially obtained a sample of N=1228 respondents.

* [Query #2](/../scripts/SQL_query_2.md)

## Third Sample

For both **Commuting Stress and Well-Being** and **Commuting and Sleep**, we used a variable determined by stress *reported during the activity of traveling to work*. Since those participating in the Well-Being Module were asked about their moods during three randomly selected activities, only a subset of them were asked about their moods while they were commuting. This subset forms our third sample.

In the following query, we begin by performing the same filtering and calculations as in the previous queries. Then, we calculate total sleep time, and obtain the average stress level reported during communting activities, for those who were asked.

Working with this more restricted subset yielded a smaller sample, of N=533 respondents.

* [Query #3](/../scripts/SQL_query_3.md)
