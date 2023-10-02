# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# make esp32s3 devkit a web server
# on the webserver one webpage is hosted with on/off button to
# control the led coonected with esp32

import machine
import network
import time
import sys
import gc
try:
    import usocket as socket
except:
    import socket
    
# run the garbage collector
gc.collect()

# object for led
led = machine.Pin(4,machine.Pin.OUT)
# default led state
led.off()

# method to connect the esp32 with wi-fi and configure it as station device
def connect_wifi(ssid,psk,timeout):
    # object for wlan
    wlan = network.WLAN(network.STA_IF)
    # restart the wlan driver
    wlan.active(False)
    time.sleep(1)
    wlan.active(True)
    # connect with wi-fi
    wlan.connect(ssid,psk)
    t = 0
    print("Connecting",end="")
    while (wlan.isconnected()==False) and (timeout-t>0):
        t += 1
        print(".",end="")
        time.sleep(1)
    if wlan.isconnected() == True:
        print("\nConnection established")
        print("The IP of ESP device is: ",wlan.ifconfig()[0])
        print(wlan)
        return wlan 
    else:
        print("\nCould not connect, try again")
        sys.exit()
        
# webpage
def web_page():
    # setting up the led state variable 
    if led.value() == 1:
        led_state = "ON"
        print("LED is on")
    elif led.value() == 0:
        led_state = "OFF"
        print("LED is off")
    # html script for web page 
    html_page = """    
    <html>    
    <head>    
        <meta content="width=device-width, initial-scale=1" name="viewport"></meta>    
    </head>    
    <body>    
        <center><h2>ESP32 Web Server in MicroPython </h2></center>    
        <center>    
        <form>    
            <button name="LED" type="submit" value="1"> LED ON </button>    
            <button name="LED" type="submit" value="0"> LED OFF </button>  
        </form>    
        </center>    
        <center>
            <p>LED is now <strong>""" + led_state + """</strong>.</p>
        </center>    
    </body>    
    </html>"""  
    return html_page
    

# create server socket at esp32
def server_socket(wlan):
    try:
        if wlan.isconnected():
            # create TCP socket
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # bind the socket
            # Blank IP specifies that socket is reachable by any addr
            # the machine happens to have
            # web server port is 80 (HTTP)
            sock.bind(('',80))
            # start listening for clients (5 max clients here) 
            sock.listen(5)
            print("Socket created at esp")
            return sock
        else:
            print("wifi is not connected")
    except Exception as e:
        print("Error in socket: ",e)
        sys.exit()
        
        
def web_server(wlan,sock):
    while True:
        try:
            if wlan.isconnected():
                # accept the client connection
                client,addr = sock.accept()
                print("Client connected from ",addr)
                # receive data from client
                req = client.recv(1024)
                req = str(req)
                print("request received: ",req)
                # find the request
                led_on = req.find("/?LED=1")
                led_off = req.find("/?LED=0")
                if led_on == 6:
                    # turn on the led
                    led.value(1)
                    print("LED on")
                elif led_off == 6:
                    # turn off the led
                    led.value(0)
                    print("LED off")
                # send response back to client
                response = web_page()
                client.send("HTTP/1.1 200 OK\n")
                client.send("Content-Type: text/html\n")
                client.send("Connection: close\n\n")
                client.sendall(response)
                # close the connection
                client.close()
            else:
                print("Wifi is not connected")
                break
        except Exception as e:
            print("Error in web server: ",e)
            break
        except KeyboardInterrupt:
            print("Exit")
            break
    sock.close()
    sys.exit()
                 
                
if __name__ == "__main__":
    wlan = connect_wifi("ASF_GF", "Skills@0077",10)
    sock = server_socket(wlan)
    web_server(wlan,sock)
        