import pickle
import pandas as pd
import datetime
    
with open('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Model/btc_price_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Model/scaler_btc_mode.pkl', 'rb') as f:
    scaler = pickle.load(f)
    
def model_inputs():


    model_inp_df = pd.read_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Scripts out/clean_prices.csv')
    # [ada_high, bnb_high, eth_high, xrp_high]
    coins = ['Cardano',  'BNB', 'Ethereum', 'Solana', 'XRP']

    datee = model_inp_df[model_inp_df['Curr_name'] == 'date']['Value']
    epoch = pd.Timestamp("1970-01-01")
    datee = (pd.to_datetime(datee.values) - epoch).total_seconds()

    
    # real_BTC = model_inp_df[model_inp_df['Curr_name'] == 'Bitcoin']['Value'][0]

    prices = [datee[0]]
    for i in coins:
        temp = model_inp_df[model_inp_df['Curr_name'] == i]['Value'].values[0]
        prices.append(float(temp))
    ### remeber here the right way it should take the prices during all the day to find the max for this day 
        ## but here i will consider the first price that i take it from the api is the max {^_^}

    prices = [int(i) for i in prices]
    # print(prices)

    # [worldwide, unitedstates, Germany, UAE,  Dubai]
    ## take the Trend data base that has month euqal to the month of the predicting day (day U Trend data base of the same month)
    trend_df = pd.read_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Scripts out/Google Trend.csv')
    
    predicting_month = datetime.datetime.now().month
    last_month_in_trend_df = pd.to_datetime((trend_df['date']).max()).month
    predicting_year = datetime.datetime.now().year
    last_year_in_trend_df = pd.to_datetime((trend_df['date']).max()).year
    
    if predicting_month > last_month_in_trend_df and predicting_year > last_year_in_trend_df:
        print("You need more google trend data {-_-}")
        return -1
    else: # the google trend is enough
        full_predicting_date = pd.to_datetime("".join([str(predicting_year), '-', str(predicting_month), '-', str(1)])).date()
        trend_df['date'] = [pd.to_datetime(i).date() for i in trend_df['date']]
        predicting_date_ind = trend_df.index[trend_df['date'] == full_predicting_date].values[0]
        # print(predicting_date_ind)
        Trend = []
        for i in trend_df.iloc[predicting_date_ind][1:]:
            # [worldwide, unitedstates, Germany, UAE, Dubai]
            Trend.append(i)
            
        return prices + Trend
        
        


### result will be like 
    ##[ada_high, bnb_high, eth_high, xrp_high, worldwide, unitedstates, Germany, UAE, Dubai]

try:

    sample_to_predict = [model_inputs()]
    if sample_to_predict == -1:
        print(sample_to_predict)
    else:       
        
        scaled_sample = scaler.transform(sample_to_predict)
        pred = model.predict(scaled_sample)
        print(pred)
        
     
except ValueError as e:
    print(e)




# sample_to_predict = [ 0.282093, 12.723299, 670.587438, 0.674941, 16, 12, 14, 14, 13] ## right target are {8640.197051}
# real_BTC = 8640.197051
# scaled_sample = scaler.transform([sample_to_predict])
# print(type(scaled_sample))
# pred = model.predict([scaled_sample])
# print(f"I think it is :{pred}")
# print(f"But it is :{real_BTC}")