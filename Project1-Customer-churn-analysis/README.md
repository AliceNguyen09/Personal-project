# Bank Customer Churn Analysis

## Introduction
This project examines the "Bank Customer Churn" dataset in order to assess customer turnover and get insights to help the bank enhance customer retention strategy. Customer churn refers to the situation that customers stop doing business with a organisation or stop using its products or services. To keep consumers and sustain long-term profitability, organisations should understand the factor that cause customers churn.
<br/>
The dataset used in this investigation is the file 'Customer-Churn_data.csv'. The file includes data on bank customers' demographics, credit scores, account balances, tenures, and several other characteristics. The dependant variable is "Exited", which indicates whether a customer has churned (1) or not (0). By exploring the data and performing data analysis, we aim to identify patterns and factors associated with customer churn, thus reduce the churn rate.
<br/><br/>
The projects goes through the following key steps:<br/>
- Data Loading and Exploration: Load the dataset and perform initial exploration to understand its structure, feature types, and any missing values.
- Data Analytics: Conduct an in-depth analysis of the dataset in order to identify the relationships between variables, including visualizations and statistical summaries.
- Insight: Present finding after analysing dataset, including which factors affect customers' churn desicion, and recommemdation on how to reduce churn rate and improve customer retention.
<br/>
The script Customer_churn_analysis.py is used to perform all of these three steps.

## Proccess
### Preparation
A virtual environment is recommended to run the code. The following code will create and active a virtual environment.
```
python3 -m venv .venv
source .venv/bin/activate
```
Then , install pandas, openpyxl, statsmodels, matplotlib and seaborn.
```
pip install pandas openpyxl
pip install statsmodels
pip install matplotlib
```

### Step 1: Data Loading and Exploration
1.1. Check the dimensions of the dataset
```
Number of rows: 10000
Number of columns: 18
```
1.2. Check the data types of each column
```
RowNumber               int64
CustomerId              int64
Surname                object
CreditScore             int64
Geography              object
Gender                 object
Age                     int64
Tenure                  int64
Balance               float64
NumOfProducts           int64
HasCrCard               int64
IsActiveMember          int64
EstimatedSalary       float64
Exited                  int64
Complain                int64
Satisfaction Score      int64
Card Type              object
Point Earned            int64
dtype: object
```
So, we have data of 1000 customers. Among 18 columns, the first three columns, RowNumber, CustomerId and Surname contain random data and do not affect customers' decision to leave the bank. This project will analyse the relationships between other 14 variables and 'Exited' variable.<br/>
Among thses 14 variables, 8 variables are numerical, which are CreditScore, Age, Tenure, Balance, NumOfProduct, EstimatedSalary, Satisfaction Score and Point Earned. The relationships between these variables and the dependant variable will be tested using logistic regression analysis. The other variables, Geography, Gender, HasCrCard, IsActiveMember, Complain, and Card Type, are categorical variables. Churn rates by geography, gender, etc... are calculated to see the trend. Churn rate by age group is also calculated.

1.3. Check for missing values
```
RowNumber             0
CustomerId            0
Surname               0
CreditScore           0
Geography             0
Gender                0
Age                   0
Tenure                0
Balance               0
NumOfProducts         0
HasCrCard             0
IsActiveMember        0
EstimatedSalary       0
Exited                0
Complain              0
Satisfaction Score    0
Card Type             0
Point Earned          0
dtype: int64
```

### Step 2: Data Analytics
2.1. Analyse the numerical variable using logistic regression analysis
```
Logit Regression Results                   
==============================================================================
Dep. Variable:                 Exited   No. Observations:                10000
Model:                          Logit   Df Residuals:                     9991
Method:                           MLE   Df Model:                            8
Date:                Sat, 03 Jun 2023   Pseudo R-squ.:                 0.09007
Time:                        21:07:47   Log-Likelihood:                -4600.9
converged:                       True   LL-Null:                       -5056.3
Covariance Type:            nonrobust   LLR p-value:                2.655e-191
======================================================================================
                         coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------------
const                 -3.7252      0.247    -15.083      0.000      -4.209      -3.241
CreditScore           -0.0008      0.000     -2.820      0.005      -0.001      -0.000
Age                    0.0634      0.002     26.575      0.000       0.059       0.068
Tenure                -0.0102      0.009     -1.136      0.256      -0.028       0.007
Balance             4.942e-06   4.49e-07     11.004      0.000    4.06e-06    5.82e-06
NumOfProducts         -0.0352      0.045     -0.774      0.439      -0.124       0.054
EstimatedSalary     6.581e-07   4.57e-07      1.441      0.150   -2.37e-07    1.55e-06
Satisfaction Score    -0.0128      0.019     -0.687      0.492      -0.049       0.024
Point Earned       -9.794e-05      0.000     -0.844      0.399      -0.000       0.000
======================================================================================
```
For this project, the significance level is chosen as 0.05. Therefore, if then absolute value of z-score is greater than 1.96 and p-value is smaller than 0.05, the null hypothesis is rejected and it is concluded that the variable actually explains the dependant variable.<br/>
From the table above, it can be seen that only CreditScore, Age and Balance have effect on customers' churn decision. However, the coefficien between CreditScore and Exited, and Balance and Exited are too small, so the effect of these two variables on the dependant variable are insignificant and can be ignored.

2.2. Analyse the categorical variable<br/>
Churn distribution:<br/>
![alt text](https://github.com/AliceNguyen09/Personal-project/blob/Project1-Customer-churn-analysis/Project1-Customer-churn-analysis/Churn_distribution.png?raw=true)
<br/><br/>
Churn by geography:<br/>
![alt text](https://github.com/AliceNguyen09/Personal-project/blob/project1-customer-churn-analysis/Customer_churn_analysis/Churn%20geography.png?raw=true)
<br/><br/>
Churn by gender:<br/>
![alt text](https://github.com/AliceNguyen09/Personal-project/blob/project1-customer-churn-analysis/Customer_churn_analysis/Churn%20gender.png?raw=true)
<br/><br/>
Churn by credit card:<br/>
![alt text](https://github.com/AliceNguyen09/Personal-project/blob/project1-customer-churn-analysis/Customer_churn_analysis/Churn%20crcard.png?raw=true)
<br/><br/>
Churn by active status:<br/>
![alt text](https://github.com/AliceNguyen09/Personal-project/blob/project1-customer-churn-analysis/Customer_churn_analysis/Churn%20act%20status.png?raw=true)
<br/><br/>
Churn by having complain:<br/>
![alt text](https://github.com/AliceNguyen09/Personal-project/blob/project1-customer-churn-analysis/Customer_churn_analysis/Churn%20complain.png?raw=true)
<br/><br/>
Chur by card type:<br/>
![alt text](https://github.com/AliceNguyen09/Personal-project/blob/project1-customer-churn-analysis/Customer_churn_analysis/Churn%20card%20type.png?raw=true)
<br/><br/>
Churn by age group:<br/>
![alt text](https://github.com/AliceNguyen09/Personal-project/blob/project1-customer-churn-analysis/Customer_churn_analysis/Churn%20age%20group.png?raw=true)
<br/><br/>
### Insights:
- The clearest indicator of a customer going to churn is that customer having a complaint. Almost customers who have made complaint also churned, while almost customers who have never complained have not churned either.
- Regarding to geography, Germany has the highest churn rate (32.4%), while France and Spain have approximately same churn rate (~16.5%).
- Regrading to gender, the churn rate is higher for female customers (25.1%) compared to male customers (16.5%). This indicates that female customers are more likely to churn.
- Regarding to the age of customer, the logistic regression analysis result indicates that this factor influences the churn decision. The grapth shows that people in the <30 age group and 30-40 age group are unlikely to churn (churn rate is 7.5% and 12.1% respectively), while people in the 50-60 age group have the highest churn rate (56.25%). This implies that older customers are more likely to churn, while younger customers are more likely to stay with the bank.
- Regarding to activity status, active customers appear to have a lower churn rate compared to inactive ones. This suggests that engaged and active customers are more likely to stay with the bank.
- Regarding to card type, it appears that this factor does not have significant affact on churn decision, since the churn rates are all around 20% regardless of the type of card the customers using.
- Having creadit card also does not appear to influence churn rate. The churn rate is ~20% no matter if the customers have credit card or not.
- The other factors including credit score, tenure, balance, estimated salary, point earned appear not to have significant affact on customers churn decision.
<br/>
To sum up, the key indicator of a customer going to quit is that if the customer has made a complaint. Therefore, to sustain long-term relationships with customers, the bank need to act immediately when receiving a complaint. Other factors like gender, geography, age and activity status also have influence on churning decision and need consideration from the bank.
