# test.py
# Just a file to test if the OPENAI GPT3 API is working fine.

import json
import openai
import os

openai.api_key = "API_KEY" #os.getenv("API_KEY")


# prompt = """Poor English: Please provide me with a short brief of the design you’re looking for and that’d be nice if you could share some examples or project you did before.
# Corrected English: Please provide me with a short brief of the design you’re looking for and some examples or previous projects you’ve done would be helpful.
# Poor English: If I’m stressed out about something, I tend to have problem to fall asleep.
# Corrected English: If I’m stressed out about something, I tend to have a problem falling asleep.
# Poor English: There is plenty of fun things to do in the summer when your able to go outside.
# Corrected English: There are plenty of fun things to do in the summer when you are able to go outside.
# Poor English: She no went to the market.
# Corrected English: She didn’t go to the market.
# Poor English: Tell my name to dearest.
# Corrected English:"""

def bot(question):
    prompt = """This is chat between Sushant and Siri. Siri is an AI assistant
    and knows almost everything. It is designed to assist and help humans with
    all kinds of questions and provide them detailed answers to any questions
    that they ask.
    Sushant: {}
    Siri:""".format(question)

    response = openai.Completion.create(
        engine="ada",
        prompt=prompt,
        stop="Sushant:",
        temperature=0,
        max_tokens=200
    )

    print(response)
    json_response = json.dumps(response)

    rep = json.loads(json_response)

    bot_reply = rep['choices'][0]['text']

    print(question)
    print(str(bot_reply))

    return str(bot_reply)
