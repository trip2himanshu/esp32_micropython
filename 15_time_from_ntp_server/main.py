# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# get the time and date from internet using esp32s3 devkit
# using ntptime module which allows to synchronize the
# ESP32S3's internal clock with a Network Time Protocol (NTP) server


import network
import time
import ntptime 
import sys
import gc

# used to manually trigger the garbage collector to reclaim memory that is no longer in use
# maually triggering the garbage collector to reclaiming the memory 
gc.collect()


# method to connect with Wi-Fi
def connect_wifi(ssid, psk, timeout):
    try:
        # object for wi-fi (station mode) 
        wlan = network.WLAN(network.STA_IF)
        # restart the wlan driver
        wlan.active(False)
        time.sleep(1)
        wlan.active(True)
        # connect with wi-fi
        wlan.connect(ssid, psk)
        t = 0
        print("Connecting...")
        # connect with wi-fi with timeout 
        while wlan.isconnected() == False and timeout-t > 0:
            print("*", end="")
            t += 1
            time.sleep(1)
        if wlan.isconnected() == True:
            print("\nConnection established")
            print("The IP addr of ESP device is: ",wlan.ifconfig()[0])
            return wlan 
        else:
            print("\nCoudnt not connect")
    except Exception as e:
        print(f"Error in wifi connection > {e}")
        sys.exit()
        
# method to get date and time
def get_time():
    # we should choose the NTP server which is closer to our location
    # geographically to reduce latency and improved synchronization accuracy
    # choice 1: (for India)
    # NTP pool servers - NTP pool project servers which are collection of volunteer-operated
    # NTP servers world wide (in.pool.ntp.org)
    # Government NTP servers - operated by Indian government, they are
    # typically quite reliable and accurate (time.nic.in or time2.nic.in)
    # set the NTP server to synchronize with
    ntp_server = "in.pool.ntp.org"
    # synchronize time with NTP server
    try:
        ntptime.host = ntp_server
        ntptime.settime()
        print("Time synchronized with NTP server")
    except Exception as e:
        print("Error in synchronizing time : ", e)
    # accessing date and time
    # get the current timestamp (seconds since epoch)
    # indian standard time is UTC + 5:30
    current_timestamp = time.time() + ((5 * 3600) + (30 * 60))
    # convert the timestamp to a readable data and time
    formatted_time = time.localtime(current_timestamp)
    print("Current date and time : ", formatted_time)
    year = formatted_time[0]
    month = formatted_time[1]
    date = formatted_time[2]
    hour = formatted_time[3]
    minute = formatted_time[4]
    seconds = formatted_time[5]
    day_of_week = formatted_time[6]
    day_of_year = formatted_time[7]
    current_date_time = "{:02}-{:02}-{:04} {:02}:{:02}:{:02}".format(date,month,year,hour,minute,seconds)
    print("Current date & time = ",current_date_time)


if __name__ == "__main__":
    wlan = connect_wifi("hPhone", "testingesp32", 10)
    get_time()
    sys.exit()

        
    

