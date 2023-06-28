import pandas as pd 

data = pd.read_json('workout-data-fr.json').to_csv('workout-data.csv',index=False)

    