#!/usr/bin/python3

import socket
import sys


def main():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket
    except socket.error as msg:
        print("Failed to create socket. Error code: " +str(msg[0])+ "Error message: " +str(msg[1]))
        sys.exit()

    print("Socket created ")

    host = "www.google.pl"
    port = 80

    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    print("Ip address of " +host + " is " +remote_ip)

    s.connect((remote_ip, port)) #Connect to remote server

    print('Socket connected to ' + host + " on ip " + remote_ip)

    message = "GET / HTTP/1.1\r\n\r\n" #trying to send some data to remote server
    message_2 = "Hello"

    try:
        s.sendto(message.encode(), (host, port)) #sending string
    except socket.error:
        print("Send failed")
        sys.exit()

    print("Message send successfully")

    reply = s.recv(4096) #receving data

    print(reply)

    s.close()
    print("Socket closed")

if __name__ == "__main__":
    main()