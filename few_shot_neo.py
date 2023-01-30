import pandas as pd

def tsv_to_df(file_list):

    data = pd.DataFrame()
    
    for data_file in file_list:
        data = pd.concat([data, pd.read_csv(data_file, sep="\t")])

    return data


train_data_list = ["specific.tsv", "general_2.tsv"]     #"specific.tsv", "passw-dataset-regex.tsv"

df = tsv_to_df(train_data_list)

print(df)






import json
import requests
from pprint import pprint



with open('hugging_face_key.txt') as f:
    API_TOKEN = f.readline()

print(API_TOKEN)






def query(payload='',parameters=None, options={'use_cache': False}):
    API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    body = {"inputs":payload,'parameters':parameters,'options':options}
    response = requests.request("POST", API_URL, headers=headers, data= json.dumps(body))
    try:
      response.raise_for_status()
    except requests.exceptions.HTTPError:
        return "Error:"+" ".join(response.json()['error'])
    else:
      return response.json()[0]['generated_text']




parameters = {
    'max_new_tokens':100,  
    'temperature': 0.5, 
    'end_sequence': "###"
}




def make_prompt(df) :

    prompt=""

    length = df.shape[0]

    for i in range(length) :
        prompt += f"""text: "{df.iloc[i]['input_text']}"\nregex: {df.iloc[i]['regex']}\n###\n"""

    return prompt





prompt = make_prompt(df)


q = "match an age between 35 and 59"

question = f"""text: "{q}"\nregex:"""

prompt = prompt + question

print(prompt)







options={'use_cache': True}





data = query(prompt, parameters, options)


pprint(data)