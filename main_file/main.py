# Description: This is a virtual assistant program that gets the date, current time, responds back with a
# random greeting, and returns information on a person

# Import the libraries

from typing import Text
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import sys
import time
import subprocess
import json
import requests
import sys





# Ignore any warning messages
warnings.filterwarnings('ignore')

# Record audio and return it as a string
def recordAudio():    
    # Record the audio
    r = sr.Recognizer()
    with sr.Microphone() as source:  
       print('Say something!')
       audio = r.listen(source)
    
    # Speech recognition using Google's Speech Recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand')
    except sr.RequestError as e:
        print('Request error from Google Speech Recognition')

    return data

# Function to get the virtual assistant response
def assistantResponse(text):
    print(text)
    # Convert the text to speech
    myobj = gTTS(text=text, lang='en', slow=False)
    
    # Save the converted audio to a file    
    myobj.save('assistant_response.mp3')
    # Play the converted file
    os.system('afplay assistant_response.mp3')

# A function to check for wake word(s)
def wakeWord(text):
    WAKE_WORDS = ['hey computer', 'ok computer'] 
    text = text.lower()  # Convert the text to all lower case words
  # Check to see if the users command/text contains a wake word    
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
  # If the wake word was not found return false
    return False

def getDate():
    
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]# e.g. Monday
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'February', 'March', 'April', 'May',
       'June', 'July', 'August', 'September', 'October', 'November',   
       'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', 
                      '7th', '8th', '9th', '10th', '11th', '12th',                      
                      '13th', '14th', '15th', '16th', '17th', 
                      '18th', '19th', '20th', '21st', '22nd', 
                      '23rd', '24th', '25th', '26th', '27th', 
                      '28th', '29th', '30th', '31st']
   
    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'

# Function to return a random greeting response
def greeting(text):
    # Greeting Inputs
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greetings', 'wassup', 'hello']
     # Greeting Response back to the user
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']
     # If the users input is a greeting, then return random response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'
    # If no greeting was detected then return an empty string
    return ''

# Function to get a person first and last name
def getPerson(text):
 wordList = text.split()# Split the text into a list of words     
 for i in range(0, len(wordList)):
   if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]

def getApplication(text):
 wordList2 = text.split()# Split the text into a list of words     
 for i in range(0, len(wordList2)):
   if i + 3 <= len(wordList2) - 1 and wordList2[i].lower() == 'open' and wordList2[i + 1].lower() == 'application':
            return wordList2[i + 2] 


while True:
    # Record the audio
    text = recordAudio()
    response = '' #Empty response string
     
    # Checking for the wake word/phrase
    if (wakeWord(text) == True):
    # Check for greetings by the user
         response = response + greeting(text)

         if ('date' in text):
             get_date = getDate()
             response = response + ' ' + get_date

         if ('who is' in text):
             person = getPerson(text)
             wiki = wikipedia.summary(person, sentences=2)
             response = response + ' ' + wiki

         assistantResponse(response)

    elif ('Spotify' in text):
        os.system(f"open /Users/klaas/Desktop/{text}.app")

    elif ('ask' in text):
            assistantResponse('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=recordAudio()
            app_id="24ERV5-QY6PWUL88A"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            assistantResponse(answer)
            
               
    elif ('stop' in text or 'shut up' in text):
       time.sleep(3)
       sys.exit(assistantResponse('Bye bye'))