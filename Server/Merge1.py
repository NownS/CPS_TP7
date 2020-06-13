import csv
import datetime
import copy

def MergeList(list1, list2):
    list3 = []
    list3.append(list1[0] + list2[0][4:])
    index = [1, 1, 1]
    list1_len = len(list1)
    list2_len = len(list2)
    while(index[0] < list1_len and index[1] < list2_len):
        tmp = []
        if(list1[index[0]][1:4] == list2[index[1]][1:4]):
            tmp.append(index[2])
            tmp = tmp + list1[index[0]][1:] + list2[index[1]][4:]
            list3.append(copy.deepcopy(tmp))
            index[0] = index[0] + 1
            index[1] = index[1] + 1
            index[2] = index[2] + 1
        
        elif(list1[index[0]][3] > list2[index[1]][3]):
            tmp.append(index[2])
            tmp = (tmp + list1[index[0]][1:] + 
            list(["NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]))
            list3.append(copy.deepcopy(tmp))
            index[0] = index[0] + 1
            index[2] = index[2] + 1
        
        else:
            tmp.append(index[2])
            tmp = (tmp + list2[index[1]][1:4] + 
            list(["NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]) + 
            list2[index[1]][4:])
            list3.append(copy.deepcopy(tmp))
            index[1] = index[1] + 1
            index[2] = index[2] + 1
    
    return list3

tm = datetime.datetime.now()
yesterday = "{0}{1:02d}{2:02d}".format(tm.year,tm.month,tm.day-1)
hname = "Home_data_Linear_{}.csv".format(yesterday)
f_home = open(hname,"r", encoding = "UTF-8", newline = '')
mname = "Mobile_data_Linear_{}.csv".format(yesterday)
f_mobile = open(mname,"r",encoding = "UTF-8", newline = '')
home = csv.reader(f_home)
mobile = csv.reader(f_mobile)
f_merge = open("Merge_Linear_{}.csv".format(yesterday),"a", encoding = "UTF-8", newline = '')
merge = csv.writer(f_merge)
newlist = MergeList(list(mobile), list(home))
home = csv.reader(f_home)
mobile = csv.reader(f_mobile)
merge.writerows(newlist)
f_home.close()
f_mobile.close()
f_merge.close()