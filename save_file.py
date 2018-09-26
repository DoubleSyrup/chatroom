#小文见存储方案
#将小文件直接转化为二进制存储
from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)
db = conn.image

myset = db.santai

# f = open('5.png','rb')
# #将图片内容转化为可存储的二进制格式
# content = bson.binary.Binary(f.read())

# myset.insert({'filename':'santai','data':content})


img = myset.find_one({'filename':'santai'})

with open('santai','wb') as f:
    f.write(img['data'])
 
conn.close()
