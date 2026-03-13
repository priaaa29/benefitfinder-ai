import pandas as pd

def load_schemes():
    schemes = pd.read_csv("data/schemes.csv")
    return schemes