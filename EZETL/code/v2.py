'''
file name: v1 EZETL 
description: Fixed file formats + regular expression-based ETL process using pandas 
'''
import openai
import pandas as pd 
import re

# 정규식 여러 개 중에서 하나 선택 
def most_frequent(List):
  return max(set(List), key = List.count)

# 정규식 공백 제거 
def delete_slash(text):
  if text[0] == '/' and text[-1] == '/':
    return text[1:-1]
  else:
    return text

# API 키 확인
with open('openai_key.txt') as f:
  API_TOKEN = f.readline()

openai.api_key= API_TOKEN

# ETL Process에 필요한 변수 설정 
extract_info = ""
input_format = ""
#input_requirements = ""
output_format = ""
load_name = ""

user_requirements = [extract_info, input_format, output_format, load_name]


# input.txt에서 Regex를 이용한 ETL process 에서 필요한 요건들을 읽어와서 저장
with open("input.txt", "r") as file:
    i = 0 
    for line in file:
        user_requirements[i] = line.strip()     # 개행문자 제거 후 저장 
        i += 1
        #print(user_requirements[i])
        #print(line)

print(user_requirements[1])

# ChatGPT Regex Prompt format
form = [
  f"Generate regular expression\n\ninput :{user_requirements[0]}\noutput:",
  f"Give me regular expression of {user_requirements[0]}.",
  f"Make regex to match {user_requirements[0]}",
  f"Can you generate regular expression that represent {user_requirements[0]} ? without any explaination",
  f"Regular expression: {user_requirements[0]}\nplease give me just regex.",
  f"let me know just a regular expression of the {user_requirements[0]}",
  f"I want only regex of {user_requirements[0]}",
  f"Can you make regular expression representing: {user_requirements[0]}"
]

tda_list = []

# Get Regex from ChatGPT using previous pormpt 
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

  #print("\n------------ form ------------\n")
  #print(form[i])
  #print("\n------------ output ------------")
  #print(output)

  tda_list.append(output)

# TDA를 이용해서 가장 많이 나온 Regex를 여기에 저장한다. 
EZRegex = most_frequent(tda_list)

#print(f"\n\nAnswer list : {tda_list.count(output)}")
#print(*tda_list[:len(form)], sep='\n')

if tda_list.count(EZRegex) == 1 :
  print("\n\nTry again")
else:
  print("\nThe regular expression for the request is {}".format(EZRegex))


# 정규식을 이용해서 받아온 데이터로부터 extract 
url = ""
file_name = "input.csv"
query = ""
connection = ""
table_name = ""


# 입력 받은 input data 포맷대로 데이터프레임에 저장
df = pd.DataFrame()

if input_format == "HTML":
    df = pd.read_html(url)

elif user_requirements[1] == "CSV":
    print("1")
    df = pd.read_csv(file_name)

elif user_requirements[1] == "JSON":
    df = pd.read_json(file_name)

elif user_requirements[1] == "Excel":
    df = pd.read_excel(file_name)

elif user_requirements[1] == "SQL":
    df = pd.read_sql(query, connection)

elif user_requirements[1] == "SQLite":
    df = pd.read_sql_query(query, connection)

elif user_requirements[1] == "Oracle":
    df = pd.read_sql(query, connection)

elif user_requirements[1] == "Azure":
    df = pd.read_sql_table(table_name, connection)

elif user_requirements[1] == "AWS EMR":
    df = pd.read_parquet(file_name)

elif user_requirements[1] == "AWS Glue":
    df = pd.read_parquet(file_name)

elif user_requirements[1] == "Dataflow":
    df = pd.read_csv(file_name)

elif user_requirements[1] == "URL":
    df = pd.read_csv(url)

else:
    print("[ERROR] Invalid value! ")
    exit()

print(df)

# df에서 정규식을 이용해서 데이터 추출 (Extract)
# extracted_data = df.applymap(lambda x: re.findall(EZRegex, str(x)))
pattern = re.compile(EZRegex)   # 일반 정규식을 Re 라이브러리에서 사용가능하게 변환
#extracted_data = df.apply(lambda x: x.str.extract(pattern))
extracted_data = df.stack().str.contains(pattern).any(level=0)
print(df[extracted_data])