
import os
import sys
import csv
# change the working directory
os.chdir('C:/Users/saranshmohanty/Desktop')

A_temp=[]

# this is the part where the csv file is read, change the name of the file
with open('add.csv','r') as csvfile:
    sv_reader = csv.reader(csvfile, delimiter=',')  
    for row in sv_reader:
        A_temp.append(str(row[0]))

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
final=[]
import pandas as pd
for i in A_temp:
    try:
        location = geolocator.geocode(str(i))
        final.append((i,(location.latitude,location.longitude)))
        print(i)
        print((location.address))
    except:
        final.append((i,("LAT NA"),("Long NA")))
    print(len(final))  
    


df=[]
df=pd.DataFrame(list(final))
#output file name. It will be created in the current working directory
df.to_csv('zipcode_test.csv')
