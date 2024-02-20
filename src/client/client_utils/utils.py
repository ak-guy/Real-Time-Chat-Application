import threading

def send_msg_to_server(client):
    while True:
        msg = input("Message: ")
        if msg != '':
            client.sendall(msg.encode())
        else:
            print("message cannot be empty")
            send_msg_to_server(client)

def listen_for_message_from_server(client):
    while True:
        msg = client.recv(2048).decode('utf-8')
        if msg != '':
            print('\n')
            print(msg)
            username = msg.split('~')[1]
            actual_msg = msg.split('~')[2]
        else:
            print("No message received from server")

def communicate_with_server(client):
    username = input("Please Enter username: ")
    if username != '':
        client.sendall(username.encode())
    else:
        print("Username cannot be empty")
        communicate_with_server(client)

    threading.Thread(target=listen_for_message_from_server, args=(client,)).start()

    send_msg_to_server(client)