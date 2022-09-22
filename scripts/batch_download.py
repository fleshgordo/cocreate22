import requests
import pandas as pd
from time import sleep
import random 

# making the request
quality = "B"
params = "cnt:switzerland q:" + quality # change page=1, page=2, page=3 etc. if there are more than 500results
url="https://www.xeno-canto.org/api/2/recordings?query="+params
r = requests.get(url, headers={"Content-Type":"json"})
resp = r.json()
pages = resp["numPages"]
results = resp["numRecordings"]
print("There are " + results + " results on " + str(pages) + " pages.")
df = None

print("you really want to download? Type y / n and enter: ")
# input
answer = input()

if answer == "y":
    print("download")
    for i in range(int(pages)):
        i+=1
        url="https://www.xeno-canto.org/api/2/recordings?query="+params+"&page=" + str(i)
        r = requests.get(url, headers={"Content-Type":"json"})
        resp = r.json()
        print("fetching: " + url) 
        if 'df' not in locals():
            print("first runtime ... creating dataframe")
            df = pd.DataFrame.from_dict(resp["recordings"])
        else:
            df = pd.concat([df, pd.DataFrame.from_dict(resp["recordings"])])
            print("adding " + str(len(resp["recordings"])) + " entries to existing dataframe")
            print("currently " + str(len(df.index)) + " entries in dataframe") 
        sleep(1 + random.random() * 2) # make pause between requests
    outputfile = "data/df_paginated_"+ quality +".csv"
    df.dropna().to_csv(outputfile, columns = ["lng","lat","q"])
else:
    print("exit - ciao")
