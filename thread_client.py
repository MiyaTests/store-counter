import cv2
import numpy as np
import socket
import sys
import pickle
import struct
from threading import Thread

class Camera(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        ret,frame=cap.read()
        # Serialize frame
        data = pickle.dumps(frame)

        # Send message length first
        message_size = struct.pack("L", len(data)) ### CHANGED

        # Then data
        clientsocket.sendall(message_size + data)
    
cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',8089))

while True:
    a = Camera(1)
    a.start()
    
