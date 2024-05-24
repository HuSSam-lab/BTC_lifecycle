import pandas as pd
import re
from datetime import date



raw_data = pd.read_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/Bitcoin_tweets.csv', nrows=500)

dyn_features = ['user_followers', 'user_friends', 'user_favourites', 'user_verified', 'is_retweet']
notdyn_features = ['date', 'user_created', 'hashtags']
df  = raw_data[ dyn_features + notdyn_features]
#################### 1
df.dropna(subset=notdyn_features,inplace=True)
# df.reset_index(inplace = True)
# df.drop(['index'],axis=1,inplace=True)

#################### 2
df['hashtags'].fillna("0")

# temp = [pd.to_datetime(i).date() for i in df['date']]
# df.loc[:,'date'] = temp ## i hate warnings message 😆 
# temp = [pd.to_datetime(i).date() for i in df['user_created']]
# df.loc[:,'user_created'] = temp
temp_date = []
temp_user = []
fix_date = []
fix_user_created = []
print('length DF before:  ',len(df))
for i in df['date']:
    try:
        df['date'].replace(i, pd.to_datetime(i).date(), inplace = True)
        # temp_date.append(pd.to_datetime(i).date())
    except:
        df.drop(index= df.index[df['date'] == i],inplace=True)
for i in df['user_created']:
    try:
        df['user_created'].replace(i, pd.to_datetime(i).date(), inplace=True)
    except:
        df.drop(index= df.index[df['user_created'] == i],inplace=True)
print('length DF after:  ',len(df))




######################### 3
# 💔take about 1 hour { re.sub("[]'[,]"," ",temp)  }
res = []
for i in df['hashtags']:
    tt = re.sub("[] ' []"," ",i)
    tt = tt.split(",")
    tt = [i.strip() for i in tt]
    res.append(tt)
df.loc[:,'hashtags'] = res

######################## 4 
df.loc[:,['user_verified','is_retweet']] = df[['user_verified','is_retweet']].replace([True,False],[1,0])
df = df.sort_values('date')
df.reset_index(inplace = True)

######################## 5
df.loc[:, 'Is_old_User'] = [((abs(date.today() - i).days) >= (365*4)) for i in df['user_created']]
notdyn_features.remove('user_created')
df = df[notdyn_features + dyn_features + ['Is_old_User']]
#-----------------------------------------------
### because the bad queality of data i find that when the i take all the row from data base the value come in float and other dtype (~ int)
user_foll_m = df['user_followers'].mean()
df['user_friends'] =  df['user_friends'].astype(int)
df['user_favourites'] =  df['user_favourites'].astype(int)
user_fri_m = df['user_friends'].mean()
user_fav_m = df['user_favourites'].mean()
stats = [user_foll_m, user_fri_m, user_fav_m]


vals = df[['user_followers','user_friends', 'user_favourites']].values
df['user_important'] = [(i > stats).sum() >= 2 for i in vals]
df.loc[:,['user_important','Is_old_User']] = df[['user_important', 'Is_old_User']].replace([True,False],[1,0])

df.drop(['user_followers', 'user_friends', 'user_favourites'], axis=1, inplace=True)

######################## 6



df.to_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Scripts out/Twitter.csv', sep = ";", index=1,index_label='id')
