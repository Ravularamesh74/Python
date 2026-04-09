import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break

def write():
    while True:
        msg = input("")
        client.send(msg.encode())

threading.Thread(target=receive).start()
threading.Thread(target=write).start()