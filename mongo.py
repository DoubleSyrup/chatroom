import pymongo

conn = pymongo.MongoClient('localhost',27017) 

db = conn.class0

myset = db.class0

# myset.insert_many([{'name':'Jack','age':16,'sex':"M"},{'name':'Wick','age':19,'sex':"M"},\
#     {'name':'Sally','age':15,'sex':"M"}])

p = {'$group':{'_id':'$sex'}}
curson = myset.aggregate(p)
# myset.remove({'name':'Lucy'},)
# # curson = myset.find({},{'_id':0})
# myset.ensure_index('name')
# myindex = myset.list_indexes()
# for i in myindex:
#     print(i)

# myset.ensure_index([('name',1),('age',-1)])

# myset.ensure_index('name',name = 'Myindex',unique = True)

# myindex = myset.list_indexes()
# for i in curson:
print(curson)

conn.close()
