import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv(r'C:\Users\tony\Desktop\Tony\ATUS\mult_jobs_vs_work_travel.csv')

# Convert 'mult_jobs' to a categorical variable if needed
df['mult_jobs'] = df['mult_jobs'].astype('category')

# Ensure 'work_travel' is numeric
df['work_travel'] = pd.to_numeric(df['work_travel'], errors='coerce')

# Calculate Q1 (25th percentile) and Q3 (75th percentile) for 'work_travel'
Q1 = df['work_travel'].quantile(0.25)
Q3 = df['work_travel'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers from the data
df_filtered = df[(df['work_travel'] >= lower_bound) & (df['work_travel'] <= upper_bound)]

# Set the plot size
plt.figure(figsize=(8, 6))

# Create the boxplot with the filtered data
sns.boxplot(x='mult_jobs', y='work_travel', data=df_filtered)

# Title and labels
plt.title('Work Travel Time by Multiple Job Status', fontsize=14)
plt.xlabel('Multiple Job Status (0 = No, 1 = Yes)', fontsize=12)
plt.ylabel('Work Travel Time (minutes)', fontsize=12)

# Save the plot as a .png file
plt.savefig(r'C:\Users\tony\Desktop\Tony\ATUS\work_travel_boxplot.png')

# Show the plot
plt.show()
