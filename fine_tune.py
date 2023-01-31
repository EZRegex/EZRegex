import openai

import math
import time

with open('openai_key.txt') as f:
  API_TOKEN = f.readline()

openai.api_key= API_TOKEN


input = "NNN-NN-NNNN"

form = [
  f"Can you generate regular expression that represent {input}",
  f"make a regex : {input}",
  f"Regular expression: {input}"
]


tda_list = []





start = time.time()



for i in range(3):
  print(form[i])
  
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt = form[i],
    temperature=0.5,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  output = response['choices'][0]['text']
  
  print(output, "\n\n")

  tda_list.append(output)




# Program to find most frequent
# element in a list
def most_frequent(List):
  return max(set(List), key = List.count)
 


print(tda_list)


print(most_frequent(tda_list))






math.factorial(100000)
end = time.time()

print(f"\n\n\n{end - start:.5f} sec")