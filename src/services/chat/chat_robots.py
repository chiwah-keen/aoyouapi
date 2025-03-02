
from openai import OpenAI
from src.conf import conf




def ask_deepseek_with_deepseekchat(question):

    print("-------------->", question)
    client = OpenAI(api_key=conf.CHAT_SERVERS["deepseek"]["api_key"], base_url=conf.CHAT_SERVERS["deepseek"]["base_url"])

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question},
        ],
        stream=False
    )

    return response.choices[0].message.content
