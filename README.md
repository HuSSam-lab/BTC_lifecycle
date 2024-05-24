# BTC_lifecycle
Studying BTC(Bitcoin cryptocurrency) using SSIS,SSAS,python,SQL,DAX,Power-BI and statistics(ML) in simple Data engineer project


Mission Statement (ETL)
* The aim of this project is to Studying the historical price change of Bitcoin and the factors affecting the price and in the end help the trader in Decision making Therefore, understand the way the price changes as much as possible. (Fully automatic and some dynamics)

* Automate historical data-extraction and daily API data-extraction for Bitcoin prices.
Extract: historical of BTC and other Cryptocurrency prices, Twitter comments, BTC Google Trend.

* Transform: historical of prices to [date, high prices], Twitter to [ranking the comments and user important on BTC price], Google trend in [UAE, DE, Dubai, …..]
Loading the clean and transformed data to a DW finishing with power BI report which help trader in decision making + machine learning model to predict the price.


Collect data that has a correlation to the price
What I will need to Collect:

* Historical Bitcoin Price Data (old data)
* Historical cryptocurrency Prices Data (old data)
* Social Media Sentiment (Twitter)
* Volume of Bitcoin mentions on social media (Track Hashtags, Keywords, user followers and user created account and comments).
* Historical Relation of Google trend with BTC price.(from old to present)
* Daily BTC and other 49 cryptocurrency prices to store it in separated DB for the future.


# ETL architecture (Data flow)
![image](https://github.com/HuSSam-lab/BTC_lifecycle/assets/73494744/16941df8-0b59-4aa5-8900-f710764415b4)

# ERD
![image](https://github.com/HuSSam-lab/BTC_lifecycle/assets/73494744/e2076746-b6f9-42ee-a9d0-3bd275ac20bb)

# ETL pipeline package
![image](https://github.com/HuSSam-lab/BTC_lifecycle/assets/73494744/89e07ff8-cbd9-4feb-85cd-72617c1a98c3)

# Staging Data Flow
![image](https://github.com/HuSSam-lab/BTC_lifecycle/assets/73494744/cf56a7e8-3240-4db1-953a-14337258975f)

# Getting new prices and appending it See {What “No” mean} very helpful -_-
![image](https://github.com/HuSSam-lab/BTC_lifecycle/assets/73494744/d8b5d32d-728e-4900-a260-7c82074a6b59)

# Storing historical and new data
![image](https://github.com/HuSSam-lab/BTC_lifecycle/assets/73494744/46e63ce4-b336-4623-a697-42b5694544a6)

BTC and other cryptocurrency
* Changing the date format from timestamp to date format because I will studding depending on one days ignoring the time, and this will apply on all prices file, also keep the high price in the day.
* Merging all cryptocurrency together and keep date and high price from all cryptocurrency files, then export the table to SQL row table in staging data base.

Twitter
* Get the total data base using pandas data frame and apply some rules and mathematic equations to filtering the comments.
* Also ranking the commenters depending on the date of creating account and number of followers, because this ranking affect on the quality of comment then affect on the BTC price.
* Changing the timestamp format to date format (like BTC prices).
* As you except, in one day we have more than one comment so we need to group by depending on days, and apply sum as aggregate function to find number and quality of 
comments in this day.
* Finally we will get Clean-Twitter data base which has indirectly correlation and affect with BTC price.

Google trend
* Getting data base from official Google trend website which shows rank of BTC trend during the studying year.
* Rank was in (US, GE, Dubai, UAE, worldwide).
* Finally adding the clean google trend with all region to final row data base.


Dataset:(target) 🏡
CSV files:
  1. BTC, ADA, BNB, ETH, XRP, SOL.	
  2. Clean prices.
  3. Google trend.
  4. Twitter.
Json files:
  1. Raw real time prices.
SQL: 
   Staging BTC:
     1. Backup real time prices.
     2. Google trend staging prices.
     3. Raw prices
     4. Storing new historical prices.
     5. Twitter staging.

# Data Warehouse
![image](https://github.com/HuSSam-lab/BTC_lifecycle/assets/73494744/dd49764c-8dcd-40aa-849e-4ee55d0fe3cc)


Training ML
* I use XGBoost regressor for predicting.
* I use this features as input for the model:
(ADA, BNB, XRP, SOL, ETH) prices + (Dubai, US, UAE, GE, worldwide) trend + dates
* The advantages of twitter data base was very good and helps the model to get high accuracy 
* (why you don’t use twitter comments as input for your model)? ^_^
The Twitter data base was good but use full for short time it was just for {2021-02-05  2021-04-24} so it is very short, but the ETL and training model code can dealing with twitter comments in the future without any changing (just add enough twitter comments for the input and it will get into training process)
* So finally I get model with MSE = 600 for just 2418 rows as input and very good results, which are very help full for trader and decision maker
* Training the model will start automatically with SSIS package, but predicting price need run script.


# Test and prediction
![image](https://github.com/HuSSam-lab/BTC_lifecycle/assets/73494744/51e225b3-46c0-41fb-aa99-9e55202fa1f1)


ELT
* Here I use python script to extract all CSV and row file without any changing then storing it in parquet file format.
Why this step? ^_*
* I want to update the predicting process (I will try to using LSTM predicting BTC price) so I will need to do deferent transformation on the data to make the future model dealing with it.


What is the future updates my project needs?

* Create timer to run the API (python script) code then storing the average of high cryptocurrency prices then storing the final average prices in backup SQL table (in this case the prices will be in row data base is real average high-prices {right now I can’t do this because I have limited API and I can’t request more than 100 times at month}.
* Prepare the Volume of each cryptocurrency amount to insert it as input for training the model to predict the prices.
* Searching for more features that affect on the BTC prices in direct and indirect way.

                              The End ^_-
















