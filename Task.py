import datetime
from Speak import Say
import wikipedia
import pywhatkit
import os
import webbrowser as web
import wolframalpha
import pywikihow
from bs4 import BeautifulSoup
import googletrans
from Listen import ListenHindi, Listen
import requests
import json
import pyjokes
from OnlineClassLink import OnlineClassLink
from time import sleep
from pyautogui import click
from keyboard import press_and_release
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import psutil
import opeartor
import pyautogui

def Time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    Say(f"The time is now {time}")

def Date():
    date = datetime.date.today()
    Say(date)

def Wikipedia(query):
    name = str(query).replace("", "")
    try:
        result = wikipedia.summary(name, 4)
        Say(f"According to Wikipedia: {result}")
    except wikipedia.PageError:
        pass
    except wikipedia.exceptions.WikipediaException:
        pass

def CoronaVirus(Country):
    countries = str(Country).replace(" ", "")
    url = f"https://worldometers.info/coronavirus/country/{countries}"
    result = requests.get(url)
    soups = BeautifulSoup(result.text, 'lxml')
    corona = soups.find_all('div', class_='maincounter-number')
    Data = []
    for case in corona:
        span = case.find('span')
        Data.append(span.string)

    cases, Death, recovered = Data
    Say(f"Cases: {cases}")
    Say(f"Deaths: {Death}")
    Say(f"Recovered: {recovered}")

def CloseApps(app_name):
    if 'youtube' in app_name:
        os.system("taskkill /f /im chrome.exe")
    
    elif 'chrome' in app_name:
        os.system("taskkill /f /im chrome.exe")
    
    elif 'notepad' in app_name:
        os.system("taskkill /f /im notepad.exe")
    
    elif 'facebook' in app_name:
        os.system("taskkill /f /im chrome.exe")
    
    elif 'code' in app_name:
        os.system("taskkill /f /im code.exe")
    
    elif 'edge' in app_name:
        os.system("taskkill /f /im edge.exe")

    elif 'comand prompt' in app_name:
        os.system("taskkill /f /im cmd.exe")

    elif 'torrent' in app_name:
        os.system("taskkill /f /im torrent.exe")
    

def NonInputExecution(query):
    query = str(query)
    
    if 'time' in query:
        Time()

    elif 'date' in query:
        Date()

    elif "temperature" in query:
        f = open("WolFramAlpha.txt", "r")
        app_id = f.read()
        cli = wolframalpha.Client(app_id)
        respone = cli.query('temperature of kolkata')
        temp = next(respone.results).text
        Say(f"The temperature of Kolkata is: {temp}")

    elif "ip" in query:
        r = requests.get("https://api.ipify.org")
        ip = r.text
        Say(f"Sir, your ip address is {ip}")

    elif "whatsapp" in query:
        Say("Tell me the phone number you want to send to")
        phone_no = str(input("Enter the phone number: "))
        Say("What should i send")
        msg = Listen()
        pywhatkit.sendwhatmsg_instantly(phone_no, msg, 20)

    elif "news" in query:
        Say("Wait sir, fetching the latest news of India")
        url = 'https://newsapi.org/v2/top-headlines?' + 'country=in&' + 'apiKey=6e073a999f094d43887922367d55d817'

        try:
            response = requests.get(url)
        except:
            pass

        news = json.loads(response.text)

        for new in news['articles']:
            Say(f"Title: {str(new['title'])}")
            Say(f"Description: {str(new['description'])}")
    elif "joke" in query:
        joke = pyjokes.get_joke()
        Say(f"Here's My Joke: {joke}")

    elif 'online' in query:
        Say("Ok sir, i am joining your online class, please do nothing")
        Link = OnlineClassLink()
        web.open(Link)
        sleep(10)
        press_and_release("ctrl + d")
        sleep(3)
        press_and_release("ctrl + e")
        sleep(3)
        click(x=1346, y=649)
        pyautogui.press('f11')
    elif 'battery' in query:
        battery = psutil.sensors_battery()
        percentage = int(battery.percent)
        Say(f"Sir, we have {percentage} percent battery left with us")
        if percentage >=75:
            Say("We have enough power to continue work, but sir, if u want to play games, i would suggest that plug the charger.")
        elif percentage>=40 and percentage<=75:
            Say("Sir, you should plug your charger!")
        elif percentage>=15 and percentage<=30:
            Say("We dont have enough power to work, please connect to the charger")
        elif percentage<=15:
            Say("Sir, we have very low power, please connect to the charger")
    elif 'calculate' in query:
        Say("Sir, what should i calculate, for example: 3 plus 3 or any equation")
        my_string = Listen()
        f = open("WolFramAlpha.txt", "r")
        app_id = f.read()
        cli = wolframalpha.Client(app_id)
        respone = cli.query(my_string)
        temp = next(respone.results).text
        Say(f"Sir the result is: {temp}")
    elif "sleep" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "shut down" in query:
        os.system("shutdown /s /t 5")
    elif "restart" in query:
        os.system("shutdown /r /t 5")

def WhatsappCall(name):
    Say("Ok sir, I am Calling In Whatsapp")
    # Opening Whatsapp
    pyautogui.press('win')
    pyautogui.write('Whatsapp')
    pyautogui.press('enter')

    sleep(20)

    # Search for the name
    pyautogui.click(x=272, y=135)
    pyautogui.write(name)
    pyautogui.press('enter')

    # Click on the call button
    pyautogui.click(x=1725, y=72)
    Say("Done Sir!")


def OpenApps(app_name):
    if 'youtube' in app_name:
        web.open("youtube.com")
    elif 'stackoverflow' in app_name:
        web.open("stackoverflow.com")
    elif 'instagarm' in app_name:
        web.open("instagram.com")
    elif 'facebook' in app_name:
        web.open("facebook.com")
    elif 'code' in app_name:
        os.startfile("C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    elif 'chrome' in app_name:
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    elif 'torrent' in app_name:
        os.startfile("C:\\Users\\ASUS\\AppData\\Roaming\\uTorrent\\uTorrent.exe")
    elif 'notepad' in app_name:
        os.system("start notepad")
    elif "command prompt" in app_name:
        os.system("start cmd")
    elif "edge" in app_name:
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

def InputExecution(tag, query):
    if "wikipedia" in tag:
        Wikipedia(str(query).replace("wikipedia", "").replace("who is", "").replace("what is", "").replace("about", ""))
    
    elif "google" in tag:
        search = str(query).replace("google search", "").replace("search", "")
        pywhatkit.search(search)
    
    elif "youtube" in tag:
        music = str(query).replace("play", "").replace("song", "")
        pywhatkit.playonyt(music)

    elif "apps" in tag:
        app = str(query).replace("open", "").replace("launch", "").replace("start", "")
        OpenApps(app)

    elif "how to" in tag:
        max_results = 1
        how_tos = pywikihow.search_wikihow(query, max_results)
        assert len(how_tos) == 1
        how_tos[0].print()
        Say(how_tos[0].summary)

    elif "corona" in tag:
        c = str(query).replace("corona", "")
        CoronaVirus(c)

    elif "trans" in tag:
        Say("What should i translate")
        line = ListenHindi()
        translate = googletrans.Translator()
        result = translate.translate(line)
        Text = result.text
        Say(f"The translation for this line is: {Text}")

    elif "location" in tag:
        Say("Wait sir, let me check")
        ip_add = requests.get("https://api.ipify.org").text
        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_q = requests.get(url)
        geo_d = geo_q.json()
        state = geo_d['region']
        city = geo_d['city']
        country = geo_d['country']
        Say(f"Sir, you are in {city} city of {state} state of {country} country")
    elif "where is" in tag:
        Place = str(query).replace("where is", "").replace("distance of", "")
        Url_Place = f"https://google.com/maps/place/{Place}"
        geolocater = Nominatim(user_agent="myGeocoder")
        location = geolocater.geocode(Place, addressdetails=True)
        target_latlon = location.latitude, location.longitude
        location = location.raw['address']
        target = {'city': location.get('city', ''), 'state': location.get('state', ''), 'country': location.get('country', '')}
        current_loca = geocoder.ip('me')
        current_latlon = current_loca.latlng
        distance = str(great_circle(current_latlon, target_latlon))
        distance = str(distance.split(' ', 1)[0])
        distance = round(float(distance), 2)
        web.open(Url_Place)
        Say(target)
        Say(f"Sir, {Place} is {distance} kilometre away from your location")
    elif "close" in tag:
        app_name = str(query).replace("close", "").replace(" app", "").replace(" ", "")
        CloseApps(app_name)
    elif "call" in tag:
        name = str(query).replace("call", "").replace(" to", "").replace(" ", "")
        WhatsappCall(name)