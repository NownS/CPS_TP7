# 모바일 기기에서 프로세스 크롤링, 꾸준히 크롤링
import psutil
import time
import csv
import threading
import os
import datetime


class Crawler():
    def __init__(self):
        self.pname = [os.getcwd()+'\\Controller_Home.py','AirConditioner.py','DoorLock.py','Lamp.py','TV.py','Vacuum.py','Washer.py']
        self.pflag = dict(zip((self.pname),[0,0,0,0,0,0,0]))
        self.pid = dict(zip((self.pname),[0,0,0,0,0,0,0]))
        self.index = 0

    def Crawling(self):
        threading.Timer(5,self.Crawling).start()
        self.Write(list(self.pflag.values()))
        process = psutil.pids()
        for p in process:
            try:
                pro = psutil.Process(p)
                for i in self.pname:
                    if(self.pid[i]):
                        if(self.pid[i] not in process):
                            self.pflag[i] = 0
                            self.pid[i] = 0
                            continue
                            
                    if(pro.name() == "python.exe" and i == pro.cmdline()[1] and not self.pflag[i]):
                        self.pflag[i]=1
                        self.pid[i]=pro.pid
            except:
                continue

    def Write(self,flag):
        date = datetime.datetime.now().date()
        f = open('Home_data_Linear_{0}{1:02d}{2:02d}.csv'.format(date.year,date.month,date.day),
        'a',encoding = 'utf-8', newline ='')
        wr = csv.writer(f)
        tm = datetime.datetime.now()
        tmnow = datetime.datetime.now().time()
        tminterval = tmnow.hour * 3600 + tmnow.minute * 60 + tmnow.second
        wr.writerow([self.index, "{0:04d}/{1:02d}/{2:02d}".format(tm.year,tm.month, tm.day),
        "{0:02d}:{1:02d}:{2:02d}".format(tm.hour,tm.minute,tm.second), tminterval] + flag)
        f.close()
        self.index += 1

if(__name__ == "__main__"):
    date = datetime.datetime.now().date()
    f = open('Home_data_Linear_{0}{1:02d}{2:02d}.csv'.format(date.year,date.month,date.day),'w',encoding = 'utf-8', newline ='')
    wr = csv.writer(f)
    wr.writerow(["INDEX", "DATE", "TIME", "Interval", "Home_Controller", "AirConditioner", "DoorLock", "Lamp", "TV", "Vacuum", "Washer"])
    f.close()
    print("Process Crawler")
    print("If you shut down, press Ctrl + z")
    print("Crawl Processing...",end="")
    mobile = Crawler()
    mobile.Crawling()