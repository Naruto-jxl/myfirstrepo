import requests
from lxml import etree
import pymongo

conn = pymongo.MongoClient('localhost',27017)       #连接MongoDB
db  = conn.shixian                                  #建库shixian
table = db.libai                                    #建集合libai

import pymysql
conn = pymysql.connect(host="localhost",port=3306,database="shixian",user="root",password="mysql",charset="utf8")
cs1 = conn.cursor()
sql = "insert into libai(title,content) values(%s,%s)"



url = 'https://so.gushiwen.org/shiwen/default_2Ab90660e3e492A{}.aspx'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

for i in range(1,6):

    result = requests.get(url=url.format(i),headers=headers)
    # with open('libai.html','w',encoding='utf-8') as f:
    #     f.write(result.text)

    tree = etree.HTML(result.text)
    div_list = tree.xpath('//div[@class="main3"]/div[@class="left"]/div[@class="sons"]')
    # print(len(div_list))      10
    with open('李白.txt','a',encoding='utf-8') as f:
        for div in div_list:
            title = div.xpath('./div[@class="cont"]/p/a//text()')[0]
            # print(title)        标题
            content = div.xpath('./div[@class="cont"]/div[@class="contson"]//text()')
            content = ''.join(content)
            content = content.strip()
            # print(content)
            # f.write(title+'\n')
            # f.write(content)
            # table.insert_one({'title':title,'content':content})
            cs1.execute(sql,(title,content))


conn.commit()
cs1.close()
conn.close()











