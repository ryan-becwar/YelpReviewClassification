import pandas as pd
import json

json_file = 'yelp_academic_dataset_checkin.json'

with open(json_file) as fin:
    i=0
    for line in fin:
        line_contents = json.loads(line)
        print(line_contents)
        i+=1
        if i==3:
            break

df = pd.read_csv('yelp_academic_dataset_review.csv')

df.drop(columns=['review_id','user_id','business_id','date','useful','funny','cool'],inplace=True)

df1 = df.sample(100,random_state=0)
df2 = df.sample(1000,random_state=0)
df3 = df.sample(10000,random_state=0)

df.to_csv('all_reviews.csv')
df1.to_csv('100_reviews.csv')
df2.to_csv('1000_reviews.csv')
df3.to_csv('10000_reviews.csv')