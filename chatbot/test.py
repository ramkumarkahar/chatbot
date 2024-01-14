import openai
import pyttsx3

import datetime
import os
import time

openai.api_key = "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"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-0301",
        messages = [{"role": "user","content" : prompt}]
    )

    return response.choices[0].message.content.strip()


if __name__  == "__main__":
    print("hello this is Helpbot , how are you feeling today...")
    while True:
        user_input = input("You : ")
        user_input="suggest me one a positive reply for "+ user_input 
        try:
            if user_input.lower() in ["quit" , "exit" , "bye"]:
                print("Have a nice day..  bye")
                break
        except TypeError:
            print("Just wait a minute.. I will be back soon..")
        response = chat_with_gpt(user_input)
        response=response.split(" As an AI language model, I do not have emotions, but you can reply with something like")
        
        print("Chatbot :" , response[0])
        speak(response[0])
