import pandas as pd


def load_data(data_url):

    df = pd.read_csv(data_url)

    return df
