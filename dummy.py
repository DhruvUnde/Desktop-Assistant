import pyttsx3  # pip install pyttsx3
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import requests as rq
import calendar
import math

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Boss")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon Boss")

    else:
        speak("Good evening Boss")

    speak("What should I do for you?")

def takeCommand():
    query  = input("You can type here>")

    return query


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'tell' or 'show' in query:
            if 'joke' in query:
                res = rq.get(
                    'https://icanhazdadjoke.com/',
                    headers={"Accept": "application/json"}
                )
                if res.status_code == rq.codes.ok:
                    speak(str(res.json()['joke']))

            elif 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("tell about by wikipedia", "")
                results = wikipedia.summary(query, sentences=4)
                speak("According to Wikipedia")
                speak(results)



            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Boss, the time is {strTime}")

            elif 'the date' in query:
                strdate = str(datetime.date.today())
                speak(f"Boss, today is {strdate}")

            elif 'calendar' in query:
                query = query.replace('show calendar', '')
                speak('tell the month')
                month = takeCommand()
                if 'jan' in month:
                    monthi = 1
                elif 'feb' in month:
                    monthi = 2
                elif 'mar' in month:
                    monthi = 3
                elif 'apr' in month:
                    monthi = 4
                elif 'may' in month:
                    monthi = 5
                elif 'jun' in month:
                    monthi = 6
                elif 'jul' in month:
                    monthi = 7
                elif 'aug' in month:
                    monthi = 8
                elif 'sep' in month:
                    monthi = 9
                elif 'oct' in month:
                    monthi = 10
                elif 'nov' in month:
                    monthi = 11
                elif 'dec' in month:
                    monthi = 12
                speak("Which year?")
                year = int(takeCommand())
                cal = calendar.month(year, monthi)
                speak(f"Here is calender of {month} of year {year}")
                print(cal)



        if "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("Hold on, I will show you where " + location + " is.")
            webbrowser.open(url="https://www.google.nl/maps/place/" + location + "/&amp;")

        if 'open' or 'start' in query:
            if 'visual studio code' in query:
                codePath = "C:\\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code"
                speak("Ok, Here is Visual Studio Code")
                os.startfile(codePath)

            elif 'pycharm' in query:
                codePath = "C:\\Program Files\JetBrains\PyCharm Community Edition 2020.1.1\bin\pycharm64"
                speak("Ok, Starting PyCharm Community Edition 2020.1.1 sixty four bit")
                os.startfile(codePath)

            elif 'python' in query:
                codePath = "C:\\Users\Admin\AppData\Local\Programs\Python\Python38-32\pythonharm co"
                speak("Ok, Opening Python 3.8 32-bit")
                os.startfile(codePath)

            elif 'youtube' in query:
                speak("Ok, Here is Youtube")
                webbrowser.open("youtube.com")

            elif 'google' in query:
                speak("Ok, Starting Google")
                webbrowser.open("google.com")

            elif 'stackoverflow' in query:
                speak("Ok, Opening Stack overflow")
                webbrowser.open("stackoverflow.com")

            elif 'quantum computer' in query:
                speak("Ok, Starting IBM Quantum Experience")
                webbrowser.open(url="https://quantum-computing.ibm.com")

            elif "mum's course" in query:
                speak("Starting Autie's course")
                webbrowser.open(url="https://learndigital.withgoogle.com/digitalunlocked/course/digital-marketing")
            elif 'qiskit' in query:
                speak("Alright, Starting Qiskit")
                webbrowser.open(url="https://qiskit.org")
            elif 'gmail' in  query:
                speak("Ok, Starting your Gmail!")
                webbrowser.open(url="https://mail.google.com/mail/u/0/#inbox")
            elif 'github' in query:
                speak("Which, Web or Desktop?")
                app = takeCommand()
                if app == 'desk':
                    codePath = "C:\\Users\Admin\AppData\Local\GitHubDesktop\GitHubDesktop"
                    speak("Starting Github desktop!")
                    os.startfile(codePath)
                elif app == 'web':
                    speak("Starting Github Web")
                    webbrowser.open(url="https://github.com")

        if 'play movie' in query:
            speak("Which type of movie?")
            moviej = takeCommand()
            if 'action' in moviej:
                speak("Which movie in this section")
                movie1 = takeCommand()
                if 'uri' in movie1:
                    movie_dir = 'E:\\Movies\Action'
                    movies = os.listdir(movie_dir)
                    os.startfile(os.path.join(movie_dir, movies[0]))
            elif 'drama' in moviej:
                speak("Which movie in this section")
                movie2 = takeCommand()
                if 'gully boy' in movie2:
                    movie_dir = 'E:\\Movies\Drama'
                    movies = os.listdir(movie_dir)
                    os.startfile(os.path.join(movie_dir, movies[0]))
                
                
        if 'thanks' in query:
            speak("Its my duty boss")

        if 'thank you' in query:
            speak('Why thanks for a laptop?')
            
        if 'funny' in query:
            speak("My sense of humour is in development!")
            
        if 'your name' in query:
            speak("I'm dummy a Virtual Reality Operating System or your Virtual Companian for making your life easy!")
        if 'not right' in query:
            speak("OK, Boss I will Improve")

        if 'calcu' in query:
            speak("I'm ready to calculate!")
            speak("Tell the operation")
            opr = takeCommand()
            if 'add' in opr:
                speak("What is the first number?")
                num1 = takeCommand()
                num1 = float(num1)
                speak("What is the second number?")
                num2 = takeCommand()
                num2 = float(num1)
                ans = float(num1 + num2)
                speak(f"Boss the answer is {ans}")
            elif 'sub' in opr:
                speak("What is the first number?")
                num1 = takeCommand()
                num1 = float(num1)
                speak("What is the second number?")
                num2 = takeCommand()
                num2 = float(num2)
                ans = float(num1 - num2)
                speak(f"Boss the answer is {ans}")
            elif 'mul' in opr:
                speak("What is the first number?")
                num1 = takeCommand()
                num1 = float(num1)
                speak("What is the second number?")
                num2 = takeCommand()
                num2 = float(num2)
                ans = float(num1 * num2)
                speak(f"Boss the answer is {ans}")
            elif 'div' in opr:
                speak("What is the first number?")
                num1 = takeCommand()
                num1 = float(num1)
                speak("What is the second number?")
                num2 = takeCommand()
                num2 = float(num2)
                ans = float(num1 / num2)
                speak(f"Boss the answer is {ans}")
            elif 'expo' in opr:
                speak("What is the base number?")
                num1 = int(takeCommand())
                num1 = float(num1)
                speak("What is the index number?")
                num2 = takeCommand()
                num2 = float(num2)
                ans = float(num1 ** num2)
                speak(f"Boss the answer is {ans}")
            elif 'square root' in opr:
                speak("What is the number?")
                num1 = takeCommand()
                num1 = float(num1)
                ans = math.sqrt(num1)
                speak(f"Boss the answer is {ans}")
            elif 'area' in opr:
                speak("of which shape?")
                ar = takeCommand()            
                if 'square' in ar:
                    speak("Tell the side")
                    s = takeCommand()
                    s = float(s)
                    ans = float(s ** 2)
                    speak(f"Boss area of the square is {ans}units")
                elif 'circle' in ar:
                    speak("Tell radius")
                    s = takeCommand()
                    s = float(s)
                    ans = float((math.pi) * (s ** 2))
                    speak(f"Boss the area of the circle is {ans}units")
                elif 'triangle' in ar:
                    speak("Tell height side")
                    sf = takeCommand()
                    sf = float(sf)
                    speak("Tell base side")
                    ss = takeCommand()
                    ss = float(ss)
                    ans = float(0.5 * sf * ss)
                    speak(f"Boss the area of the triangle is {ans}units")
