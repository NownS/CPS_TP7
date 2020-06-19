#홈 IOT 기기에서 프로세스 크롤링, 변동되는 특정 지점을 확인
import psutil
import time
import csv
import datetime
import os

class Crawler():
    def __init__(self):
        self.pname = ['AirConditioner.py','DoorLock.py','Lamp.py','TV.py','Vacuum.py','Washer.py']
        self.pflag = dict(zip((self.pname),[0,0,0,0,0,0]))
        self.pid = dict(zip((self.pname),[0,0,0,0,0,0]))
        self.index = 1

    def Crawling(self):
            for p in psutil.pids():
                try:
                    pro = psutil.Process(p)
                    for i in self.pname:
                        if(self.pid[i]):
                            if(self.pid[i] not in psutil.pids()):
                                self.pflag[i] = 0
                                self.pid[i] = 0
                                self.Write(i, 0)
                                continue

                        if(pro.name() == "python.exe" and i == pro.cmdline()[1] and not self.pflag[i]):
                            self.pflag[i]=1
                            self.pid[i]=pro.pid
                            self.Write(i, 1)
                except:
                    continue

    def Write(self,name,flag):
        f = open('Home_data_event_{0}{1:02d}{2:02d}.csv'.format(date.year,date.month,date.day),'a',encoding = 'utf-8', newline ='')
        wr = csv.writer(f)
        tm = time.localtime(time.time())
        tmnow = datetime.datetime.now().time()
        tminterval = tmnow.hour * 3600 + tmnow.minute * 60 + tmnow.second
        wr.writerow([self.index, name, "{0:02d}:{1:02d}:{2:02d}".format(tm.tm_hour,tm.tm_min,tm.tm_sec), tminterval, flag])
        self.index += 1

if(__name__ == "__main__"):
    mobile = Crawler()
    date = datetime.datetime.now().date()
    f = open('Home_data_event_{0}{1:02d}{2:02d}.csv'.format(date.year,date.month,date.day),'w',encoding = 'utf-8', newline ='')
    wr = csv.writer(f)
    wr.writerow(["INDEX", "Name", "TIME", "Interval", "Flag"])
    f.close()
    print("Process Crawler")
    print("If you shut down, press Ctrl + z")
    print("Crawl Processing...",end="")
    while(1):
        mobile.Crawling()
        print(".",end="")
        time.sleep(1) 