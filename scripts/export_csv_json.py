import pandas as pd

files = ["data/df_paginated_A","data/df_paginated_B","data/df_paginated_C","data/df_paginated_D","data/df_paginated_E"]

for single_file in files:
    df = pd.read_csv(single_file+".csv")
    df.to_json(single_file+".json",orient='records')