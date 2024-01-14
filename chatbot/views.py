from django.shortcuts import render
from django.http import JsonResponse
import openai

import pyttsx3
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






# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        message="suggest me one a positive reply for "+message
        response = chat_with_gpt(message)
        
        return JsonResponse({'message': message, 'response': response})
    

    
    return render(request, 'chatbot.html')





