
import os

path = 'C:\\py_drill'
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print (file)


#______


fName = 'Drill_1.txt'

fPath = 'C:\\py_drill'


abPath = os.path.join(fPath, fName)
print(abPath)


#______


import time 

os.path.getmtime('C:\\py_drill')
  
modification_time = os.path.getmtime('C:\\py_drill') 
print("Last modification time since the epoch:", modification_time) 
  

local_time = time.ctime(modification_time) 
print("Last modification time(Local time):", local_time) 


#______


import fnmatch
for file in os.listdir('C:\\py_drill'):
    if fnmatch.fnmatch(file, '*.txt'):
        fTime = os.path.getmtime('C:\\py_drill')
        print (file,fTime)
