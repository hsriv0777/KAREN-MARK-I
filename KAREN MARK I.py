import requests, json
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime, time
import wolframalpha
import os
import sys
import playsound
import pyjokes
import socket
import subprocess
from plyer import notification
from pprint import pprint
from bs4 import BeautifulSoup 
import requests  
import pandas as pd

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('YOUR_CLIENT_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

name = 'Hritik'
bot = 'Karen'


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def playMusic():
    try:
        music_dir = 'F:\\PRSNLS\\music folder'
        songNum = random.randint(0,19)
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[songNum]))
        print('\n\tPlaying Music...... ')
        speak('okay sir playing your Music, enjoy!')
    except:
        speak('Unable to Play Music From Your Device!')
        print('\n\tUnable to Play Music!')


def connectionCheck():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('www.google.com', 80))
        s.close()
    except Exception:
        print("\n\t<!!! OFFLINE !!!>" )
        print('\n\tUnable to Connect!' )
        speak('Sorry sir you are not connected to the internet!')
        quitApp()

def quitApp():
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<18:
        speak('Bye sir, Have a Good Day!')
    else:
        speak('Bye sir, Good Night!')
    exit(0)    

connectionCheck()
print("\n\t<!!! ONLINE !!!>")

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak(f'Good Morning {name}!')

    if currentH >= 12 and currentH < 18:
        speak(f'Good Afternoon {name}!')

    if currentH >= 18 and currentH !=0:
        speak(f'Good Evening {name}!')

greetMe()

stMsgs = ['I am so happy to see you again',
          'Recently I was thinking about you!',
          'i missed you! just joking yar come on!',
          'Lets start what we have to do!',
          'Hey! Feeling Happy to see you again']
ans_q = random.choice(stMsgs)
speak(ans_q)


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query.capitalize() + '\n')
        
    except sr.UnknownValueError:
        stMsgs = ['Sorry sir! I didn\'t get that! type the command!', 'sorry sir can you please type the command', 'i am not sure please type that!']
        ans_q = random.choice(stMsgs)
        speak(ans_q)
        a = str(input('Your Command: '))
        query=a

        

    return query

def Take_break():
    speak("How long to notify?")
    tm = input("Enter time in seconds: ")
    speak(f'Ok sir i will remined you to take a break after,{tm} seconds')
    time.sleep(int(tm))
    notification.notify(title="PLEASE TAKE A BREAK SIR! ", 
    message="I will re-remined you after 30 seconds", 
    timeout=10) 
		
    time.sleep(0.5*60) 

    speak("Please Take a break Sir") 
		
    notification.notify(title="Break Notification", 
    message="Please do use your device after sometime as you have"
    "been continuously using it for 45 mins and it will affect your eyes", 
    timeout=30)


name = 'Hritik'.lower()
bot = 'KAREN'.lower()
wakeWord = 'Ok'.lower()
emailadd = 'YOUR_MAIL_ID'
pword = ' '
os.system('cls')

        

if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()
        
        if "youtube" in query:
            speak("Ok! Fetching Results")
            query = query.replace("youtube ", "")
            query = query.replace(" youtube", "")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
            speak("Checkout Youtube Results!")

        elif "search" in query or 'google' in query:
            query = query.replace("search", "")
            query = query.replace(" for ", "")
            query = query.replace(' google', '')
            query = query.replace('google ', '')
            webbrowser.open(f'https://www.google.com/search?q={query}')
            speak(f"Searching for {query}")

        elif '.' in query:
            webs_name = query.replace('open ', '')
            speak(f"Opening {webs_name}!")
            webbrowser.open('http://'+ webs_name)

        elif 'say ' in query or 'speak' in query:
            copy = query.replace("say ", "")
            speak(copy)
            time.sleep(1)

        elif 'the time' in query:
            x = datetime.datetime.now()
            speak("Sir the time is")
            speak(x.strftime("%X"))
 

        elif 'the date' in query:
            x = datetime.datetime.now()
            speak("Sir today is")
            speak(x.strftime("%c"))


        elif 'cashflow game' in query:
            speak('okay')
            webbrowser.open('www.richdad.com/classic?game')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "shutdown" in query or 'shut down' in query or 'turn off' in query:
            speak("Are you sure sir ?")
            answ = myCommand()
            
            if 'yes' in answ or 'sure' in answ or 'yeah' in answ or 'shut down' in answ:
                speak('Okay sir! Shutting Down in a Minute.')
                os.system('shutdown -s')
                quitApp()
            else:
                speak("Okay! Don't Worry")

        elif 'my website' in query or 'goto my website' in query:
            speak('Opening in Browser Please Visit!')
            webbrowser.open('YOUR_WEBSITE')

        elif 'joke' in query:
            speak(pyjokes.get_joke(language='en'))


        elif 'your name' in query or " what's your name" in query:
            speak("my name is {bot} if you want change my name you change it anytime")

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
            speak('What about you')
            content = myCommand()

            if 'fine' in content or 'just like you' in content or 'not bad' in content:
                speak('okay sir! keep it up')

            elif "bad"in content or ' i am sad' in content:
                speak('So sorry to hear')

            elif 'bored' in content or 'boring' in content:
                speak('So sorry to hear that you are Boring with me!  nex time I will try my best!')
                

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("hsriv0777@gmail.com", 'hectoris')
                    server.sendmail('your_email_id', "receiver_id", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'see you soon' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query or 'hii' in query:
            speak('Hello {name})

        elif 'who are you' in query or 'tell me about you' in query or 'tell about you' in query:
            speak('I am a python program! Basically programed for assistant purpose by Mr. Hritik! my date of birth is twenty four! july !2020') 
         
        elif 'okay bye' in query or 'see you again' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
      
        elif'play music' in query or 'change music' in query or 'some music' in query or 'the music' in query:
            playMusic()


        elif 'play ' in query:
            music_name = query.replace('play ', '')
            musicSearch = f'https://music.youtube.com/search?q={music_name}'
            speak(f'\n\t-->  Playing {music_name} online .......\n')
            webbrowser.open(musicSearch)
            time.sleep(1)

        elif 'launch' in query:
            query = query.replace('launch ', "")
            app = query.title()
            try:
                os.startfile(app)
                speak(f'Launching {app}....')
                
            except:
                speak(f"Couldn't Launch {app}, Should I Search Online?")
                reply = myCommand()
                if "yes" in reply or 'ok' in reply or 'yup' in reply or 'do' in reply:
                    speak('Fine, Searching Online!')
                else:
                    speak("Okay, Don't Worry")

        elif 'task manager' in query or 'task-manager' in query:
            speak('Opening Task Manager')
            os.startfile('C:\\Windows\\system32\\Taskmgr.exe')

        elif "wi-fi details" in query or 'wifi details' in query:
            try:
                speak("Trying to Show Details")
                subprocess.call('netsh wlan show profiles')
                time.sleep(5)
            except:
                speak(" Sorry sir, Unable to Show Details!")

        elif 'ip details'in query or 'my ip' in query:
            speak("Showing Ip Details")
            subprocess.call("ipconfig")
            time.sleep(4)

        elif 'system information' in query or 'system info' in query:
            speak("Ok, Showng Your System Information. Please Wait!")
            subprocess.call('systeminfo')
            speak('Done, please checkout this!')
            time.sleep(7)

        elif 'task list' in query or 'tasklist' in query:
            speak('Showing All Running Tasks!')
            subprocess.call('tasklist')
            time.sleep(10)

        elif 'clear' == query or 'clean' == query or 'clear console' in query:
            os.system('cls')
            speak('Current Console Cleared')

        elif bot == query:
            toReply = [
                'Ready to Help You sir!',
                'How Can I Help You sir?',
                'I am Here for you!'
            ]
            toReply = random.choice(toReply)
            speak(toReply)

        elif 'thanks' in query or 'thank you' in query:
            thanksGiving = [
                'Nevermind!',
                'You are Always Welcome!',
                'Mention Not!',
                "That's My Duty sir!"
            ]
            thanksGiving = random.choice(thanksGiving)
            speak(thanksGiving)

        elif 'welcome' in query:
            speak('I Feel Honored!')

        elif 'sorry' in query or 'my fault' in query or 'my mistake' in query:
            speak("Don't worry sir!")

        elif 'logout' in query or 'sign out' in query:
            speak("Logging off...")
            os.system("shutdown -l")
            quitApp()
            
        elif "you feeling" in query:
            speak("feeling Very sweet after meeting with you")

        elif "you doing" in query:
            speak('oh! waiting for your command')

        elif 'ok' in query or 'okay' in query:
            speak("That's It.")

        elif 'take a break' in query:
            Take_break()

        elif 'open whatsapp' in query:
            speak("here is your whatsapp. make sure that your phone is connected to the internet")
            webbrowser.open('https://web.whatsapp.com/')

        elif 'covid' in query or 'corona virus' in query:
            x=[] 
            x1=[] 
            source=requests.get('https://www.worldometers.info/coronavirus/country/india/').text 
            soup=BeautifulSoup(source,'lxml') 
            z=soup.find_all('div',id='maincounter-wrap') 
            z1=soup.find_all('div',class_='maincounter-number') 
 
            for k in z:
                y=k.h1.text 
                x.append(y) 
 
            for i in z1: 
                y1=i.span.text 
                x1.append(y1) 
     
            df=pd.DataFrame(x1,x,['Number']) 
            df.head()
            speak(df)


        else:
            query = query
            speak('Searching on the internet! It will take some little bit please wait!')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
