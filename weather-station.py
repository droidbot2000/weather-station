from HIH6130.io import HIH6130
from picamera import PiCamera
from datetime import datetime
from twython import Twython
import time

# Twitter authentication
APP_KEY=''
APP_SECRET=''
OAUTH_TOKEN=''
OAUTH_TOKEN_SECRET=''

# Twython object
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

while True:
    #take a photo and store it
    camera = PiCamera()
    camera.capture('/home/pi/ODC.jpg')
    camera.close()
    time.sleep(10)
    
    #take a temperature and humidity reading
    rht = HIH6130()
    rht.read()
    print("timestamp: {0}\tRH: {1}%\tTemp: {2} degC".format(rht.timestamp, rht.rh, rht.t))
    
    # Post to Twitter!
    photo = open('/home/pi/ODC.jpg', 'rb')
    response = twitter.upload_media(media=photo)
    msg = 'Hello there! CIS WeatherBot here! Right now, it is {0}\tRH: {1}%\tTemp: {2} degC'.format(rht.timestamp, rht.rh, rht.t)
    twitter.update_status(status=msg, media_ids=[response['media_id']])
    
    # Delay (in seconds ) before next reading
    time.sleep(3600)
