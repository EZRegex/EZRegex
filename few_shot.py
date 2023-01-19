import pandas as pd

def tsv_to_df(file_list):

    data = pd.DataFrame()
    
    for data_file in file_list:
        data = pd.concat([data, pd.read_csv(data_file, sep="\t")])

    return data


train_data_list = ["specific.tsv"]

df = tsv_to_df(train_data_list)

print(df)






import json
import requests
from pprint import pprint



with open('hugging_face_key.txt') as f:
    key = f.readline()

print(key)