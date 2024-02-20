import openai
openai.api_key='sk-ohjp56bFBhoVoj3cc9ry2RUIjT3BlbkFJHKuuLPRc2t8757ksiRXE'

def Senitement_analysis(text):
    messages=[
        {"role":"system","content":"""you are tried to analyzed and detect the sentiment of given"""},
        { "role":"user", "content": f"""Analyze the following text and determine if the sentiment is:positive or negative{text}"""}


    ]
    response = openai.ChatCompletion.create(
                      model="gpt-3.5-turbo",
                      messages=messages,
                      max_tokens=1,
                      n=1,
                      stop=None,
                      temperature=0)

    response_text = response.choice[0].message.content.strip().lower()
    return response_text

# Calling the function
input = 'I hate fast food'
response = Senitement_analysis(input)
print(input,':The sentiment is',response)

