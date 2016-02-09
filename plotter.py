import random
import RPi.GPIO as GPIO
import time
import cv2
import sys

img = cv2.imread(sys.argv[1])

height = img.shape[0]
width = img.shape[1]

delay=0.005

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

xa1, xa2, xb1, xb2 = 18, 23, 24, 25
ya1, ya2, yb1, yb2 = 22, 27, 17, 4
za1, za2 = 8, 7

GPIO.setup(xa1, GPIO.OUT)
GPIO.setup(xa2, GPIO.OUT)
GPIO.setup(xb1, GPIO.OUT)
GPIO.setup(xb2, GPIO.OUT)

GPIO.setup(ya1, GPIO.OUT)
GPIO.setup(ya2, GPIO.OUT)
GPIO.setup(yb1, GPIO.OUT)
GPIO.setup(yb2, GPIO.OUT)

GPIO.setup(za1, GPIO.OUT)
GPIO.setup(za2, GPIO.OUT)

GPIO.output(xa1, False)
GPIO.output(xa2, False)
GPIO.output(xb1, False)
GPIO.output(xb2, False)

GPIO.output(ya1, False)
GPIO.output(ya2, False)
GPIO.output(yb1, False)
GPIO.output(yb2, False)

GPIO.output(za1, False)
GPIO.output(za2, False)

def moveX(w1, w2, w3, w4):
  GPIO.output(xa1, w1)
  GPIO.output(xa2, w2)
  GPIO.output(xb1, w3)
  GPIO.output(xb2, w4)

def moveY(w1, w2, w3, w4):
  GPIO.output(ya1, w1)
  GPIO.output(ya2, w2)
  GPIO.output(yb1, w3)
  GPIO.output(yb2, w4)

def moveZ(w1, w2):
  GPIO.output(za1, w1)
  GPIO.output(ya1, w1)
  GPIO.output(ya2, w2)
  GPIO.output(yb1, w3)
  GPIO.output(yb2, w4)

def moveZ(w1, w2):
  GPIO.output(za1, w1)
  GPIO.output(za2, w2)

def dot():
  moveZ(0, 0)
  time.sleep(0.2)
  moveZ(0, 1)
  time.sleep(0.34)
  moveZ(0, 0)
  time.sleep(0.2)
  moveZ(1, 0)
  time.sleep(0.5)

def moveLeft(steps):
  for i in range(0, steps):
      moveX(1,0,1,0)
      time.sleep(delay)
      moveX(1,0,0,1)
      time.sleep(delay)
      moveX(0,1,0,1)
      time.sleep(delay)
      moveX(0,1,1,0)
      time.sleep(delay)

def dot():
  moveZ(0, 0)
  time.sleep(0.2)
  moveZ(0, 1)
  time.sleep(0.34)
  moveZ(0, 0)
  time.sleep(0.2)
  moveZ(1, 0)
  time.sleep(0.5)

def moveLeft(steps):
  for i in range(0, steps):
      moveX(1,0,1,0)
      time.sleep(delay)
      moveX(1,0,0,1)
      time.sleep(delay)
      moveX(0,1,0,1)
      time.sleep(delay)
      moveX(0,1,1,0)
      time.sleep(delay)

def moveYUp(steps):
  for i in range(0, steps):
    moveY(0,1,1,0)
    time.sleep(delay)
    moveY(0,1,0,1)
    time.sleep(delay)
    moveY(1,0,0,1)
    time.sleep(delay)
    moveY(1,0,1,0)
    time.sleep(delay)

def moveYDown(steps):
  for i in range(0, steps):
    moveY(1,0,1,0)
    time.sleep(delay)
    moveY(1,0,0,1)
    time.sleep(delay)
    moveY(0,1,0,1)
    time.sleep(delay)
    moveY(0,1,1,0)
    time.sleep(delay)

def moveRight(steps):
  for i in range(0, steps):
    moveX(0,1,1,0)
    time.sleep(delay)
    moveX(0,1,0,1)
    time.sleep(delay)
    moveX(1,0,0,1)
    time.sleep(delay)
    moveX(1,0,1,0)
    time.sleep(delay)

for x in range(width):
  for y in range(height):
    print "Row: {}\nCol: {}".format(x, y)
    percentDone = (x * y) / (width*height)
    print "Percent complete: {}%".format(percentDone)
    red = img[y, x, 2]
    green = img[y, x, 1]
    blue = img[y, x, 0]

    if red != 255 and green != 255 and blue != 255:
      dot()
    moveRight(1)

  #Go back to the start of the row
  moveLeft(height)
  moveYUp(1)

moveYDown(width)
