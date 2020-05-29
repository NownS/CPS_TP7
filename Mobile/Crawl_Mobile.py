# 모바일 기기에서 프로세스 크롤링

import psutil
import time

class Crawler():
    def __init__(self):
        self.pids = psutil.pids

    def Crawling(self):
        if(self.pids != psutil.pids):
            pass
            

    def Write(self):
        pass

if(__name__ == "__main__"):
    mobile = Crawler()
    while(1):
        mobile.Crawling()
        time.sleep(1)