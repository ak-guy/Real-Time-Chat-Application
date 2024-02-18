import socket
from src.server.server import *

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print(f"successfully to server {HOST} {PORT}")
    except:
        print(f"not able to connect to server {HOST} {PORT}")


if __name__ == '__main__':
    main()