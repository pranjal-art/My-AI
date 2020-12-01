import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import time
import win10toast
from subprocess import *
import sounddevice
from scipy.io.wavfile import write
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from playsound import playsound
import datetime as dt
from gpiozero import Robot
from time import sleep

"""
robot = Robot(left = (27, 17), right = (22, 23))
"""

clear = lambda: os.system("cls")
clear
toaster = win10toast.ToastNotifier()

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('V7EAL6-JGR56ELT3H')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-3].id)

def speak(audio):
    print('Arduino: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=21:
        speak('Good Evening!')

    if currentH >= 21 and currentH !=0:
        speak("Good night!")

playsound('ui-wakesound.mp3')

def myCommand():

    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        playsound('ui-endpointing-touch.mp3')
        speak('Sorry sir!  I didn\'t catch that! Can you please repeat that?')
        playsound('ui-wakesound.mp3')
        query = myCommand()

    return query

if __name__ == '__main__':

    n = 0

    if n <= 1:

        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif "hello" in query or "hi" in query or "hello arduino" in query or "hi arduino" in query:
            greet = "Hello there. 😁😎😍"
            speak(greet)

        elif "detect my face" in query or "am i safe ffom corona" in query or "am i safe" in query or "corona" in query:
            speak("Let, me hendel this, sir...")
            speak("Let's check.")
            Popen('python detect_mask_video.py')

        elif 'your help' in query or "arduino help" in query:
            speak("#Arduino help section -")
            speak("Help is loading...")
            tip = ['I was designed by prasoon rai' , 'I am getting smarter everyday!' , 'I can play music' , 'What\'s up buddy!']
            time.sleep(1)
            print("#------- " + "12.5%")
            time.sleep(2)
            print("##------ " + "25%")
            time.sleep(2)
            print("###----- " + "37.5%")
            time.sleep(2)
            print("####---- " + "50%")
            time.sleep(2)
            print("#####--- " + "62.5%                                                        " + 'Do you know?: ' + (random.choice(tip)))                                               
            time.sleep(2)
            print("######-- " +"75%")
            time.sleep(2)
            print("#######- " + "87.5%")
            time.sleep(2)
            print("######## " + "100%")
            speak("Done!")
            playsound('system-alerts-melodic-01-short.mp3')
            print('''
            <------------------------------------------------------------------------------------------>
            #Arduino help...
            Help -
            Arduino AI was designed by a solo developer, Prasoon rai.
            For more information just say 'more information arduino' or 'information arduino'.

            What's upcoming? --->

            Well, we are working on new updates right now!

            What's new -->

            1. You can play game's with Arduino! like - Hangman, snake game, golf game, drawing pragram!
            Well, soon I am going to bring new updates to the AI like a online chess game!

            2. It can even recognize your face!
            Don\'t worry because your data is safe and will not be leaked.

            3. It can send e-mail, set alarms, play music, call anybody, perform many more amazing things.
            Just ask 'what can you do?' 

            4. I can tell you some of my most amazing features here -
              (a) Can tell you the weather of anyplace.
              (b) Tell you a story.
              (c) Tell you joke.
              (d) Perform mathematical operations.
              (e) Can do things related to science.
              (f) I can be your best friend!

             A common Tip by AI Arduino:

             Ok, please don't ask me such kind of questions, like 'can you walk?, can you dance and can you drive a car 
             etc...
             So, my answer to all such questions is |No|, but if you want me to do such things, make any kind
             of robotic body you like (using a raspberry PI) and just tell your Ideas to my developer
             at his G-mail ID  (arduinobot.vbps@gmail.com) and you will get a responce from him under 5 days with basic codes...
             Well how to run the codes and other important information will be give with a handy guide added with the E-mail
             
             Well, you can Improve me because I am open source!

             Thanks!
            <------------------------------------------------------------------------------------------->
            All the information given in guide.
            In order to open the guide just say 'open help guide' or 'Help guide'.
            ''')
            

        elif "set a alarm" in query or "set a timer" in query:
            speak("Loading Alarm...")
            time.sleep(1)
            Popen('python alarm.py')
            time.sleep(10)

        elif "help guide" in query or "open help guide" in query:
            webbrowser.open("http://cmsplanes.ezyro.com")

        elif "what are your secrets" in query or "what is your secret" in query or "tell me your secrets" in query:
            speak("If, I will tell you my secrets. It will not be a secret!")

        elif "start facerecognition" in query or "face recognition" in query or "start face recognition" in query:
            from subprocess import *

            Popen('python Driver_Cam.py')
            greetMe()
            clear()

        elif "system info" in query or "info" in query:
            speak("Loading...")
            speak("Info loaded...")
            speak("---------------------------------------------------------------------------------------")
            speak("No current updates...")
            speak("I automatically get updated.")
            speak("---------------------------------------------------------------------------------------")

        elif "set a alarm" in query or "set a timer" in query:
            Popen('python delta.py')

        elif "open binge" in query or "open bige" in query:
            webbrowser.open('https://www.bing.com/') 

        elif "open opera" in query or "open opera gaming browser" in query or "open opera gx" in query or "open opera GX" in query:
            webbrowser.open('http://opera.com')
            print('''
            -------------------------------------------------------------------------------------------------------
            WARNING!

            Opera isn't available for commercial use on browsers. You need to download it.
            However, the AI Arduino can run opera and opera GX locally.

            It's safer to run saffari , google , binge , Microsoft edge and Mozila firefox!

            What we recommend?

            WINDOWS - 

            Well our AI is released officialy for Windows 10, 10.1 , 10.2 and Windows 7 
            so, we recomend Binge , Microsoft edge and Google.
            
            Depends upon your default browser!

            MAC -

            We, recommend safari for MAC 

            Linux -

            Well, we haven't released it officialy for Linux but you can you it on linux
             (Codes and installation to be performed indivussialy)

             However, for smoother experience we recommend Mozzila Firefox and Google for linux.

             ------------------------------------------------------------------------------------------------------
             Any loss of data, harm to computer or anything else will not be on our risk if you use Opera / Opera GX
             or any opera browser!
             ------------------------------------------------------------------------------------------------------

             Thanks!
             -------------------------------------------------------------------------------------------------------
            ''')


        elif "play snake game" in query or "start snake game" in query or "snake game" in query:
            speak("Starting snake game...")
            Popen('python snake.py')

        elif "open microsoft" in query or "open mycrosoft account" in query or "open my microsoft account" in query:
            webbrowser.open_new_tab('https://account.microsoft.com/')
            speak("Happy journey! " + ":-)")

        elif "open digital clock" in query or "start digital clock" in query or "digital clock" in query:
            speak("Loading digital clock...")
            time.sleep(2)
            Popen('python3 digital_clock.py')

        elif "clear" in query or "clear chat" in query:
            speak("Clearing...")
            speak("This may take some time...")
            clear()
            print('Loading')
            time.sleep(2)
            clear()
            print('Loading.')
            time.sleep(2)
            clear()
            print('Loading..')
            time.sleep(2)
            clear()
            print('Loading...')
            time.sleep(2)
            clear()
            print('Loading')
            time.sleep(2)
            clear()
            clear()

            speak("Chat history is deleted...")
            clear() 
            speak("Loading codes...")
            time.sleep(2)
            print("--------------------------------------------------------------------------------")
            speak("Basic cascade loaded")
            time.sleep(1)
            speak("done")


            """

        elif "move forward" in query or "move forveward" in query:
            robot.forward()
            sleep(5)
            robot.stop()                   
                                                        #To make the robo move forward...

        elif "move backward" in query or "move bakward" in query:
            robot.backward()
            sleep(5)
            robot.stop()
                                                        #To make the robot move backward...

        elif "turn left" in query or "move left" in query:
            robot.left()
            sleep(5)
            robot.stop()
                                                        #To make the robot move left...

        elif "move right" in query or "turn right" in query:
            robot.right()
            sleep(5)
            robot.stop()
                                                        #To make the robot move right...

           """
                                                        
        elif "open python drawing program" in query or "python drawing" in query or "open python drawing" in query:
            Popen('python main.py')

        elif "record my voice" in query or "make a announcement" in query:
            speak("Ok, starting to record your voice!")

            fs=44100
            second=10
            print("recording -")
            record_voice=sounddevice.rec(int(second * fs),sample=fs,channels=2)
            sounddevice.wait()
            write("output.wav",fs,record_voice)

        elif "open hangman game" in query or "start hangman" in query or "open python hangman game" in query or "open python hangman" in query:
            Popen('python hangman.py')

        elif "play" in query:
            import pywhatkit as kit
            speak("We may encounter a ad as I am going to play the music on youtube.")
            kit.playonyt(query)

        elif "remember that" in query or "remember" in query:
            speak("Ok, I will remember that you told me,")
            speak("To," + (query))

        elif "where do i kept" in query or "where is my" in query or "tell me where i kept" in query or "where i kept my" in query:
            speak("You told me to remember that -")
            speak(query)

        elif "show my history" in query or "show my browsing history" in query:
            speak("Heres your browsing history!")
            import time
            time.sleep(15)

        elif "send a notification" in query or "send me a notification" in query:
            import win10toast
            speak("What should I send as a notification?")
            notification_con = myCommand()
            toaster = win10toast.ToastNotifier()
            toaster.show_toast((notification_con) , duration=7)


        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "open my os" in query or "open rc os" in query or "open plane os" in query or "plane os" in query or "open cms" in query:
            Popen('OS.bat')

        elif "would you marry me" in query or "will you marry me" in query or "marry me" in query:
            speak("Well before answering this question")
            speak("You have to answer some questions!")
            speak("Are you ready?")
            speak("Let's begin!")
            speak("1. When is my birthday?")

            A_A = myCommand()

            if "8 january" in A_A or "eight january" in A_A or "Eight January" in A_A:
                speak('Wow! great')
                speak("Let's move towards next question!")

            else:
                ("Wrong answer!")
                while(1):
                    break

            speak("1. What is my favourite colour?")

            B_B = myCommand()

            if "red" in B_B or "Red" in B_B:
                speak("Correct answer!")
                speak("Let's move toward\'s next question")
                speak("This one is going to be a bit harder!")

            else:
                speak("Wrong")
                while(1):
                    break

            speak("3. Who made me?")

            C_C = myCommand()

            if "Prasoon rai" in C_C or "prasoon rai" in C_C:
                speak("Great! but")
                speak("Right, now I am wrapping my head around the concept of love")
                speak("So, for now I would like to answer by this song!")
                webbrowser.open('https://www.youtube.com/watch?v=lNmAkWvnWEg')

            else:
                speak('Nah...')
                speak("I, think we need more time to get to know each other!")

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif "make my notes" in query or "make my school notes" in query:
            speak("Let's start making your notes...")
            speak("Enter your notes here -")
            speak("To exit notes just say, exit notes")
            note_content = myCommand()

            if "exit notes" in note_content or "exit note" in note_content:
                while(1):
                    quit
            
        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient or 'MI' in recipient or "mi" in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Mail", 'Passward')
                    server.sendmail('Your_Mail', "Your_Mail", content)
                    speak('Email sent!')
                    server.close()

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif "stop" in query:
            sys.exit

        elif "information arduino" in query or "more information arduino" in query:
            speak("Ok")

        elif "Who made you" in query or "who is your master" in query or "who made you" in query:
            ans_m = ("Prasoon rai made me... Thanks to him!")
            speak(ans_m)

        elif "send a whatsapp message" in query or "send a message on whatsapp" in query or "send a message" in query:
            speak("What is the recipent's phone number?")
            what_no = myCommand()
            speak("Sorry, please try again later. 😝😜")
            clear()

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak("Here's what I found on the web.")
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak(results)
        
            except:
                webbrowser.open('https://www.bing.com/')
                speak("Sorry, I am unable to help with that!" + " 🤐")





print('-----------------------------------------------------------------------------------------------------------')