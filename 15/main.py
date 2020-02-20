from googlehomepush import GoogleHome
import os

google_home_ip = "#"

host_list = [
    "#",
    "#",
    "#"
]

def main():
    for host in host_list:

        HOST_UP  = True if os.system("ping -c 1 " + host) is 0 else False
        if HOST_UP:
            pass
        else:
            GoogleHome(host=google_home_ip).say(f"{host} is down")
    

if  __name__ == "__main__":
    try:
       main()
    except (ValueError, KeyboardInterrupt) as reason:
        print("<--------- ERROR OCCURED --------- >")
        print(reason)