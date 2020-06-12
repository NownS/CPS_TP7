import socket

HOST = "127.0.0.1"
PORT = 8080
Buff_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(100)
    print('Server Listening...')
    while True:
        Client, addr = s.accept()
        print('Connection from', addr)
        Filename = Client.recv(Buff_SIZE)
        Filename = Filename.decode()
        Filesize = Client.recv(Buff_SIZE)
        Filesize = int(Filesize.decode())
        msg = "ready"
        Client.sendall(msg.encode())
        with open(Filename, 'w', encoding="UTF-8") as f:
            data = Client.recv(Filesize)
            f.write(data.decode())
        print("File name : "+Filename)
        print("File size : "+str(Filesize))
        