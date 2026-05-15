import pandas as pd
from src.helper import load_config
from src.data_preprocess import data_preprocess
from src.modeling import train_model, evaluate_model, save_model



config= load_config()
raw_data_path = config['raw_data_path']
data= pd.read_csv(raw_data_path)

data= data_preprocess(data)
data.to_csv(config['preprocessed_data_path'], index=False)


model, X_test, y_test = train_model(data)
evaluate_model(model, X_test, y_test)
save_model(model, config['model_save_path'])
