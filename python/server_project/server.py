#!/usr/bin/python3

import socket
import sys
from _thread import *


def main():

    host = ""
    port = 8888


    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Failed to create socket. Error code: " + str(msg[0]) + " Message " + str(msg[1]))
        sys.exit()

    print("Socket created")

    try:
        s.bind((host, port))
    except socket.error as msg:
        print("Bind failed. Error code: " + str(msg[0]) + " Message " + str(msg[1]))

    print("Socked bind complete")

    s.listen(10)
    print("Socket is now listening")

    def clientthread(conn):

        #Message sended to the connected client
        conn.send(("Welcome to the server. Type something and hit Enter\n").decode())
        while True:
            data = conn.recv(2048).decode()
            reply = ("Server says: ") + data
            if not data:
                break

            conn.send(reply.encode())

        conn.close()


    while 1:
        conn, addr = s.accept() #waiting to accept connection

        print("Connected with " + addr[0] + " : " + str(addr[1]))
        start_new_thread(clientthread(conn))


    s.close()

if __name__ == "__main__":
    main()