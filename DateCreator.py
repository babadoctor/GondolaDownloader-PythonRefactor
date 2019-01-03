import datetime,time,calendar
dates = []
epochtime = 1542744000
numlines = 0
import os

print os.path.split("/Users/babadoctor/Desktop/datechecker/dates.txt")
print calendar.timegm(time.gmtime())#gets current epoch time

with open("/Users/babadoctor/Desktop/datechecker/parsed.sh") as ff:
    for i, l in enumerate(ff):
        pass
    numlines = i + 1
f = open("/Users/babadoctor/Desktop/datechecker/dates.txt","w+")



for i in range(numlines):#enumerate through list
    dates.append(datetime.datetime.fromtimestamp(epochtime).isoformat())#gets iso date from epochtime 
    epochtime+=86400 #adds a day to epoch time
    f.write(dates[i]) #write the new date to the array
    f.write("\n")#newline
f.close()
