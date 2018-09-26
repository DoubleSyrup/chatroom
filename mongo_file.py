#将文件以grid方案存放到数据库
import gridfs
from pymongo import MongoClient

conn = MongoClient('localhost',27017)
db = conn.grid

fs = gridfs.GridFS(db)

f = open('5.png','rb')
#将内容写入到数据库
fs.put(f.read(),filename = '5.png')

conn.close()