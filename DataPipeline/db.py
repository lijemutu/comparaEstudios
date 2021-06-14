from pymongo import MongoClient
import json
import pprint
import os
def createDB():

    with MongoClient('localhost', 27017) as client:
        print(os.getcwd())
        db = client['comparaEstudios']
        with open('classified_data.json','r',encoding='utf-8') as data:
            data = json.load(data)
        studyDBCollection = db.studyDB
        studyDBCollection.insert_many(data)
        with open('study_id.json','r',encoding='utf-8') as study_id:
            study_id =json.load(study_id)
        studyIDCollection = db.studyID
        studyIDCollection.insert_many(study_id)

def readDB():
    with MongoClient('localhost', 27017) as client:
        db = client['comparaEstudios']
        studies = db.studyDB
        for doc in studies.find():
            pprint.pprint(doc)

def updateDB():
    with MongoClient('localhost', 27017) as client:
        db = client['comparaEstudios']
        studies = db.studyDB
        with open('classified_data.json','r',encoding='utf-8') as data:
            data = json.load(data)
        for doc in data:
            query = {'Study_id':doc['Study_id']}
            updateValues = {"$set":{"key1":doc['key1'],
                                    "key2":doc['key2']}}

            studies.update_one(query,updateValues)
            


if __name__ == "__main__":
    createDB()