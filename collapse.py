import re
#对oui文件进行提取压缩
#生成data文件
f=open("oui.txt","r",encoding='utf-8')
l=0
list=[]
while True:
    line=f.readline()
    if line=='':
        break
    l+=1
    line=line.strip('\n')
    regex1=re.compile(r'^[0-9A-F]{6}.+$')
    ret=regex1.findall(line)
    if len(ret)!=0:
        mac=line[:6]
        org=line[22:]
        org.strip()
        test=mac+" "+org
        list.append(test)
list.sort()
print(list)
f.close()

f2=open("data.txt",'w',encoding='utf-8')
for item in list:
    f2.writelines(item+"\n")
f2.close()
