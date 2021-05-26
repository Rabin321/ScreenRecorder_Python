from PIL import ImageGrab
import numpy as np
import cv2
import datetime
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
# print(width, height) width and height of  screen
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
filename = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
videorecord = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))

webcam = cv2.VideoCapture(0)  # capture the webcam
while True:
    image = ImageGrab.grab(bbox=(0, 0, width, height))
    image_np = np.array(image)
    imagenext = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)  # convert messed up colors into rgb(proper color)
    _, frame = webcam.read()  # read the webcam capture
    webcap_height, webcap_width, _ = frame.shape
    imagenext[0:webcap_height, 0:webcap_width, :] = frame[0: webcap_height, 0:webcap_width, :]

    cv2.imshow('Screen recorder python', imagenext)
    # cv2.imshow('webcam', frame)  # show the webcam capture
    videorecord.write(imagenext)
    if cv2.waitKey(10) == ord('e'):
        break
