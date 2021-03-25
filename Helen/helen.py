import speech_recognition as sr
from gtts import gTTS
import pyaudio
import sklearn
import os

########## ASSISTANT LOGIC   ##############
def assistant():
	######### INITIALIZING TOOLS ##########
	def speak(audio):
		print(audio)
		tts = gTTS(text=audio, lang='en')
		tts.save('audio.mp3')
		os.system('mpg123 audio.mp3')

	######## LISTENING TO USER COMMANDS #######
	def listen():

		r = sr.Recognizer()

		with sr.Microphone() as source:
			print('Say something')
			audio = r.listen(source)
			r.pause_thresholde = 1
			r.adjust_for_ambient_noise(source, duration=1)
			audio = r.listen(source)
		try:
			cmd = r.recognize_google(audio)
			print('You said: ' + cmd)
		except sr.UnknownValueError:
			print('Failed to recognize your speech!')
			execute(listen())

		return cmd

	###### AND EXECUTING THEM
	def execute(cmd):
		if 'open chrome' in cmd:
			speak('Opening.')
			os.system("/usr/bin/google-chrome-stable")

		elif 'open firefox' in cmd:
			speak('Opening')
			os.system("/usr/bin/firefox")

		elif 'open the file manager' in cmd:
			speak('Opening')
			os.system("/usr/bin/nautilus")

		elif 'open vscode' in cmd:
			speak('Opening')
			os.system("/usr/bin/code")

		elif 'power off' in cmd:
			os.system("poweroff")

	speak('I am ready for your command')

	#### FOR A LONG TIME
	while True:
		execute(listen())
		
assistant()
