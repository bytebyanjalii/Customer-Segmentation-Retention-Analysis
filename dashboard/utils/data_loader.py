import pandas as pd

def load_rfm():
    return pd.read_csv("../outputs/rfm_clusters.csv")

def load_raw():
    return pd.read_excel("../data/raw/Online_Retail.xlsx")