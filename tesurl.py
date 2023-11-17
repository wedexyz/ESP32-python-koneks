import time
import urllib.request

while True :
    urllib.request.urlopen('http://192.168.1.15/ledon')
    print(1)
    time.sleep(1)
    urllib.request.urlopen('http://192.168.1.15/ledoff')
    print(2)
    time.sleep(1)
