# -*- coding: utf-8 -*
import os
import io
def replace_char(string,char,index):
     string = list(string)
     string[index] = char
     return ''.join(string)


f_path = '/home/gjx/picture/dancer/2020.1.24/validateImage/' 
files = os.listdir(f_path)
for file in files:
	#if not os.path.isdir(file):
    f = os.path.basename(file)
    (filename, extension) = os.path.splitext(file)      #将文件名拆分为文件名与后缀
    if (extension == '.txt'):                             #判断该后缀是否为.c文件
        print(f_path+filename+extension)           #以PLACE_RAM(文件名)形式输出文件名
        whole_name = f_path+filename+extension
        lines=[]
        with open(whole_name,'r') as ff:
            if True:
              ff.seek(0)
              nline=ff.readlines()
            for line in range(len(nline)):
            #print(f.readline())
            
                myline=nline[line]
                if(myline!="\n"):
                #print("myline:"+myline)
                  newline=myline.replace(myline[0],str(int(myline[0])+3),1)
                #print("new:"+newline)
                  lines.append(newline)
        with open(whole_name,'w') as ff:
            print(lines)
            ff.writelines(lines)
            ff.close()
            #ff.writelines(newline)
        
        #outfile.write(""+f+"\n")
        #paths=""