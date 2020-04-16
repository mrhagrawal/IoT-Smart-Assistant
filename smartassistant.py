from __future__ import print_function
from datetime import datetime
import pickle
import os.path  
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import random
import os

from gpiozero import Button

button = Button(2)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def main():
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

    # Call the Calendar API
    while True:
	    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	    print('Getting the upcoming 10 events')
	    events_result = service.events().list(calendarId='primary', timeMin=now,
	                                        maxResults=10, singleEvents=True,
	                                        orderBy='startTime').execute()
	    events = events_result.get('items', [])

	    if not events:
	        print('No upcoming events found.')
	    for event in events:
	        start = event['start'].get('dateTime', event['start'].get('date'))
	        print("Details fetched for the event with time:  ",start,end="")
	        print(" and event details:  ",event['summary'])
	        # print(start.strftime("%m/%d/%Y, %H:%M:%S"))
	        # print(time.now())
	        
	        if datetime.now().strftime("%Y-%m-%dT%H:%M:%S+05:30")[0:16] == start[0:16]:
	                print ("Waking you up!")
	                print ("---")
                        
                        x = 4

	                while (x>0):
                            x = x -1 
                            time.sleep(1)
                            if button.is_pressed:
                                print("Button is pressed. Stopping Alarm")
                                os.system("flite -voice awb -t 'Button Pressed. Stopping Alarm.' " )
                                break
                            else:
                                os.system("flite -voice awb -t ' " + event['summary'] + " ' " )
			
			#for x in range(5):
 				#os.system("flite -voice awb -t ' " + event['summary'] + " ' " )
 			
	              	#  choosing by random an .mp3 file from direcotry
	                #print ("Now Playing: alarm.mp3")
	                                                               #  plays the MP3 in it's entierty. As long as the file is longer 
	                                                               #  than a minute it will only be played once:
	                #command ='mpg321 /home/hemant/Music/alarm.mp3 -g 100 -n 1500' 
	                #print (command)
	                #os.system(command)                             #  plays the song
	        else: 
	                print ("Waiting 45 seconds to check again")
	    time.sleep(45)

if __name__ == '__main__':
    main()
