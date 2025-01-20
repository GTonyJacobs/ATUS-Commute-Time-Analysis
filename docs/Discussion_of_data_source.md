# Data Source and Collection

## What Is the ATUS?

The American Time Use Survey has been conducted by the US Bureau of Labor Statistics (BLS) every year since 2003. In it, households are selected from those that have recently completed all eight months of the Current Population Survey (CPS). Households are chosen to reflect a demographic balance of the US population.

From each selected household, one person is chosen for the ATUS to keep a "diary" for one day, noting each activity they perform, and how long they spend doing it. Their responses are coded and stored in a database, providing a rich gallery of snapshots of American life, crossing boundaries of geography, age, sex, occupation, and socio-economic status.

## Why 2021?

In some years, most recently in 2021, the BLS adds a module to the survey called the Well Being Module. This is an additional survey administered to a subset of ATUS participants, in which they are asked, not just about their activities on "diary day", but also about their general health and well being. They are also asked how they felt during certain reported activities, such as driving, relaxing at home, or socializing. For each selected activity, participants rate their feelings of happiness, sadness, fatigue, stress, and sense of meaning.

We chose the 2021 ATUS as our dataset, because the Well Being Module offers additional insights. With this data, we can go beyond learning who commutes and how long they commute. We can begin to explore deeper questions that illuminate the relationship between commuting and other aspects of commuters' lives, such as well-being, health, and happiness.

## Obtaining the Data for Analysis

ATUS data frome each year's survey is publicly available on the Bureau of Labor Statistics' website. Everything we needed for this project can be found on the pages

* [American Time Use Survey—2021 Microdata Files](https://www.bls.gov/tus/data/datafiles-2021.htm), and
* [American Time Use Survey Well-Being Module Microdata Files](https://www.bls.gov/tus/data/wbdatafiles-2021.htm)

On those pages can be found:

* The microdata files themselves. These are zip files, and when extracted, each one yields: a data file (.DAT) which is a standard csv table, a text file (.TXT) containing a brief dictionary of variables used, and three program files (.SAS, .SPS, and .DO) to integrate the data file with various kinds of statistical software.

  The specific microdata files we downloaded for this study are:

  - **Respondent file:** This file contains information about each respondent, including certain demographics and work-force status
  - **Roster file:** This file contains information about each respondent's household, such as the number and ages of the people they live with.
  - **ATUS-CPS file:** This file contains more detailed demographic information about the respondent and their household, pulled from responses to CPS surveys in previous months.
  - **Activity file:** This file is the heart of the ATUS. It contains the contents of each respondent's diary, including start times and stop times for each activity, with the activity type coded in a three-tiered hierarchy.
  - **Well-Being Respondent file:** This file contains responses to general survey questions that were part of the Well-Being Module
  - **Well-Being Activity file:** This file contains data about respondents' reported moods during activities, and is keyed to the main activity file.
  
* Data dictionaries (.PDF): These extremely useful documents detail every variable found in the microdata files, including information about skip patterns on the survey, that is, rules about which questions to skip depending on previous responses. Here we also see descriptions of codes that reflect missing answers and other anomalies.
  
* Coding lexicon (.PDF): The coding lexicon is an essential tool for reading the activity file. It explains the three-tier hierarchy used to code each activity, including examples and notes.
  
* Questionnaires (.PDF): These contain the actual questions asked of the respondents, as well as skip patterns, so we can see the structure of the survey as it was administered.
  
* ATUS User's Guide (.PDF): - This compendious tome tells us all about the ATUS, including its history, sample selection, administration, and many details about all of the files listed above.

## Data Handling and Storage

Having downloaded the microdata files, we uploaded them to a project in BigQuery. There we were able to examine each data set, become familiar with their structures, and run some exploratory queries to see whether we had sufficient data to address our questions.
