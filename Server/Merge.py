import csv
import datetime

tm = datetime.datetime.now()
today = "{0}{1:02d}{2:02d}".format(tm.year,tm.month,tm.day)
hname = "Home_data_Crawling_{}.csv".format(today)
f_home = open(hname,"r", encoding = "UTF-8")
mname = "Mobile_data_Crawling_{}.csv".format(today)
f_mobile = open(mname,"r",encoding = "UTF-8")
read1 = csv.reader()
read2 = csv.reader()
f_merge = open("Merge_{}".format(today),"w", encoding = "UTF-8")