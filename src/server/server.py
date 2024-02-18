from dotenv import load_dotenv
import os
import socket

load_dotenv()

# HOST = os.environ.get("HOST")
# PORT = os.environ.get("PORT")
# LISTNER_LIMIT = os.environ.get("LISTNER_LIMIT")

# test
HOST = '127.0.0.1'
PORT = 1234
LISTNER_LIMIT = 5

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"binded server successfully to {HOST} {PORT}")
    except Exception as e:
        print(f"not able to bind server to {HOST} and {PORT}, exception >> {e}")
        return
    
    server.listen(LISTNER_LIMIT)

    while True:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

if __name__ == '__main__':
    main()