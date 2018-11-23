#program to change indentation of 4 spaces to a single tab
import os
filename=input('enter filename: ')
file=open(filename,'r')
file1=open('temp.py','w')
for i in file:
    s=i
    s.replace('    ','  ')
    file1.write(s)
file1.close()
file.close()
os.remove(filename)
os.rename('temp.py',filename)