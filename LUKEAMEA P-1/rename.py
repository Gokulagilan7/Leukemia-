import os
os.chdir('NORMAL')
i=1
for file in os.listdir():
    src=file
    dst="NORMAL"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1

