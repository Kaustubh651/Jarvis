from traceback import print_tb
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[4].id)
engine.setProperty('voice',voices[5].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning sir! and wish u a good day ahead")
    elif hour>=12 and hour<16:
        speak("good afternoon! hope u had a good food in afternoon")
    elif hour>16 and hour <=20 :
        speak("good evening kaustubh")
    else:
        speak("hello kaustubh ")
    speak('i am lucifer sir ,i am ready for your command')

def takeCommand():
    #it take microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_thershold=1
        audio=r.listen(source)

        try:
            print("Recongnixe..")
            query=r.recognize_google(audio)
            audio=r.listen(source)
            print(f"User said:{query}\n")
        except Exception as e:
            print(e)
            print("please say it again")
            return "None "
        return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("shrutij@student.iul.ac.in","kaust651@")
    server.sendmail("youremail@gmail.com",to,content)







        
if __name__=="__main__":
    wishMe()
    while True:
        query= takeCommand().lower()

        #logic for executing taks based on query
        if "wikipedia" in query:
            speak("Searching wikipedia..")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open netflix" in query:
            webbrowser.open("https://www.netflix.com/browse")
        elif "play music" in query:
            music_dir='C:\\Users\\kaustubh\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))
        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir ji,the tume is{strTime}")
        elif " open spotify" in query:
            webbrowser.open("https://open.spotify.com/?_gl=1*vxr4df*_gcl_aw*R0NMLjE2NDM2NDQxMzcuQ2owS0NRaUFydDZQQmhDb0FSSXNBTUY1d2FnaTQ0Qk9JUnVsdHRjZk0tR2NqZnlHZ0s3OU5GUlh5Z3BjcHRrb3FpV0liWVJkbTRTSjZib2FBc1RKRUFMd193Y0I.*_gcl_dc*R0NMLjE2NDM2NDQxMzcuQ2owS0NRaUFydDZQQmhDb0FSSXNBTUY1d2FnaTQ0Qk9JUnVsdHRjZk0tR2NqZnlHZ0s3OU5GUlh5Z3BjcHRrb3FpV0liWVJkbTRTSjZib2FBc1RKRUFMd193Y0I.&_ga=2.101663491.306076404.1643644137-819778465.1639628859&_gac=1.262708734.1643644140.Cj0KCQiArt6PBhCoARIsAMF5wagi44BOIRulttcfM-GcjfyGgK79NFRXygpcptkoqiWIbYRdm4SJ6boaAsTJEALw_wcB")
        elif "open whatapp" in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif "open code" in query:
            code_path="C:\\sers\\kaustubh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif "email to king" in query:
            try:
                speak("what should i write")
                content= takeCommand()
                to="testing.work651@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry bhaiya i lucifer wasnit able to sent the email")













            
