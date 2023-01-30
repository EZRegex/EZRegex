import openai

with open('openai_key.txt') as f:
    API_TOKEN = f.readline()

openai.api_key= API_TOKEN



p = """
text: "A valid URL with http/https"
regex: https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)
###
text: "SSN"
regex: ^(?!0{3})(?!6{3})[0-8]\d{2}-(?!0{2})\d{2}-(?!0{4})\d{4}$
###
text: "format NNN-NN-NNNN. Contain all zeroes in any specific group (e.g 000-##-####, ###-00-####, or ###-##-0000), Begin with 666., Begin with any value from 900-999."
regex: ^(?!0{3})(?!6{3})[0-8]\d{2}-(?!0{2})\d{2}-(?!0{4})\d{4}$
###
text: "At least 8 characters, at least one character, one number, and one special character"
regex: ^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$
###
text: "start with 'li' and end with 'e'"
regex: li*e
###
text: "start with 'w', end with 'i'"
regex: 
"""


response = openai.Completion.create(
  engine="text-davinci-002",
  prompt = p,
  temperature=0.5,
  max_tokens=256,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response['choices'][0]['text'])