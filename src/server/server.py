from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
LISTNER_LIMIT = os.environ.get("LISTNER_LIMIT")

def main():
    pass

if __name__ == '__main__':
    main()