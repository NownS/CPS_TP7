# 모바일 기기에서 프로세스 크롤링
import psutil
import time
import csv
import threading

class Crawler():
    def __init__(self):
        self.pname = ['Alarm.py','Game.py','Music.py','Note.py','Training.py','Video.py']
        self.pflag = dict(zip((self.pname),[0,0,0,0,0,0]))
        self.pid = dict(zip((self.pname),[0,0,0,0,0,0]))
        self.index = 0

    def Crawling(self):
        threading.Timer(1,self.Crawling).start()
        self.Write(self.pflag.values)
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
        f = open('mobile_data.csv','a',encoding = 'utf-8', newline ='')
        wr = csv.writer(f)
        tm = time.localtime(time.time())
        wr.writerow([self.index, "{0:02d}/{1:02d} {2:02d}:{3:02d}:{4:02d}".format(tm.tm_mon, tm.tm_mday, tm.tm_hour,tm.tm_min,tm.tm_sec)] + flag)
        f.close()
        self.index += 1

if(__name__ == "__main__"):
    f = open('mobile_data.csv','w',encoding = 'utf-8', newline ='')
    wr = csv.writer(f)
    wr.writerow(["INDEX", "TIME", "Alarm", "Game", "Music", "Note", "Training", "Video"])
    f.close()
    mobile = Crawler()
    mobile.Crawling()