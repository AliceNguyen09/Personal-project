# UK Interest rate and Housing transactions analysis

## Introduction
This project examines the relationship between interest rate and mortgage, housing transactions and house prices in the UK from 2020 to 2023. The output is visualised using Power BI.

## Input
The project uses data from these following sources:<br/>
Interest rate: Source: Bank of England https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate<br/>
Mortgage data: Source: Bank of England https://www.bankofengland.co.uk/statistics/mortgage-lenders-and-administrators/2024/2024-q1<br/>
Regional house transactions data: Source: HM Land Registry: https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads<br/>
<br/><br/>
House prices in 5 cities Southampton, London, Manchester, Cardiff and York are used to represent UK house price.

## Process
### Preparation
Load data from Excel files into Power BI.
In Power Query Editor: 
Combine yearly house transactions into one table.<br/>
![alt text](https://github.com/AliceNguyen09/Personal-project/blob/Project2-UK-Interest-rate-and-Housing-transactions/Project3-UK-Interest-rate-and-Housing-transactions/pic/1_house%20transactions.png?raw=true)
Format mortgage tables.<br/>
![alt text](https://github.com/AliceNguyen09/Personal-project/blob/Project2-UK-Interest-rate-and-Housing-transactions/Project3-UK-Interest-rate-and-Housing-transactions/pic/2_house%20transactions.png?raw=true)
![alt text](hhttps://github.com/AliceNguyen09/Personal-project/blob/Project2-UK-Interest-rate-and-Housing-transactions/Project3-UK-Interest-rate-and-Housing-transactions/pic/3_mortgage.png?raw=true)
Load tables into Power BI, then create a Date table using DAX by taking the date column from Interest rate table.<br/>

Connect Date table with other tables. Make sure all connections are One to One or Many to One.<br/>

### Data modeling
Create 2 measures to calculate mortgage accounts and mortgage value:<br/>

Create 7 measures to calculate number of housing transactions and housing transaction value in the UK and in each cities. <br/>

Group the measures together.<br/>

Create 2 parameters, one for mortgage data and one for housing transactions data.<br/>


### Visualisation
There are 2 pages in the report: Interest rate and Mortgage, and Housing Transactions and Prices.<br/>
Interest rate and Mortgage page:<br/>
The Line chart and Column chart use the parameters for its y-axis, therefore user can switch between Mortgage accounts and Mortgage value, and Housing price and Housing transaction to see the correlation between Interest rate and those variables.<br/>
![alt text](https://github.com/AliceNguyen09/Personal-project/blob/Project2-UK-Interest-rate-and-Housing-transactions/Project3-UK-Interest-rate-and-Housing-transactions/pic/1_gif.gif?raw=true)

Housing Transactions and Prices page:<br/>
The dynamic value is used to show the corresponding city name in the card when user choose different city.<br/>

The Housing transactions by City pie chart is not impacted by the City slicer by setting the 'Edit interactions' for the slicer.<br/>

Users have the option to switch the line and column chart to see housing transaction data or housing price data by clicking the button. This feature is built by using bookmark.<br/>
Gif


### Output
Gif

### Insights
- The UK interest rate began rising sharply from February 2022. Initially, the rate was 0.1% before December 2021, increased to 0.25% in December 2021 and January 2022, and then increased significantly. By December 2023, the interest rate had reached 5.25%.
- The number of mortgage accounts also increased, starting from February 2023. There were 2,860 mortgage accounts in 2022, which grew to 4,615 in 2023—a 61.6% increase. This suggests that the total number of mortgage accounts lags behind interest rate changes, as people may rush to secure a mortgage before rates climb even higher.
- However, there appears to be no significant correlation between interest rates and mortgage value, housing transactions, or house prices. During the observed period, total mortgage value and housing transactions remained relatively stable.
- The average house price began to decline in the latter half of 2023, dropping from £690,031 in June to £582,065 by December.
- London accounted for 60% of all housing transactions and remains the most expensive region, with house prices 136% higher than the UK average.

