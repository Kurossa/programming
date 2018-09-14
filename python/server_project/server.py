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

    host = "www.google.com"
    port = 80

    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Host name could not be resolved. Exiting")
        sys.exit()

    print("Ip address of " +host + " is " +remote_ip)

    s.connect(remote_ip, port) #Connect to remote server

    print('Socket connected to ' + host + "on ip" + remote_ip)

if __name__ == "__main__":
    main()