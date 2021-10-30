import re
#对data文件进行搜索查询
f=open("data.txt",'r',encoding='utf-8')
content=f.read()

#s="F4-BD-9E"

s=input("输入mac地址（:/-间隔不区分大小）：")
s=re.sub(r'[^0123456789ABCDEFabcdef]','',s)
s=s.upper()
ret=re.match("[A-Z0-9]{6}",s).group()
print(ret)
regex1=re.compile(r"(%s).+"%ret)
ans=regex1.search(content).group()
ans=ans[7:]

print(ans)
