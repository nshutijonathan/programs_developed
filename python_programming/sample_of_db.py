import time
import os,glob
import webbrowser
import os
for i in range(1,11):
    print(i)
i=1
while i<=10:
    print(i)
    i +=1

os.chdir(r"C:\Users\Technician\Desktop")
for file in glob.glob("*.docx"):
    print(file)   
    if file =="jonathancv3.docx":
        d=(r"C:\Users\Technician\Desktop\malaika.mp4")
        os.system(d)
    else:
        print("")
