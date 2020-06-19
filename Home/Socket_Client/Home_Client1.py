import socket
import os
from datetime import datetime

HOST = "127.0.0.1"
PORT = 8080
Buff_SIZE = 1024
Filename = 'Home_data_Linear_{0}{1:02d}{2:02d}.csv'.format(datetime.now().year,datetime.now().month,datetime.now().day)

def getFileSize(fileName, directory):
        fileSize = os.path.getsize(directory+"\\"+fileName)
        return str(fileSize)

def getFileData(fileName, directory):
        with open(directory+"\\"+fileName, 'r', encoding="UTF-8") as f:
            data = ""
            for line in f:
                data += line
        return data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connection Complete")
    directory = str(os.getcwd())
    print("Send Filename...")
    s.sendall(Filename.encode())
    print("Done")
    print("Wait...")
    s.sendall(getFileSize(Filename, directory).encode())
    msg = s.recv(Buff_SIZE)
    if(msg.decode() == "ready"):
        print("ready")
        s.sendall(getFileData(Filename, directory).encode())
    s.close()
