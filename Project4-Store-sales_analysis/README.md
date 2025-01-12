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
This table does not have a primary key column
<br/>
Table 'customers' has 3 columns and 4372 rows.
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
