import pymongo
from bson.objectid import ObjectId
import time
import datetime
client = pymongo.MongoClient("mongodb+srv://admin:Kiennguyen98@cluster0-ic9nh.mongodb.net/test?retryWrites=true&w=majority")
db = client.Allteam
db1 = client.thisweek
def get_all():
   l2=[]
   list1 = db.lichdau11.find()
   for v in list1:     
      a=v["lichdau"]
      for b in a: 
         tonghop={}   
         c = b["time"]
         doi1=b["doi"][0]
         doi2=b["doi"][1]
         tonghop["team1"]=doi1
         tonghop["team2"]=doi2
         tonghop["time"]=c
         l2.append(tonghop)
   return list(l2)   
def clear_data():
   db1.thisweek1.drop()
def clear_data2():
   db.lichdau11.drop()
def insert_data(a,b):
       db.lichdau11.insert_one({'Đội':a,'lichdau':b})
def insert(thisweek1):
   db1.thisweek1.insert_one({"Tuần này":thisweek1})
def insert_lineup(a,b,c,d):
    db.lineup.insert_one({'Đội':a,'lineup':b,'result':c,'img':d})
def clear_database():
    db.lineup.drop()
def match_this_week():
   tw=[]
   l1=db1.thisweek1.find()
   for v in l1:
      a=v["Tuần này"]
      for b in a:
         tonghop={}
         team1=b["team1"]
         team2=b["team2"]
         time=b["time"]
         stadium=b["stadium"]
         logo1=b["logo1"]
         logo2=b["logo2"]
         tonghop["team1"]=team1
         tonghop["team2"]=team2
         tonghop["time"]=time
         tonghop["stadium"]=stadium
         tonghop["logo1"]=logo1
         tonghop["logo2"]=logo2
         count=0
         for m in tw:
            if m==tonghop:
               count=count+1
         if count==0:
            tw.append(tonghop)
   return(tw)

