# Store sales analysis

## Introduction
This project works with store sales data from [**Kaggle**](https://www.kaggle.com/code/allunia/e-commerce-sales-forecast/notebook).<br/>
The dataset includes 2 tables: sales and customers.

## Load data into SQL
Firstly, I create a new Sales schema. Then I create 2 tables, sales and customers, with same format with the data in the csv files.<br/>
Then I load data from the 2 csv files into two tables.
```
CREATE SCHEMA Sales;
USE Sales;

CREATE TABLE sales (
    InvoiceNo INT NOT NULL,
    StockCode VARCHAR(100) NOT NULL,
    Description VARCHAR(250),
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice DECIMAL(10,2),
    CustomerID INT,
    Country VARCHAR(100)
    );

CREATE TABLE customers (
    CustomerID INT PRIMARY KEY,
    Gender VARCHAR(100),
    Age VARCHAR(100)
    );


LOAD DATA INFILE '/Users/Documents/GitHub/Personal-project/Project4-Sales-analysis/sales.csv'
INTO TABLE sales
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/Documents/GitHub/Personal-project/Project4-Sales-analysis/customers.csv'
INTO TABLE customers
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```
Table 'sales' has 8 columns and 405874 rows.
* InvoiceNo: Invoice number of the purchase
* StockCode: Stock code of production in the purchase
* Description: Description of production in the purchase
* Quantity: Quantity of production in the purchase
* InvoiceDate: Date & time of the purchase
* UnitPrice: Unit price of production
* CustomerID: Customer ID
* Country: Country where the purchase was done
<br/>
This table does not have a primary key column
<br/>
Table 'customers' has 3 columns and 4372 rows.<br/>
* CustomerID: Customer ID. This is the primary key of this table
* Age: Age group of each customer
* Gender: Male of Female

## Analysis
### 1. 20 items being sold the most
```
SELECT COUNT(*) AS 'No. of items sold',
StockCode, Description FROM sales
GROUP BY StockCode, Description
ORDER BY 1 DESC
LIMIT 20 OFFSET 0;
```
The script counts the total number of rows in the sales table, since each row represents 1 item sold, then group by Stock code & description.
Result:
| No. of items sold | StockCode | Description |
|----------|----------|----------|
|2067| 85123A| WHITE HANGING HEART T-LIGHT HOLDER|
|1900| 22423| REGENCY CAKESTAND 3 TIER|
|1657| 85099B| JUMBO BAG RED RETROSPOT|
|1416| 84879| ASSORTED COLOUR BIRD ORNAMENT|
|1413| 47566| PARTY BUNTING|
|1353| 20725| LUNCH BAG RED RETROSPOT|
|1232| 22720| SET OF 3 CAKE TINS PANTRY DESIGN|
|1194| POST| POSTAGE|
|1124| 20727| LUNCH BAG  BLACK SKULL|
|1078| 21212| PACK OF 72 RETROSPOT CAKE CASES|
|1029| 23298| SPOTTY BUNTING|
|1028| 22086| PAPER CHAIN KIT 50'S CHRISTMAS| 
|1021| 22382| LUNCH BAG SPACEBOY DESIGN|
|1011| 20728| LUNCH BAG CARS BLUE|
|996| 22457| NATURAL SLATE HEART CHALKBOARD|
|995| 22469| HEART OF WICKER SMALL|
|975| 22384| LUNCH BAG PINK POLKADOT|
|973| 22960| JAM MAKING SET WITH JARS|
|955| 21034| REX CASH+CARRY JUMBO SHOPPER|
|948| 22383| LUNCH BAG SUKI DESIGN|

<br/>

### 2. Average invoice value
```
SELECT ROUND(SUM(Quantity*UnitPrice) / COUNT(DISTINCT InvoiceNo), 2) AS AverageInvoiceValue
FROM sales;
```
The script calculates the total sales (Quantity*UnitPrice) then divides by the total number of invoices.
Result:
| AverageInvoiceValue |
|----------|
|373.34|

<br/>

### 3. Revenue by countries
```
SELECT ROUND(SUM(Quantity*UnitPrice),2) AS Revenue,
Country
FROM sales
GROUP BY Country
ORDER BY Revenue DESC;
```
The script returns revenue by contries in descending order.
Result:
| Revenue | Country |
|----------|----------|
|6753012.41	| United Kingdom|
|284661.54	| Netherlands|
|250168.47	| EIRE|
|220664.86	| Germany|
|195851.66	| France|
|137077.27	| Australia|
|55739.40	| Switzerland|
|54774.58	| Spain|
|40910.96	| Belgium|
|36595.91	| Sweden|
|35340.62	| Japan|
|35163.46	| Norway|
|28073.38	| Portugal|
|22326.74	| Finland|
|19881.14	| Channel Islands|
|18768.14	| Denmark|
|16890.51	| Italy|
|12946.29	| Cyprus|
|10154.32	| Austria|
|9120.39	| Singapore|
|7213.14	| Poland|
|6994.25	| Israel|
|4710.52	| Greece|
|4310.00	| Iceland|
|3666.38	| Canada|
|2232.76	| Malta|
|1902.28	| United Arab Emirates|
|1730.92	| USA|
|1693.88	| Lebanon|
|1661.06	| Lithuania|
|1291.75	| European Community|
|1143.60	| Brazil|
|1002.31	| RSA|
|707.72	| Czech Republic|
|548.40	| Bahrain|
|131.17	| Saudi Arabia|
|14.85	| France|

### 4. The item sold the most in each country
```
WITH CountrySales AS (
    SELECT 
        COUNT(*) AS 'No. of items sold',
        Description,
        Country
    FROM sales
    GROUP BY Description, Country
),
MaxSales AS (
    SELECT 
        Country,
        MAX(`No. of items sold`) AS MaxItems
    FROM CountrySales
    GROUP BY Country
)
SELECT 
    cs.Country,
    cs.Description,
    cs.`No. of items sold`
FROM CountrySales cs
JOIN MaxSales ms
    ON cs.Country = ms.Country AND cs.`No. of items sold` = ms.MaxItems
ORDER BY cs.Country;
```
The script uses WITH clause to create 2 CTE (Common Table Expression). 
The CountrySales table calculates the total items sold per Desciption in each country. 
The MaxSales tables finds the maximum number of items sold in each country. 
The JOIN of these 2 tables returns the Total items sold and Description of the item sold the most in each country. 
Result:
| Country | Description | No. of items sold |
|----------|----------|----------|
|Australia | SET OF 3 CAKE TINS PANTRY DESIGN | 10|
|Austria | POSTAGE | 14|
|Bahrain | NOVELTY BISCUITS CAKE STAND 3 TIER | 2|
|Belgium | POSTAGE | 98|
|Brazil | RECYCLED ACAPULCO MAT TURQUOISE | 1|
|Canada | COLOURING PENCILS BROWN TUBE | 3|
|Channel Islands | DOORMAT HOME SWEET HOME BLUE | 7|
|Cyprus | REGENCY CAKESTAND 3 TIER | 8|
|Czech Republic | PINK METAL CHICKEN HEART | 3|
|Denmark | POSTAGE | 14|
|EIRE | CARRIAGE | 99|
|France | BAKING SET 9 PIECE RETROSPOT | 1|
|Germany | POSTAGE | 383|
|Greece | POSTAGE | 4|
|Iceland | AIRLINE BAG VINTAGE JET SET BROWN | 6|
|Israel | SPACEBOY LUNCH BOX | 3|
|Italy | POSTAGE | 18|
|Japan | RED SPOTTY BISCUIT TIN | 7|
|Malta | FAMILY PHOTO FRAME CORNICE | 5|
|Netherlands | POSTAGE | 39|
|Norway | POSTAGE | 20|
|Poland | LARGE CHINESE STYLE SCISSOR | 7|
|Poland | RECIPE BOX PANTRY YELLOW DESIGN | 7|
|Portugal | POSTAGE | 29|
|Saudi Arabia | GLASS JAR DAISY FRESH COTTON WOOL | 2|
|Singapore | Manual | 14|
|Spain | POSTAGE | 62|
|Sweden | POSTAGE | 24|
|Switzerland | POSTAGE | 33|
|United Kingdom | WHITE HANGING HEART T-LIGHT HOLDER | 1978|
|USA | TEA PARTY BIRTHDAY CARD | 4|

### 5. The day with highest revenue in each country
```
WITH DailyRevenue AS (
    SELECT 
        DATE(InvoiceDate) AS RevenueDate,
        Country,
        SUM(Quantity * UnitPrice) AS TotalRevenue
    FROM sales
    GROUP BY RevenueDate, Country
),
MaxRevenue AS (
    SELECT 
        Country,
        MAX(TotalRevenue) AS MaxRevenue
    FROM DailyRevenue
    GROUP BY Country
)
SELECT 
    dr.Country,
    dr.RevenueDate,
    dr.TotalRevenue
FROM DailyRevenue dr
JOIN MaxRevenue mr
    ON dr.Country = mr.Country AND dr.TotalRevenue = mr.MaxRevenue
ORDER BY dr.Country;
```
The logic is similar with finding The item sold the most in each country.
2 CTE, DailyRevenue and MaxRevenue, are joined to return the day with highest revenue for each country.
Result:
| Country | RevenueDate | TotalRevenue |
|----------|----------|----------|
|Australia | 2011-06-15 | 23426.81|
|Austria | 2011-03-23 | 1542.08|
|Bahrain | 2011-05-09 | 459.40|
|Belgium | 2011-11-04 | 1673.03|
|Brazil | 2011-04-15 | 1143.60|
|Canada | 2011-07-11 | 1217.64|
|Channel Islands | 2011-08-23 | 2705.22|
|Cyprus | 2011-10-13 | 2876.85|
|Czech Republic | 2011-02-28 | 549.26|
|Denmark | 2011-03-17 | 3978.99|
|EIRE | 2011-01-14 | 16774.72|
|Finland | 2011-03-01 | 4969.22|
|France | 2011-10-28 | 8990.46|
|Germany | 2011-05-12 | 12165.25|
|Greece | 2011-01-24 | 2661.24|
|Iceland | 2011-10-31 | 1294.32|
|Israel | 2011-08-18 | 4873.81|
|Italy | 2011-11-21 | 1757.55|
|Japan | 2011-02-09 | 5735.24|
|Lebanon | 2011-01-27 | 1693.88|
|Lithuania | 2010-12-05 | 1598.06|
|Malta | 2011-08-15 | 905.50|
|Netherlands | 2011-10-20, 25833.56|
|Norway | 2011-09-19 | 4366.78|
|Poland | 2011-05-25 | 1367.57|
|Portugal | 2011-01-18 | 2271.62|
|RSA | 2011-10-13 | 1002.31|
Saudi Arabia | 2011-02-24 | 145.92|
|Singapore | 2011-07-18 | 3949.32|
|Spain | 2011-01-11 | 4564.30|
|Sweden | 2011-10-17 | 5296.96|
|Switzerland | 2011-11-06, 6207.67|
|United Arab Emirates | 2011-09-01 | 975.54|
|United Kingdom | 2011-09-20 | 100460.38|
|USA | 2011-10-10 | 1579.51|

### 6. Customer with highest invoice value
```
SELECT SUM(Quantity * UnitPrice) AS InvoiceValue,
s.CustomerID,
Gender,
Age
FROM sales s
JOIN customers c ON s.CustomerID = c.CustomerID
GROUP BY s.CustomerID
ORDER BY TotalRevenue DESC
LIMIT 1 OFFSET 0;
```
The script calculates each invoice value, maps with customer ID and returns only row with highest invoice value.
Result:
|InvoiceValue | CustomerID | Gender | Age |
|----------|----------|----------|----------|
|279489.02 | 14646 | M | 26-35 |


### 7. Revenue by age groups
```
SELECT SUM(Quantity*UnitPrice) AS Revenue,
Age
FROM sales s
JOIN customers c ON s.CustomerID = c.CustomerID
GROUP BY Age
ORDER BY Revenue DESC;
```
The script calculates the revenues by each age group and sort by revenues from high to low.
Result:
|Revenue | Age |
|----------|----------|
|2654268.94 | 26-35|
|1759049.91 | 36-45|
|1464283.08 | 18-25|
|1023200.90 | 46-50
|692134.79 | 51-55|
|432523.15 | 55+|
|255434.79 | 0-17|
|848.55 | 18-25|
