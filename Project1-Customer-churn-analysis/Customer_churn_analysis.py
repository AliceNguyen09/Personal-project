import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Data Loading and Exploration
# read the file
df =  pd.read_csv('Customer-Churn-data.csv')
df.head()

# 1.1 Check the dimensions of the dataset
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# 1.2 Check the data types of each column
print(df.dtypes)

# 1.3 Check for missing values
print(df.isnull().sum())

# Done checking

# Step 2: Data Analytics
# 2.1 Analyse the numerical variable

# Prepare the data
X = df[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary', 'Satisfaction Score', 'Point Earned']]  # Explanatory variables
y = df['Exited']  # Dependent variable

# Add a constant term to the explanatory variables
X = sm.add_constant(X)

# Fit the multiple linear regression model
model = sm.Logit(y, X)
results = model.fit()

# Check the regression results
print(results.summary())

# 2.2 Analyse the categorical variable

# Churn distribution
plt.figure(figsize=(6, 6))
churn_counts = df['Exited'].value_counts()
plt.pie(churn_counts, labels=['Retained', 'Churned'], autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Churn Distribution')
plt.show()

# Churn by geography
plt.figure(figsize=(8, 6))
grouped_data = df.groupby(['Geography', 'Exited']).size().unstack()
grouped_data_percent = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100
ax = grouped_data_percent.plot(kind='bar', stacked=True)
plt.title('Churn by Geography')
plt.xlabel('Geography')
plt.ylabel('Percentage')
plt.legend(['Not Exited', 'Exited'])
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=8, color='black')

plt.show()

# Churn by gender
plt.figure(figsize=(8, 6))
grouped_data = df.groupby(['Gender', 'Exited']).size().unstack()
grouped_data_percent = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100
ax = grouped_data_percent.plot(kind='bar', stacked=True)
plt.title('Churn by Gender')
plt.xlabel('Gender')
plt.ylabel('Percentage')
plt.legend(['Not Exited', 'Exited'])
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=8, color='black')

plt.show()

# Churn by age group
plt.figure(figsize=(8, 6))
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 30, 40, 50, 60, np.inf], labels=['<30', '30-40', '40-50', '50-60', '60+'])
grouped_data = df.groupby(['AgeGroup', 'Exited']).size().unstack()
grouped_data_percent = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100
ax = grouped_data_percent.plot(kind='bar', stacked=True)
plt.title('Churn by Age group')
plt.xlabel('Age group')
plt.ylabel('Percentage')
plt.legend(['Not Exited', 'Exited'])
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=8, color='black')

plt.show()

# Churn by credit card
plt.figure(figsize=(8, 6))
grouped_data = df.groupby(['HasCrCard', 'Exited']).size().unstack()
grouped_data_percent = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100
ax = grouped_data_percent.plot(kind='bar', stacked=True)
plt.title('Churn by credit card')
plt.xticks([0,1], ['No', 'Yes'])
plt.xlabel('Having credit card')
plt.ylabel('Percentage')
plt.legend(['Not Exited', 'Exited'])
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=8, color='black')

plt.show()

# Churn by activity status
plt.figure(figsize=(8, 6))
grouped_data = df.groupby(['IsActiveMember', 'Exited']).size().unstack()
grouped_data_percent = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100
ax = grouped_data_percent.plot(kind='bar', stacked=True)
plt.title('Churn by activity status')
plt.xticks([0,1], ['No', 'Yes'])
plt.xlabel('IsActiveMember')
plt.ylabel('Percentage')
plt.legend(['Not Exited', 'Exited'])
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=8, color='black')

plt.show()

# Churn by having complain
plt.figure(figsize=(8, 6))
grouped_data = df.groupby(['Complain', 'Exited']).size().unstack()
grouped_data_percent = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100
ax = grouped_data_percent.plot(kind='bar', stacked=True)
plt.title('Churn by having complain')
plt.xticks([0,1], ['No', 'Yes'])
plt.xlabel('Complain')
plt.ylabel('Percentage')
plt.legend(['Not Exited', 'Exited'])
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=8, color='black')

plt.show()

# Churn by Card Type
plt.figure(figsize=(8, 6))
grouped_data = df.groupby(['Card Type', 'Exited']).size().unstack()
grouped_data_percent = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100
ax = grouped_data_percent.plot(kind='bar', stacked=True)
plt.title('Churn by Card Type')
plt.xlabel('Card Type')
plt.ylabel('Percentage')
plt.legend(['Not Exited', 'Exited'])
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=8, color='black')

plt.show()

# Done script 
