# first have to install pymongo by the command  "pip install pymongo"

import pymongo
myclient  = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db=myclient["MovieDB"]
coll=db["movie"]

for i in coll.find():
    print("name: ",i['name'])
    print("img : ",i['img'])
    print("summary: ",i['Summary'],"\n")
print("...............Done.............")
