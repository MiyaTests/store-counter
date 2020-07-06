import cv2
import numpy as np
import socket
import sys
import pickle
import struct

cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',8089))

while True:
    ret,frame=cap.read()
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        # Serialize frame
        data = pickle.dumps(frame)

        # Send message length first
        message_size = struct.pack("L", len(data)) ### CHANGED
        # Send size 0 if want to terminate

        # Then data
        clientsocket.sendall(message_size + data)

        # Receive price
        total = clientsocket.recv(4096)
        print(total)

        # Release cv2
        cap.release()
        cv2.destroyAllWindows()
        exit(1)

        
