from __future__ import print_function
import datetime
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import speech_recognition as sr
import os
import re
import threading
import win32api
from time import sleep
import pyttsx3
import pyautogui
from playsound import playsound
import webbrowser
from subprocess import call
import random 
import time
import wikipedia
import datetime
from google import google
import pytz
import datetime
import time
#import detect
import subprocess
import wolframalpha
#import cv2
import lookup_file_system_events
import ctypes
from google.cloud import translate
from pynput.keyboard import Key, Controller
keyboard = Controller()
client = wolframalpha.Client('ENTER YOUR OWN API KEY')
#mouse_work()
#translate_client = translate.TranslationServiceClient()
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october","november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]
greeting_dict = { "hello", "hi"}
open_launch_dict = {"Open": "open", "Launch":"launch"}
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which', 'how': 'how'}
youtube_search_dict = {'search': 'search'}
social_media_dict = {"facebook":"https://www.facebook.com", "twitter":"https://www.twitter.com", "gmail":"https://www.gmail.com", "google":"https://www.google.com", "instagram":"https://instagram.com", "chrome":"https://www.google.com", "youtube":"https://www.youtube.com"}
thankyou_dict = {"thanks": "thanks", "thank you": "thank you"}
goodbye_dict = {"goodbye": "goodbye", "by": "by", "bye": "bye"}
BYE = ["you may take a leave" , "please leave", "get lost", "take a leave", "take leave", "you may take a leave"]
play_music = ['play music']
sublime_dict = ["open sublime"]
calci = ["open calculator", " launch calculator", "open the calculator", "launch the calculator"]
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
joke_dict = ["tell me a joke", "tell a joke", "tell me something funny", "one more joke", ]
INFO = ['tell me about']
COPY_SAVE = ['copy', 'save', 'notepad']
COPY = {"copy": "copy"}
SAVE_WORD = ['save', 'it', 'as']
MAXIMIZE = ["maximize", "make it large", "maximise"]
MINIMIZE = ["minimize", "make it small", "minimise"]
YOUTUBE_SEARCH = ['open youtube and search', 'search on youtube']	
youtube_dict = ["open youtube", "search on youtube", "turn on youtube mode", "open youtube friday", "friday open youtube", "friday search on youtube"]
CALENDAR_STRS = ["any meetings", "what do i have", "am i busy", "am i avaliable", "do i have plans", "check for the meetings", "check if i have mettings", "do i have meetings", "do i have any events", "do i have anything", "check if i am free on"]
NOTE_STRS = ["make a note", "note it out", "write this down", "remember this"]
HELP_STRS = ["i need your help", "help me", "i am facing a problem buddy", "facing a problem", "i am stuck"]
help_speak = ["how can i help you sir"]
WAKE = ["wake up", "get up", "time to work", "uth jao", "urja", "utha jao", "utho"]
Wake_REPLY = ["always at your service sir", "always ready to help you", "i am there for you", "online sir", "all set for you"]
SLEEP = ["sleep", "go to sleep"]
CMD = ["open cmd", "open command prompt"]
SAVE = ["save"]
SEARCH = ['friday search']
DELETE = ["delete", "destroy"]
WOLFRAMCMD = ["calculate", "joule", "newton", "news", "weather"]
SCREENSHOT = ["take a screenshot", "take screenshot", "screenshot this"]
SCREENSHOT_REPLY = ["done", "done sir", "ok sir"]
CLOSE = ['close tab', 'close tabs', 'close', 'close window']
notepad_dict = ["open notepad", "launch notepad"]
wordpad_dict = ["open wordpad", "launch wordpad"]
switch_window = ["switch window", "switch tab", "swap"]
restart = ["restart", "reboot"]
shut_down = ["kill power", "power of", "power off", "shutdown", "log of", "log off"]
mp3_goodbye_list = ['friday\goodbye.mp3']
mp3_thankyou_list = ['friday\hankyou_1.mp3', 'friday\hank_2.mp3']
mp3_listening_problem_list = ['friday\listening_problem_1.mp3', 'friday\listening_problem_2.mp3']
mp3_struggling_list = ['friday\struggling_1.mp3']
mp3_google_search = ['friday\google_search_1.mp3','friday\google_search_2.mp3']
mp3_greeting_list =['friday\greeting_accept.mp3', 'friday\greeting_accept_2.mp3']
mp3_open_launch_list = ['friday\open_1.mp3','friday\open_2.mp3']
mp3_youtube_search = ("what would you like to search sir", "What should i search for sir")
error_occurrence = 0
counter = 0
working_counter = 0
False_count = 0
count = 0
countt = 0
copysave = 0
delete_count = 0
search_count = 0
try:
	engine = pyttsx3.init()
except ImportError:
    print('Requested driver is not found')	
except RuntimeError:
	print('Driver fails to initialize')

voices = engine.getProperty('voices')
#for voice in voices:
#	print(voice.id)
#	break
#exit()
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MS-Anna-1033-20-DSK')
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 130)
def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service
def get_events(day, service):
    # Call the Calendar API
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        speak_text_cmd('No upcoming events found.')
    else:
        speak_text_cmd(f"You have {len(events)} events on this day.")

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            if int(start_time.split(":")[0]) < 12:
                start_time = start_time + "am"
            else:
                start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
                start_time = start_time + "pm"
            speak_text_cmd(event["summary"] + " at " + start_time)
def speak_text_cmd(cmd):
	engine.say(cmd)
	engine.runAndWait()
def google_search_result(query):  
    global counter
    search_result = google.search(query)
    #print(search_result)
    for result in search_result:
            play_sound(mp3_google_search)
            print(result.description.replace('...', '').rsplit('.', 3)[0])
            speak_text_cmd(result.description.replace('...', '').rsplit('.', 3)[0])
            break
def is_valid_google_search(phrase):
	if(google_searches_dict.get(phrase.split(' ')[0])==phrase.split(' ')[0]):
		return True
def get_index(text):
    if 'first' in text:
        return 0
    elif 'second' in text:
        return 1
    elif 'third' in text:
        return 2
    else:
        return None
def alt_tab1():
	keyboard.press(Key.alt)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.release(Key.alt)

def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)

def read_voice_cmd():
	speech = sr.Recognizer()
	voice_text = ""
	print('Listening..')
	global error_occurrence
	#global wake_check
	try:
		with sr.Microphone()as source:
			audio = speech.listen(source=source,timeout=10,phrase_time_limit=10)
		voice_text = speech.recognize_google(audio, language='en-in')
	except sr.UnknownValueError:
		if error_occurrence == 0:
			play_sound(mp3_listening_problem_list)
			#print("Unknown VAlue Error")
			#wake()
			error_occurrence += 1
		elif error_occurrence == 1:
			play_sound(mp3_struggling_list)
			error_occurrence += 1
	except sr.RequestError as e:
		print('Network Error')
		engine.say('Network Error Sir')
		engine.runAndWait()
	except sr.WaitTimeoutError:
		if error_occurrence==0:
			play_sound(mp3_listening_problem_list)
			error_occurrence += 1
		elif error_occurrence == 1:
			play_sound(mp3_struggling_list)
			error_occurrence+=1	
		
	return voice_text
def maximize():
	pyautogui.keyDown('win')
	keyboard.press(Key.up)
	pyautogui.keyUp('win')
def minimize():
	pyautogui.keyDown('win')
	keyboard.press(Key.down)
	pyautogui.keyUp('win')
def delete():
	global delete_count
	keyboard.press(Key.shift)
	keyboard.press(Key.delete)
	while True:
		delete_count += 1
		if delete_count >= 200000:
			keyboard.release(Key.shift)
			keyboard.release(Key.delete)
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
			break
		
def wake():
	voice_note = read_voice_cmd().lower()
	if voice_note is WAKE:
		print("Found")
def save():
	pyautogui.hotkey("ctrlleft", "s")
def closetabs():
	pyautogui.hotkey("ctrlleft", "w")
def close():
	pyautogui.hotkey("alt", "f4")
def get_date(text):
    text = voice_note.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    # THE NEW PART STARTS HERE
    if month < today.month and month != -1:  # if the month mentioned is before the current month set the year to the next
        year = year+1

    # This is slighlty different from the video but the correct version
    if month == -1 and day != -1:  # if we didn't find a month, but we have a day
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    # if we only found a dta of the week
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:  
        return datetime.date(month=month, day=day, year=year)

def note(text):
	date = datetime.datetime.now()
	file_name = str(date).replace(":", "-") + "-note.txt"
	with open(file_name, "w") as f:
		f.write(text)
	subprocess.Popen(["notepad.exe", file_name])

def is_valid_note(greet_dict, voice_note):
	for key, value in greet_dict.items():
		#'hello Friday
		#'hi Friday
		try: 
			if value == voice_note.split(' ')[0]:
				return True
				break
			elif key == voice_note.split(' ')[1]:
				return True
				break
		except IndexError:
			pass
	return False
def getperson(text):
	wordlist = text.split()
	for i in range(0, len(wordlist)):
		if i +3<= len(wordlist)	-1 and wordlist[i].lower() == 'who' and wordlist[i+1].lower() == 'is':
			return wordlist[i + 2] +' ' + wordlist[i+3] +' ' + wordlist[i+4]
def workingcounter():
	while True:
		global working_counter
		working_counter += 1
		if working_counter == 3:
			speak_text_cmd("You Have Been Working")
			print("You Have Been Working")
			#break
		break
def search(text):
	text = voice_note
	word = 'search'
	res = re.sub("[^\w]", " ", voice_note).split() 
	res = res.index(word) + 1
	print(str(res))
	res = voice_note.split(' ', res)[res] 
	print("hello World")
	return res
def youtubesearch(text):
	
  #print(voice_note)
	voice_note = text
	words ='search'
	wrd2 = 'on'
	wrd1 = 'youtube'
	try:
		if wrd1 and words in voice_note:
			res = re.sub("[^\w]", " ", voice_note).split() 
			res =  res.index(wrd2) and res.index(wrd1) + 1
			print(str(res))
			res = voice_note.split(' ', res)[res] 
			#print("hello World")
			return res
	except ValueError:
		#return voice_note
		pass                           	
	try:
		if words in voice_note:
			res = re.sub("[^\w]", " ", voice_note).split() 
			res = res.index(words) + 1
			print(str(res))
			res = voice_note.split(' ', res)[res] 
			#print("hello World")
			return res
	except ValueError:
		#return voice_note
		pass
 
if __name__ == "__main__":
	print(          
				" ███████║ █████║  ║█████║   ███║      ║███║   ║█    █║\n"
	            " █║       █   █║    ║█║     ║  ██║   ║██  ██║  ║█  █║\n"
	            " ████║    ████║     ║█║     ║   ██║  ║█    █║   ║██║\n"
	            " █║       █   █║    ║█║     ║   ██║  ║█════█║   ║█║\n"
	            " █║       █   ██║ ║█████║   ████║    ║█    █║   ║█║" 
                
	             )
	
	
	speak_text_cmd("Please Wait. System Initializing")
	speak_text_cmd("Loading Disk. Initializing Security Setup ")
	speak_text_cmd("Launching User Interface                     ")
	speak_text_cmd("System Initialize Launching system         ")
	playsound('friday\greeting.mp3')
	
	while True:
                        
		voice_note = read_voice_cmd().lower()
		 
		print('cmd: {}'.format(voice_note))

		#SERVICE = authenticate_google()
		if error_occurrence >= 6:
			while True:
				print("In Sleepp...")
				#voice_note = read_voice_cmd().lower()
				for phrase in WAKE:
					if phrase in voice_note:
						error_occurrence =  0
						wake_prompt = random.choice(Wake_REPLY)
						speak_text_cmd(wake_prompt)
						print("Waked...")
						break
					
				break
			continue

		
		
		for phrase in voice_note.split():
			if phrase.lower() in greeting_dict:
				print("In Greeting...")
				play_sound(mp3_greeting_list)
		if 'who is' in voice_note:
			person = getperson(voice_note)
			print(person)
			wiki = wikipedia.summary(person, sentences=2)
			speak_text_cmd(wiki)
		for phrase in CALENDAR_STRS:
			if phrase in voice_note:
				date = 	get_date(speak_text_cmd)
				if date:
					get_events(date, SERVICE)
				else:
					speak_text_cmd("Please Try Again")
					print("Please Try Again")
			continue
		for phrase in voice_note:
			if phrase in NOTE_STRS:
				speak_text_cmd("what would you like me to write down")
				note_text = read_voice_cmd().lower()
				note(note_text)
				speak_text_cmd("I've made a note of that.")
		for phrase in COPY_SAVE:
			if phrase in voice_note:
				if phrase in voice_note.split():
					copysave +=1
					if copysave == 2:
						voice_note.join(' ')
						pyautogui.hotkey("ctrlleft", "a")
						pyautogui.hotkey("ctrlleft", "c")
						speak_text_cmd("What should i save. It as Sir")
						voice_note = read_voice_cmd().lower()
						#voice_note = ('save it as imp')
						#voice_note.split()
						voice_note = voice_note.replace('save it as', '')
						voice_note = voice_note.replace('save as', '')
						file_name = ('{}'.format(voice_note)) + ".txt"
						print(file_name)
						with open(file_name, "w") as f:
							f.write(' ')
						#    f.write(text)
						#call(["notepad.exe", file_name])
						subprocess.Popen(["notepad.exe", file_name])
						#os.startfile('C:/Windows/System32/notepad.exe')
						while True:
							copysave += 1
							if copysave > 2000000*3:
								pyautogui.hotkey("ctrlleft", "v")
								pyautogui.hotkey("ctrlleft", "s")
								pyautogui.hotkey("alt", "f4")
								#exit()
								break
							#pyautogui.hotkey("alt", "f4")
     
		for phrase in YOUTUBE_SEARCH:
			if phrase in voice_note:
				while True:
					print("Ok Sir")
					speak_text_cmd("Ok Sir ")
					#voice_note = voice_note.replace('open youtube and search', '').replace('search on youtube', '').replace('on youtube', '').replace('search youtube', '').replace('youtube search', '')
					you = youtubesearch(voice_note)
					print(you)
					if you is None:
						print("None Type Error. Maybe you should check your program")
						speak_text_cmd("None Type Error. Maybe you should check your program")
					else:
						webbrowser.open('https://www.youtube.com/results?search_query={}'.format(you))
						break
				continue
		for phrase in SEARCH:
			if phrase in voice_note:
				you = search(voice_note)
				print(you)
				while True:
					speak_text_cmd("Where Should I search Sir?")
					voice_note = read_voice_cmd().lower()
					search_count += 1
					if 'google' in voice_note:
						webbrowser.open('https://www.google.co.in/search?q={}'.format(you))
						break
					if 'youtube' in voice_note:
						webbrowser.open('https://www.youtube.com/results?search_query={}'.format(you))
						break
					elif search_count >= 3:
						speak_text_cmd("No Command Received")
						break
		for phrase in CMD:
			if phrase in voice_note:
				os.startfile('C:/Windows/System32/cmd.exe')
		for phrase in MAXIMIZE:
			if phrase in voice_note:
				maximize()
				reply = random.choice(SCREENSHOT_REPLY)
				print(reply)
				speak_text_cmd(reply)
		for phrase in MINIMIZE:
			if phrase in voice_note:
				minimize()
				reply = random.choice(SCREENSHOT_REPLY)
				print(reply)
				speak_text_cmd(reply)
		if "time" in voice_note:
			strTime = datetime.datetime.now().strftime("%H:%M:%S") 
			speak_text_cmd(f"Sir, the time is {strTime}")
		for phrase in CLOSE:
			if phrase in voice_note:
				if 'close tab' in voice_note:
					closetabs()
				else:
					close()
		for phrase in HELP_STRS:
			if phrase in voice_note:
				speak_text_cmd(help_speak)
				voice_note = read_voice_cmd().lower()
		for phrase in DELETE:
			if phrase in voice_note:
				while True:
					#global delete_count
					print("Are you sure sir")
					speak_text_cmd("Are you sure sir")
					delete_count += 1
					voice_note = read_voice_cmd().lower()
					if 'yes' in voice_note:
						delete_count = 0
						delete()
						reply = random.choice(SCREENSHOT_REPLY)
						speak_text_cmd(reply)
					elif 'no' in voice_note:
						delete_count = 0
						speak_text_cmd("Fine Sir")
					elif delete_count >=3:
						print("No command received")
						speak_text_cmd("No command received")
						break
		for phrase in SAVE:
			if phrase in voice_note:
				copysave = 0
				save()
				reply = random.choice(SCREENSHOT_REPLY)
				print(reply)
				speak_text_cmd(reply)
		for phrase in joke_dict:
			if phrase in voice_note:
				joke_dir = random.choice(jokes)
				print(joke_dir)
				speak_text_cmd(joke_dir)
		for phrase in calci:
			if phrase in voice_note:
				os.startfile('C:/Windows/System32/calc.exe') 
				#call(["calc.exe"])
				#call(["cmd.exe"])	
				#os.system('calc'.exe)
		for phrase in notepad_dict:
			if phrase in voice_note:
				#open_app = ("notepad")
				#call(["notepad.exe"])
				os.startfile('C:/Windows/System32/notepad.exe')
				#call(["Sublime Text 3.exe"])
		if "open" in voice_note:
			key = voice_note.replace('open ', '').replace('launch ', '')
			print(key)
		#if 'close' in voice_note:
		#	os.system('TASKKILL /F /IM {}.exe'.format(key))
		for phrase in SLEEP:
			if phrase in voice_note:
				error_occurrence = 6
		if 'lock' in voice_note:
			for value in ['pc','system','windows']:
				speak_text_cmd("Sure Sir")
				ctypes.windll.user32.LockWorkStation()
				speak_text_cmd('Your System is Locked            ') 
				exit()
		for phrase in switch_window:
			if phrase in voice_note:
				speak_text_cmd("Ok Sir")
				exe = alt_tab1()
		for phrase in shut_down:
			if phrase in voice_note:
				speak_text_cmd('Ok Sir. Initiating.')
				print('Ok Sir. Initiating.')
				os.system("shutdown/s")
		for phrase in restart:
			if phrase in voice_note:
				speak_text_cmd('Ok Sir. Initiating.')
				print('Ok Sir. Initiating.')
				os.system("shutdown/r")
		for phrase in SCREENSHOT:
			if phrase in voice_note:
				im1 = pyautogui.screenshot()
				while True:
					speak_text_cmd('what should i save it as sir')
					voice_note = read_voice_cmd().lower()
					copysave +=1
					if 'save' in voice_note:
						copysave = 0
						voice_note = voice_note.replace('save it as', '').replace('save as', '').replace('save', '')
						screenshot_name = ('{}'.format(voice_note)) + ".png"
						im2 = pyautogui.screenshot(screenshot_name)
						reply = random.choice(SCREENSHOT_REPLY)
						speak_text_cmd(reply)
						break
					elif copysave >= 3:
						copysave = 0
						print("No command received")
						speak_text_cmd("No command received")
						break
		if 'scroll up' in voice_note:
			speak_text_cmd("Ok Sir")
			pyautogui.scroll(1500)#scroll up 1500
		if 'scroll down' in voice_note:
			speak_text_cmd("Ok Sir")
			pyautogui.scroll(-1500)#scroll down -1500
		if 'google maps' in voice_note:
			speak_text_cmd('Ok Sir')
			speak_text_cmd('Tell Me your current location')
			voice_note = read_voice_cmd().lower()
			webbrowser.open('https://www.google.com/maps/{}', voice_note)
			continue	
		elif 'what is your name' in voice_note:
			speak_text_cmd('I am friday')
			continue
		elif ' when were you created' in voice_note:
			speak_text_cmd('Sir i regularly get updated But i was been created on 22nd April')
		elif 'who created you' in voice_note:
			speak_text_cmd('i am been created by Mr Gaurav')
			continue
		elif 'when were you born' in voice_note:
			speak_text_cmd('22nd of April Sir')
			continue
		elif 'who are you' in voice_note:
			speak_text_cmd('I am friday an Artificial Intelligence Created by Mr Gaurav')
			continue
		elif 'what is your age' in voice_note:
			speak_text_cmd('Sir i am a computer program')
			continue
		elif is_valid_google_search(voice_note):
			print("In google Search...")
			playsound('friday\search_1.mp3')
			webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))
			google_search_result(voice_note)
		elif is_valid_note(thankyou_dict, voice_note):
			play_sound(mp3_thankyou_list)
			continue
		elif 'thank you' in voice_note:
			play_sound(mp3_thankyou_list)
			#sleepp()
			continue
		elif 'play song' in voice_note:
			while True:
				if 'play song' in voice_note :
					speak_text_cmd('which song would you  like to listen sir')
					song_name=read_voice_cmd().lower()
					music_dir = 'D:\Music'
					songs = os.listdir(music_dir)
					print(songs)
					os.startfile(os.path.join(music_dir, songs[0]))
					break
		if 'age detection' in voice_note:
			os.system('cmd /c "python detect.py --image girl1.jpg"')
			#cap = detect
			continue
		elif is_valid_note(open_launch_dict, voice_note):
			print("In Open..")
			play_sound(mp3_open_launch_list)
			if (is_valid_note(social_media_dict, voice_note)):
			# Launch Facebook
				key = voice_note.split(' ')[1]
				webbrowser.open(social_media_dict.get(key))
			else:
				key = voice_note.replace('open ', '').replace('launch ', '')
				print('Key is : ' + key)
				# print(list(lookup_file_system_events.lookup_dict.keys()))

				opt_dict = {}
				for k in list(lookup_file_system_events.lookup_dict.keys()):
					if key in k.lower():
						opt_dict.update({k: lookup_file_system_events.lookup_dict.get(k)})

				print(opt_dict)
				if len(opt_dict) == 1:
					for key in opt_dict.keys():
						print('explorer {}'.format(opt_dict.get(key)))
						os.system('explorer {}'.format(opt_dict.get(key)))
				elif len(opt_dict) > 1:
					speak_text_cmd('I have found multiple instances. Which one you want?')
					default = 0
					index = None
					for i, k in enumerate(opt_dict.keys()):
						print(k.split('.')[0].split('_')[0] + ' from {} folder'.format(opt_dict.get(k).split('\\')[-2]))
						speak_text_cmd(
							k.split('.')[0].split('_')[0] + ' from {} folder '.format(opt_dict.get(k).split('\\')[-2]),
							)

						default = i

					text = read_voice_cmd().lower()
					print(text)
					index = get_index(text)

					if index != None:
						print('explorer {}"'.format(
							lookup_file_system_events.lookup_dict.get(list(opt_dict.keys())[index])) + ' ' + str(index))
						speak_text_cmd('Ok Sir')
						os.system(
							'explorer {}"'.format(lookup_file_system_events.lookup_dict.get(list(opt_dict.keys())[index])))

			continue

		if is_valid_note(goodbye_dict, voice_note):
			play_sound(mp3_goodbye_list)
			exit()

		for phrase in BYE:
			if phrase in voice_note:
				play_sound(mp3_goodbye_list)
				exit()
		for phrase in WOLFRAMCMD:
			if phrase in voice_note:
				try:
					query = voice_note.replace('friday ', '')
					#speak_text_cmd("Give me a minute sir")
					res = client.query(query)
					results = next(res.results).text
					speak_text_cmd("Give me a minute sir")
								#speak('WOLFRAM-ALPHA says - ')
								#speak_text_cmd('Got it.')
					print(results)
					speak_text_cmd(results)
				except:
					speak_text_cmd("I don't know sir. Google is smarter than me")
					webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))
