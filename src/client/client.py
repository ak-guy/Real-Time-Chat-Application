import socket
from client_utils import utils
import tkinter as tk

HOST = '127.0.0.1'
PORT = 1234

tk_window = tk.Tk()
tk_window.resizable(False, False)
tk_window.geometry("600x600")
tk_window.title("Oshaberi App")

top_frame = tk.Frame(tk_window, width=600, height=70, bg='orange')
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

middle_frame = tk.Frame(tk_window, width=600, height=460, bg='white')
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

bottom_frame = tk.Frame(tk_window, width=600, height=70, bg='green')
bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

def main():
    tk_window.mainloop()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print(f"successfully to server {HOST} {PORT}")
    except:
        print(f"not able to connect to server {HOST} {PORT}")

    utils.communicate_with_server(client)

if __name__ == '__main__':
    main()