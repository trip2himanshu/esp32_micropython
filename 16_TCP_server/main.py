# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# setup the esp32s3 as TCP server and let it comunicate with the
# PC as a client
# run the main.py script (server side script) on esp32s3
# run the client.py script on your PC

import usocket as socket
import network
import time
import time
import gc
import sys

# reclaim memory 
gc.collect()

# method to connect the esp32s3 with wi-fi network
def connect_wifi(ssid,psk,timeout):
    try:
        # wlan object (station device) 
        wlan = network.WLAN(network.STA_IF)
        # re-enable the wlan driver
        wlan.active(False)
        time.sleep(1)
        wlan.active(True)
        # connect with network
        wlan.connect(ssid,psk)
        print("Connecting", end="")
        t = 0
        # wait for connection till timeout limit completes
        while wlan.isconnected() == False and timeout - t > 0:
            print("-",end="")
            t += 1
            time.sleep(1)
        if wlan.isconnected() == True:
            print("\nConnection established")
            print("IP of ESP32S3: ", wlan.ifconfig())
            return wlan
        else:
            print("Could not connect")
            sys.exit()
    except Exception as e:
        print("Error in connection > ",e)
        sys.exit()


# setup TCP server on esp32s3
def tcp_server():
    try:
        # server socket 
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # bind the socket with IP and port
        s.bind(('0.0.0.0',5050))
        # listen for clients
        s.listen()
        print("Server is up and running")
        return s
    except Exception as e:
        print("Error in socket creation > ",e)
        sys.exit()
    except KeyboardInterrupt:
        print("Exiting from tcp_server() method")
        sys.exit()

def start_communication(s):
    while True:
        try:
            # accept the client connection 
            client,addr = s.accept()
            print("Client connected from ",addr[0]," : ",addr[1])
            while True:
                # receive msg from client
                msg = client.recv(1024)
                if not msg:
                    print("No message received")
                    break
                print("Client :: ",msg.decode('utf-8'))
                # send echo message to client
                client.send(msg)
            # close the socket
            client.close()
            print("Client disconnected, waiting for new client")
        except Exception as e:
            print("Error in client comm > ", e)
            break
        except KeyboardInterrupt:
            print("Exiting from client communication")
            break
    print("Closing server")
    s.close()
    sys.exit()
    

if __name__ == "__main__":
    wlan = connect_wifi("hPhone","testingesp32",10)
    server = tcp_server()
    start_communication(server)











        

        
    

