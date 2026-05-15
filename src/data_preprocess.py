
import numpy as np


def data_preprocess(df):
    df = df.drop_duplicates()
    df["oldpeak_log"] = np.log1p(df["oldpeak"])
    return df


