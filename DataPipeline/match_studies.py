from fuzzywuzzy import fuzz
import json
import uuid
import os
import itertools as it
from textwrap import dedent
from random import shuffle
def write_to_file(name,data):
    with open(name,"w",encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

def add_match_id(study1,study2):
    if not os.path.exists("study_id.json"):
        with open("study_id.json","w"):
            pass

    with open("study_id.json","r",encoding='utf-8') as study_id_table:
        try:
            existing_ids = json.load(study_id_table)
            if type(existing_ids) is dict:
                existing_ids = [existing_ids]

            if study1['match_study_id'] !='':
                study2['match_study_id'] = study1['match_study_id']
                temp = next(study for study in existing_ids if study['match_study_id']==study1['match_study_id'])
                temp['study_names'].append(study2['Study'])
                temp['Study_id'].append(study2['Study_id'])

            if study2['match_study_id'] !='':
                study1['match_study_id'] = study2['match_study_id']
                temp = next(study for study in existing_ids if study['match_study_id']==study2['match_study_id'])
                temp['study_names'].append(study1['Study'])
                temp['Study_id'].append(study1['Study_id'])
            

            else:
                idStudy = str(uuid.uuid4())
                study1['match_study_id'] = idStudy
                study2['match_study_id'] = idStudy
            
                study ={
                    "study_names":[study1['Study'],study2['Study']],
                    "match_study_id": idStudy,
                    "Study_id": [study1['Study_id'],study2['Study_id']]
                }

            
                existing_ids.append(study)
        except:
            existing_ids = []
            idStudy = str(uuid.uuid4())
            study1['match_study_id'] = idStudy
            study2['match_study_id'] = idStudy
        
            study ={
                "study_names":[study1['Study'],study2['Study']],
                "match_study_id": idStudy,
                "Study_id": [study1['Study_id'],study2['Study_id']]
            }

        
            existing_ids.append(study)
        
    with open("study_id.json","w",encoding='utf-8') as study_id_table:
        #except:
        #    pass
        json.dump(existing_ids,study_id_table, ensure_ascii=False)


    
def two_study_classifier(inputData,outData):
    data = json.load(inputData)
    shuffle(data)
    for study1,study2 in it.combinations(data,2):
        if study1['match_study_id']=='' and study1['Lab']!=study2['Lab']:
                
            estudio =f"""\
            study on 1: {study1['Study']} ${study1['Price']}
            Category: {study1['Category']}
            Lab: {study1['Lab']}\n
            study on 2: {study2['Study']} ${study2['Price']}
            Category: {study2['Category']}
            Lab: {study2['Lab']}\n
            """
            valor = fuzz.partial_ratio(study1['Study'].lower(), study2['Study'].lower())
            if valor > 85:
                assign = str(input('Coinciden?:\n'+dedent(estudio)+'valor: '+str(valor)+'\n'))
                if assign.lower() == 'y':
                    add_match_id(study1,study2)                                
                    continue
                if assign.lower() == 'b':
                    write_to_file(name=outData,data=data)
                    break
                else:
                    continue
    write_to_file(name=outData,data=data)

def match_studies():
    try:
        with open("classified_data.json",'r',encoding='utf-8') as labData:
            two_study_classifier(inputData=labData,outData="classified_data.json")
    except:
        with open("dataLab.json",'r',encoding='utf-8') as labData:
            two_study_classifier(inputData=labData,outData="classified_data.json")


                    
if __name__ == "__main__":
    match_studies()