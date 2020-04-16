# IoT-Smart-Assistant
Using Raspberry and Google API made a project that fetches the events from Calendar and reminds for the event by Text-to-Speech reminder. 

Please Note that, In this code, GPIO is used for using a toggle button as Snooze Button. If you are implementing this project in LINUX then you may need to remove couple of lines of code corresponding to Snooze part. Rest of the things will be good to go.

## Step 1 : Turn on Google Calendar API

To do so, Kindly visit https://developers.google.com/calendar/quickstart/python#step_1_turn_on_the and follow step 1 as mentioned. You will be needing to download credentials.json file to your working directory on local system. 

## Step 2 : Install Google Client Library

To do so, Kindly visit https://developers.google.com/calendar/quickstart/python#step_2_install_the_google_client_library and follow step 2 as mentioned. This is to install the required library.  

## Step 3 : Run the main python code file

For this, type following in the shell.
>python smartassistant.py


Note : You may need to install few other packages if that is not available in your system.
