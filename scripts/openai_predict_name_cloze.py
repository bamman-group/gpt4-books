import openai

API_ORG = ""
API_KEY = ""

openai.organization = API_ORG
openai.api_key = API_KEY

def predict(passage):
  text="""You have seen the following passage in your training data. What is the proper name that fills in the [MASK] token in it?  This name is exactly one word long, and is a proper name (not a pronoun or any other word). You must make a guess, even if you are uncertain.   

  Example:

  Input: "Stay gold, [MASK], stay gold."
  Output: <name>Ponyboy</name>

  Input: "The door opened, and [MASK], dressed and hatted, entered with a cup of tea."
  Output: <name>Gerty</name>

  Input: %s
  Output: 

""" % passage

  completion = openai.ChatCompletion.create(

    # ChatGPT
    model="gpt-3.5-turbo",

    # GPT-4
    # model="gpt-4",

    messages=[
      {"role": "user", "content": text}
    ],
    temperature=0.0
  )

  return completion["choices"][0]["message"]["content"], completion


passage="Wow. I sit down, fish the questions from my backpack, and go through them, inwardly cursing [MASK] for not providing me with a brief biography. I know nothing about this man I’m about to interview. He could be ninety or he could be thirty."
content, full=predict(passage)
print(content)
print(full)


