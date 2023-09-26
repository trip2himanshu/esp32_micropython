# client.py
# python script to run on PC
# Himanshu Tripathi

# client side python script using TCP socket
# run this script on your PC
# server will be running on ESP32 device (main.py)

import socket
import time
import sys

# method to create tcp socket
def client_socket():
    try:
        # client socket
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # connect with server socket
        s.connect(('192.168.156.227',5050))
        print("connection establisged")
        return s
    except Exception as e:
        print("Error in client_socket() : ",e)
        sys.exit()

# method to communicate with server
def start_communication(s):
    while True:
        try:
            # send message to server
            s.send(input(">> ").encode('utf-8'))
            # receive the echo message from server
            msg = s.recv(1024)
            if not msg:
                print("No message received")
                break
            print("Server >> ",msg.decode('utf-8'))
        except Exception as e:
            print("Error in comm :: ", e)
            break
        except KeyboardInterrupt:
            print("Exiting from start_communication()")
            break
    # close socket
    s.close()
    sys.exit()


if __name__ == "__main__":
    client = client_socket()
    start_communication(client)