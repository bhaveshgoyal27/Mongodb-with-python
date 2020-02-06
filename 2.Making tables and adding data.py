from pymongo import MongoClient                
democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]   #creating DB
mycoll=mydb["dbtable"]    #creating Table

mylist = [
  { "id": 1, "name": "John", "address": "Highway 37"},
  { "id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "id": 3, "name": "Amy", "address": "Apple st 652"},
  { "id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "id": 5, "name": "Michael", "address": "Valley 345"},
  { "id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "id": 8, "name": "Richard", "address": "Sky st 331"},
  { "id": 9, "name": "Susan", "address": "One way 98"},
  { "id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "id": 12, "name": "William", "address": "Central st 954"},
  { "id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycoll.insert_many(mylist) #inserting many data in the table
y = mycoll.insert_one(mylist[0]) #to insert one set of data in the table

dblist = myclient.list_database_names()
if input('Enter DB') in dblist:
    print("The database exists.")
else:
    print("Not Present")

print(dblist)
