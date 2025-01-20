import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load the data
df = pd.read_csv(r'C:\Users\tony\Desktop\Tony\ATUS\analysis2_data.csv')

# Variables for logistic regression
predictor = 'work_travel'
outcome = 'happy_bin'

# Filter and scale the data
df = df.dropna(subset=[predictor, outcome])  # Drop rows with missing values
scaler = StandardScaler()
df['scaled_' + predictor] = scaler.fit_transform(df[[predictor]])

# Logistic regression
X = df[['scaled_' + predictor]]
y = df[outcome]
model = LogisticRegression()
model.fit(X, y)

# Predicted probabilities
x_vals = np.linspace(df['scaled_' + predictor].min(), df['scaled_' + predictor].max(), 300).reshape(-1, 1)
y_pred = model.predict_proba(x_vals)[:, 1]

# Plot with confidence interval
plt.figure(figsize=(8, 6))

# Scatter plot with regression line and confidence interval
sns.regplot(x=df[predictor], y=df[outcome], logistic=True, ci=95, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title(f'Logistic Regression for Happy vs Work_Travel', fontsize=14)
plt.xlabel(f'Work Travel (min)', fontsize=12)
plt.ylabel('Probability of High Happiness Rating', fontsize=12)
plt.legend()
plt.show()

