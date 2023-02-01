import openai

import math
import time
import pandas as pd
import numpy as np
import sys


# Program to find most frequent
# element in a list
def most_frequent(List):
  return max(set(List), key = List.count)

def delete_slash(text):
  if text[0] == '/' and text[-1] == '/':
    return text[1:-1]
  else:
    return text



    

with open('openai_key.txt') as f:
  API_TOKEN = f.readline()

openai.api_key= API_TOKEN

f = open("./../dataset/input.txt", 'r')
input =f.read()

f.close()

form = [
  f"Generate regular expression\n\ninput :{input}\noutput:",
  f"Give me regular expression of {input}.",
  f"Make regex to match {input}",
]


# f"Can you generate regular expression that represent {input} ? without any explaination",
# f"Regular expression: {input}\nplease give me just regex.",
# f"let me know just a regular expression of the {input}",
# f"I want only regex of {input}",
# f"Can you make regular expression representing: {input}"

tda_list = []



start = time.time()



for i in range(len(form)):

  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt = form[i],
    temperature=0.3,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  output = response['choices'][0]['text']
  output = output.replace("\n", "")
  output = output.replace(" ", "")
  output = delete_slash(output)

  print("\n------------ form ------------\n")
  print(form[i])

  print("\n------------ output ------------")
  print(output)

  tda_list.append(output)



output = most_frequent(tda_list)


print(f"\n\nAnswer list : {tda_list.count(output)}")
print(*tda_list[:len(form)], sep='\n')


print(f"\n\nMost Frequent Answer is : {tda_list.count(output)}")

if tda_list.count(output) == 1 :
  print("\n\n다시 하자")
else:
  print(output)




math.factorial(100000)
end = time.time()

print(f"\n\n{end - start:.5f} sec")




new_p = f"Can you make some examples with regex: {output}\nmatched and not matched. each 3"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt = new_p,
    temperature=0.3,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

new_output = response['choices'][0]['text']

print(new_output)





new_p = f"Can you explain this regex: {output}\n"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt = new_p,
    temperature=0.3,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

new_output = response['choices'][0]['text']

print(new_output, "\n'n")

fout = open ("./../dataset/outpu.txt", "w")
fout.write(new_output)
fout.close()
