#IncomeStatement
import datetime
import pandas as pd
import requests

api_key = 'coinranking909055a70c105030912075cb6fcb0c4d97547ecbcfbdb35c'
# api_key = 'coinranking909055a70c105030912075cb6fcb0c4d97547ecbcfbdb35y'## Wrong API
endpoint = "/coins"
headers = {'x-access-token': api_key}
url = f"https://api.coinranking.com/v2{endpoint}"

response = requests.get(url,headers)
def r():
    if response.status_code == 200:
        data = response.json()
        try :
            data = pd.DataFrame(data)
        except :
            return -1
        data.to_json('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Scripts out/RAW_API.json')
        raw_data = pd.read_json('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Scripts out/RAW_API.json')
        df = raw_data
        dic = df['data'].to_dict()
        coins = dic['coins']
        prices = []
        prices_name = []
        for i in range(50):
            price = coins[i]['price']
            price_name = coins[i]['name']
            
            prices.append(price)
            prices_name.append(price_name)
        prices.append(datetime.datetime.now().date())  
        prices_name.append('date')
        pri_dic = {'Curr_name' : prices_name,'Value':prices}
        
        df_price = pd.DataFrame(pri_dic)
        df_price.to_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Scripts out/clean_prices.csv', index=1)

        return 1
    else:
        res =  response.status_code
        return 0
print(r())

