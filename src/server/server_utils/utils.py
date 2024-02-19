from server import server
from datetime import datetime

def send_message_to_single_client(client, msg):
    client.sendall(msg.encode())

def send_messages_to_all_client(msg):
    for client in server.ACTIVE_CLIENT:
        send_message_to_single_client(client[1], msg)

def listen_for_message(client, username):
    while True:
        response = client.recv(2048).decode('utf-8')
        if response != '':
            time_now = datetime.now()
            msg = str(time_now) + username + ' ~ ' + response
            send_messages_to_all_client(msg)
        else:
            print(f"message sent from user {username} is empty")

def client_handler(client):
    while True:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            server.ACTIVE_CLIENT.append((username, client))
        else:
            print("Did not receive username")
