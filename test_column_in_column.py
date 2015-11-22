
import pandas as pd


df =pd.DataFrame({'coname1':['Apple','Yahoo','Gap Inc'],'coname2':[['Microsoft', 'Apple', 'Google'],['American Express', 'Jet Blue'],['American Eagle', 'Walmart', 'Gap Inc']]})



df['isin'] =df.apply(lambda row: row['coname1'] in row['coname2'],axis=1)

print df
