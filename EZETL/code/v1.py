import openai
import math
import time



with open('openai_key.txt') as f:
  API_TOKEN = f.readline()

openai.api_key= API_TOKEN


extract_form = "input_g.csv"
extract_what = "all the data"
transform = "remove '$' in sales, and remove comma in sales, make a graph. x=year, y=sales"
load = "output.png"


p = f"""
Can you make ETL Python code?
Extract from:
{extract_from}
Extract what:
{extract_what}
Transform:
{transform}
Load:
{load}
"""



start = time.time()



  
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt = p,
  temperature=0.3,
  max_tokens=256,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

output = response['choices'][0]['text']

print(output)


math.factorial(100000)
end = time.time()

print(f"\n\n{end - start:.5f} sec")
