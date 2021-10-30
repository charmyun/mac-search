import requests

#运行即爬取更新官网mac-oui文件库
#生成oui文件

f=open('oui.txt','w',encoding='utf-8')

resp=requests.get("http://standards-oui.ieee.org/oui/oui.txt")

f.write(str(resp.content,encoding="utf-8"))

f.close()