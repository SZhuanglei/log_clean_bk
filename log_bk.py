#!/usr/bin/env python
#coding=utf-8
import os

#if data >= 20000k
find_data=os.popen("find / -size +20000k | grep log")

data=find_data.read()
print("-------------data_list------------")
print data
data_list= data.split("\n")


#clear the gz file before
print("----------rm file.gz--------------")
for i in data_list:
    try:
        print ("rm %s.gz"%i)
        os.system("rm %s.gz"%i)
    except:
        pass
        
#creat gz file
print("---------gzip file----------------") 
for i in data_list:
    try:
        print ("gzip %s"%i)
        os.system("gzip %s"%i)
    except:
        print ('null')
    
