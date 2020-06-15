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
        f = open('Mobile_data_event_{0}{1:02d}{2:02d}.csv'.format(date.year,date.month,date.day),'w',encoding = 'utf-8', newline ='')
        wr = csv.writer(f)
        tm = time.localtime(time.time())
        wr.writerow([self.index, name, time.strftime('%c', tm),"{0:02d}:{1:02d}:{2:02d}".format(tm.tm_hour,tm.tm_min,tm.tm_sec), flag])
        self.index += 1

if(__name__ == "__main__"):
    mobile = Crawler()
    date = datetime.datetime.now().date()
    f = open('Mobile_data_event_{0}{1:02d}{2:02d}.csv'.format(date.year,date.month,date.day),'w',encoding = 'utf-8', newline ='')
    wr = csv.writer(f)
    wr.writerow(["INDEX", "DATE", "TIME", "Interval", "AirConditioner", "DoorLock", "Lamp", "TV", "Vacuum", "Washer"])
    f.close()
    print("Process Crawler")
    print("If you shut down, press Ctrl + z")
    print("Crawl Processing...",end="")
    while(1):
        mobile.Crawling()
        print(".",end="")
        time.sleep(1) 