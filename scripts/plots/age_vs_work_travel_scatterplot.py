import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r'C:\Users\tony\Desktop\Tony\ATUS\age_vs_work_travel.csv')

# Ensure 'age' and 'work_travel' are numeric
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['work_travel'] = pd.to_numeric(df['work_travel'], errors='coerce')

# Set the plot size
plt.figure(figsize=(8, 6))

# Create the scatterplot with regression line
sns.regplot(x='age', y='work_travel', data=df, scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})

# Title and labels
plt.title('Work Travel Time vs. Age', fontsize=14)
plt.xlabel('Age (years)', fontsize=12)
plt.ylabel('Work Travel Time (minutes)', fontsize=12)

# Save the plot as a .png file
plt.savefig(r'C:\Users\tony\Desktop\Tony\ATUS\age_vs_work_travel_scatterplot.png')

# Show the plot
plt.show()
