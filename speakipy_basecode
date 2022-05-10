import pyttsx3 #converting speech to text
import webbrowser #for web data accessing
import os #for accesing local files
import datetime #for keeping track of time
import speech_recognition as sr #for recognising speech
import pygame as pg#for main mic design
import time as t
import wikipedia
import random
from tkinter import *
from tkinter import messagebox as ms
import sqlite3

import pandas as pd
DF=pd.read_csv("speakipy.csv")
History={}
Name=[]
Com=[]


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)  # set the audio of voice assistant as zera
rate = engine.getProperty('rate')  # Go to Start Search for Microphone Setup
newrate = 130  # You will find  David as default voice
engine.setProperty('rate', newrate)  # We have encapsulated Hari with David's Voice
#@@@FOR ENGINE SETUP@@@

def speak(audio):
    engine.say(audio)  # Here is a function  to intake audio
    engine.runAndWait()
#@@@TO PROMPT USER TO SPEAK

def recognise():
    try:
        IN = sr.Recognizer()
        with sr.Microphone() as s:
            print("Listning.....")
            IN.non_speaking_duration=0.6
            au=IN.listen(s)
            print("Recognising......")
        audio=IN.recognize_google(au)
        return str(audio)
    except Exception as e:
        # print(e)
        print("Sir I was unable to hear you Please Say again")  # if there occurs some exception It will ask to
        speak("Sir I was unable to hear you ")
        return " Touch mic and Please Say again"# Speak Again

#@@@PACKAGES USED@@@

pg.init()
def launch():

    pg.init()
    pg.display.set_caption("Loading....")
    surface=pg.display.set_mode((1366,700))
    launch_Image=pg.image.load('Speakipylaunch.png')
    surface.blit(launch_Image,(0,0))
    pg.display.update()
    t.sleep(5)
    pg.display.set_caption("Welcome to Speakipy!!")
#function for launching screen

def mainmic():
    History=[]
    pg.init()
    pg.display.set_caption("Your Desktop Voice Assistant!")
    base_surface=pg.display.set_mode((260,280))
    image1=pg.image.load('mic1')
    base_surface.blit(image1,(0,0))
    pg.display.update()
#after launching if login is successfull the mic will be displayed!!!

######

launch()
t.sleep(10)

def wishMe():
    print("Executable Voice Commands are: >>>> \n 1.time\n 2.Chrome\n 3.Notepad\n4.Wikipidea"
          "\n5.Google and its products\n6.Youtube\n7.Play Game\n 8.Udemy\n9.Dev C++\n10.Read a text File\n11.Greating User\n12.Exit\n")
    print("Touch mic to Say in commands...")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!!")  # This Function  is to greet the  Owner  as per System Time
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !!!")  # We can dyanamically modify as per requirements
    elif hour >= 18 and hour < 22:
        speak("Good Evening !")
    else:
        speak("Sir!! It's beyond 10pm We must Sleep")
    speak("I am Zira. How may I help You")

# Python Tkinter and Sqlite3 Login Form

with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEX NOT NULL);')
db.commit()
db.close()



class main:
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()


    def login(self):

        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            Name=self.username.get()
            self.head['text'] = Name + '\n Logged In'
            self.head['pady'] = 100
            mainmic()
            root.destroy()
            wishMe()
            speak("Hi..."+Name+"Welcome to Speakipy...")
            #t.sleep(5)

        else:
            ms.showerror('Oops!', 'Username Not Found.')


    def new_user(self):
        # Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user, [(self.n_username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            N=self.n_username.get().join(".txt")

            F=open(N,"w+")
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()


    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 100), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=50, pady=100)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2,
                                                                                                         column=1)


#if __name__ == '__main__':

root = Tk()
root.title('Login Page')
main(root)
root.mainloop()







#mainmic()
#@@@FOR MIC DISPLAY@@@


        #speakmic()
#@@@TO RECOGNIZE THE SPEECH AND RETURN IT IN STRING FORM@@@

N=input("Enter Your Name\n")
#@@@FOR GREETING THE USER@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def speakmic():
    pg.init()
    #ONCE LOGIN IS SUCCESSFULL SPEAK MIC IS EXECUTED AND USER CAN USE THE SOFTWARE
    while True:

        for event in pg.event.get():
            pg.init()
            if event.type==pg.QUIT:
                pg.quit()
                quit()

            if event.type in [pg.MOUSEBUTTONDOWN or pg.MOUSEBUTTONUP]:
                #base_surface.blit(image1,(0,0))
                speak("Your command please...")
                print("Your Command Please...")
                if event.type==pg.MOUSEBUTTONDOWN:
                    messageRead=recognise()

                    if 'time' in messageRead.lower():
                        Name.append(N)
                        Com.append(messageRead.lower())
                        print(messageRead)
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"The time is {strTime}")
                        continue
                    if "history" in messageRead.lower():
                        Name.append(N)
                        Com.append(messageRead.lower())
                        History["User"]=Name
                        History["Commands"]=Com
                        print("Procesing....")
                        H=pd.DataFrame(History)
                        H.to_csv('speakipy.csv',mode='a',header=False)
                        speak("Fetching Your Data...")
                        print("Fetching Your Data...")
                        print("\n================================================\n")
                        for i in range(H.index.stop):
                            if H.User[i]==N:
                                print(H.Commands[i])
                        print("\n================================================\n")
                        print("Fetched!!")
                    if 'notepad' in messageRead.lower():
                        Name.append(N)
                        Com.append(messageRead.lower())
                        speak("Opening Notepad for You...")
                        os.startfile("C:\\Users\\Sahil\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad")
                        speak("opened notepad!!")
                    if 'exit' in messageRead.lower():
                        print(messageRead)

                        speak("Thank You For Using Speakipy...")
                        speak("Have a good day...")
                        quit()
                    if 'chrome' in messageRead.lower():

                        Name.append(N)
                        Com.append(messageRead.lower())
                        speak("opening google chrome for You!!")
                        webbrowser.open("‪C:\\Users\\Public\\Desktop\\Google Chrome.lnk")
                        speak("Opened Chrome..!")
                    if 'wikipedia' in messageRead.lower():
                        speak('Searching Wikipedia...')  # Surf to Wikipedia
                        messageRead = messageRead.lower().replace("wikipedia", "")
                        results = wikipedia.summary(messageRead.lower(), sentences=5)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                    if 'youtube' in messageRead.lower():
                        Name.append(N)
                        Com.append(messageRead.lower())
                        speak("Opening YouTube For You.")
                        webbrowser.open("https://www.youtube.com/")
                        speak("opened Youtube!!")
                    if 'google' in messageRead.lower():
                        Name.append(N)
                        Com.append(messageRead.lower())
                        # Browse to google Services
                        if 'maps' in messageRead.lower():
                            speak("Opening Google Maps For you.")
                            webbrowser.open("https://www.google.co.in/maps/")
                            speak("Google maps opened...")
                            print("Sleeping for 10 Sec...")
                            t.sleep(10)
                        elif 'drive' in messageRead.lower():
                            speak("Opening Google Drive for you.")
                            webbrowser.open("https://drive.google.com/drive/")
                            speak("Google drive Opened...")
                        elif 'translate' in messageRead.lower():
                            speak("Opening Google translate for you.")
                            webbrowser.open("https://translate.google.co.in/")
                            speak('Google translate opened...')
                        else:
                            speak("Opening Google for you.")
                            webbrowser.open("https://www.google.co.in/")
                            speak('Opened Google..')
                    elif "play music" in messageRead.lower():
                        Name.append(N)
                        Com.append(messageRead.lower())
                        song_dir = "E:\MY MUSIC"  # HERE U SPECIFY UR DRIVE DETAILES
                        SONGS = os.listdir(song_dir)  # HERE U SPECIFY UR SONGS FOLDER INSIDE THE ROUND BRACE::::::
                        speak("Playing for You...")
                        os.startfile(os.path.join(song_dir, SONGS[random.randrange(0, 15)]))
                        speak('NEXT COMMAND PLEASE')
                        Q7=input("Next command please...(y/n)\n")
                        if Q7=='y':
                            continue
                        else:
                            break
                    elif 'udemy' in messageRead.lower():
                        Name.append(N)
                        Com.append(messageRead.lower())
                        speak("Opening Udemy for You")
                        webbrowser.open("https://www.udemy.com/")
                        speak('Opened Udemy..')
                    elif 'thank you' in messageRead.lower():
                        Name.append(N)
                        Com.append(messageRead.lower())
                        speak("You are Most Welcome It's my Honor.")  # Thank You
                        sr.non_speaking_duration=0.6
                    elif 'open dev c' in messageRead.lower():
                        Name.append(N)
                        Com.append(messageRead.lower())
                        # Open System Applications
                        codePath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
                        os.startfile(codePath)
                        speak("Opened Developer C")
                    elif 'file' in messageRead.lower():
                        Name.append(N)
                        Com.append(messageRead.lower())
                        INF = input("Enter/paste the file path\n")
                        with open(INF, 'r') as f:
                            R = f.readlines()
                            for i in R:
                               speak(i)
                        speak("File is read completely...")

                    elif 'game' in messageRead.lower():
                        Name.append(N)
                        Com.append(messageRead.lower())
                        speak("Don't try to Quit before you end the game..!")
                        print("Don't try to Quit before you end the game..!")
                        import app
                        speak("Well Played..!!")
                        mainmic()
                    if 'amazon' in messageRead.lower():
                        Name.append(N)
                        Com.append(messageRead.lower())
                        speak("Opening amazon For You..")
                        webbrowser.open("https://www.amazon.in/")
                        speak("opened Amazon!!")
                    else:
                        #speak("This command isn't trained...")
                        continue
#MANY ADDITIONAL FEATURES CAN BE ADDED.......
speakmic()

###Code for retrival of data
