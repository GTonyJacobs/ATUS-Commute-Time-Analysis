import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r'C:\Users\tony\Desktop\Tony\ATUS\sleep_time_analysis.csv')

# Calculate the IQR for sleep_time
Q1 = df['sleep_time'].quantile(0.25)
Q3 = df['sleep_time'].quantile(0.75)
IQR = Q3 - Q1

# Define the outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
df_filtered = df[(df['sleep_time'] >= lower_bound) & (df['sleep_time'] <= upper_bound)]

# Create the boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='commute_stress_bin', y='sleep_time', data=df_filtered)

# Add labels and title
plt.title('Sleep Time vs Commute Stress', fontsize=16)
plt.xlabel('Stressful Commute (0=No, 1=Yes)', fontsize=12)
plt.ylabel('Sleep Time (minutes)', fontsize=12)

# Show the plot
plt.show()
