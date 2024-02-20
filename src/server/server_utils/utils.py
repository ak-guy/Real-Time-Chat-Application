from constants import *
from datetime import datetime
import threading

def send_message_to_single_client(client, msg):
    client.sendall(msg.encode())

def send_messages_to_all_client(msg):
    for client in ACTIVE_CLIENT:
        send_message_to_single_client(client[1], msg)

def listen_for_message_from_client(client, username):
    while True:
        response = client.recv(2048).decode('utf-8')
        if response != '':
            time_now = datetime.now()
            chat_msg = str(time_now) + '~' + username + '~' + response
            send_messages_to_all_client(chat_msg)
        else:
            pass

def client_handler(client):
    while True:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            ACTIVE_CLIENT.append((username, client))
            prompt_msg = username + f"~added to the chat"
            send_messages_to_all_client(prompt_msg)
            break
        else:
            print("Did not receive username")

    threading.Thread(target=listen_for_message_from_client, args=(client, username)).start()