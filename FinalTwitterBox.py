from PIL import Image
import StringIO
import subprocess
import sys
from twython import Twython
import pygame
import pygame.camera
from pygame.locals import *
import time

CONSUMER_KEY = 'key'
CONSUMER_SECRET = 'key'
ACCESS_KEY = 'key'
ACCESS_SECRET = 'key'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()

def check():
	im1 = Image.open("/home/pi/Desktop/base.jpg")
	buffer1 = im1.load()

	im2 = Image.open("/home/pi/Desktop/other.jpg")
	buffer2 = im2.load()

	 # Count changed pixels
	changedPixels = 0
	threshold = 30
	for x in xrange(0, 100):
	    for y in xrange(0, 75):
	        # Just check green channel as it's the highest quality channel
	        pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])
	        if pixdiff > threshold:
	            changedPixels += 1
	return changedPixels

def takepic():
	image = cam.get_image()
	pygame.image.save(image,'other.jpg')

while(True):
	time.sleep(20)    #dely of 20sec 
	takepic()
	if check() > 1000
		photo = open('/home/pi/Desktop/other.jpg','rb')
		api.update_status_with_media(media=photo, status='My PI be tweeting images now of who opened the box ')


