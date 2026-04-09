import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

clients = []

def broadcast(message, client):
    for c in clients:
        if c != client:
            c.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Server running...")

    while True:
        client, addr = server.accept()
        print(f"Connected with {addr}")

        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

start_server()