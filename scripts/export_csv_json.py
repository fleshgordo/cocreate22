import requests
import pandas as pd
from time import sleep
import random 

df = pd.read_csv("sample_data/df_paginated_B.csv")

df.to_json("sample_data/df_paginated_B.json",orient='records')