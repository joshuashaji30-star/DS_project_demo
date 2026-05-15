import pandas as pd
from src.helper import load_config


config= load_config()
raw_data_path = config['raw_data_path']

data= pd.read_csv(raw_data_path)
print(data.head())