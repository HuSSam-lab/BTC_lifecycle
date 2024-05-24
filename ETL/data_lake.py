import pandas as pd

# ## storing the sources file before transforming it (ELT)
twitter_raw = pd.read_csv('Sources Files/Bitcoin_tweets.csv', nrows=500)

ada_raw = pd.read_csv('Sources Files/OHLCV_Binance_ADA-USDT_D20180417T040200UTC-D20240404T115959UTC_1min.csv')
bnb_raw = pd.read_csv('Sources Files/OHLCV_Binance_BNB-USDT_D20171106T035400UTC-D20240404T115959UTC_1min.csv')
eth_raw = pd.read_csv('Sources Files/OHLCV_Binance_ETH-USDT_D20170817T040000UTC-D20240404T115959UTC_1min.csv')
sol_raw = pd.read_csv('Sources Files/OHLCV_Binance_SOL-USDT_D20200811T060000UTC-D20240404T115959UTC_1min.csv')
XRP_raw = pd.read_csv('Sources Files/OHLCV_Binance_XRP-USDT_D20180504T081100UTC-D20240404T115959UTC_1min.csv')
btc_raw = pd.read_csv('Sources Files/bitcoin_2010-07-27_2024-04-25.csv')
t_dubai_raw = pd.read_csv('Sources Files/Trend/BTC Trend Dubai.csv')
t_germany_raw = pd.read_csv('Sources Files/Trend/BTC Trend Germany.csv')
t_uae_raw = pd.read_csv('Sources Files/Trend/BTC Trend UAE.csv')
t_us_raw = pd.read_csv('Sources Files/Trend/BTC Trend US.csv')
t_ww_raw = pd.read_csv('Sources Files/Trend/BTC Trend worldWide.csv')
print('imported Done :)')


twitter_raw.to_parquet('(ELT) Data lake/twitter.parquet')
ada_raw.to_parquet('(ELT) Data lake/curr/ada.parquet')
bnb_raw.to_parquet('(ELT) Data lake/curr/bnb.parquet')
eth_raw.to_parquet('(ELT) Data lake/curr/eth.parquet')
sol_raw.to_parquet('(ELT) Data lake/curr/sol.parquet')
XRP_raw.to_parquet('(ELT) Data lake/curr/xrp.parquet')
btc_raw.to_parquet('(ELT) Data lake/curr/btc.parquet')
t_dubai_raw.to_parquet('(ELT) Data lake/trend/dubai.parquet')
t_germany_raw.to_parquet('(ELT) Data lake/trend/germany.parquet')
t_uae_raw.to_parquet('(ELT) Data lake/trend/uae.parquet')
t_us_raw.to_parquet('(ELT) Data lake/trend/us.parquet')
t_ww_raw.to_parquet('(ELT) Data lake/trend/ww.parquet')
print('Exported Done ^_-')

