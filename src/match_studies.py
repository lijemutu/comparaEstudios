from fuzzywuzzy import fuzz
import json

def write_to_file(name,data):
    with open(name,"w",encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)


def two_study_classifier(raw_read_data_1,raw_read_data_2,outfile1,outfile2,counter):
    data1 = json.load(raw_read_data_1)
    data2 = json.load(raw_read_data_2)
    for study1 in data1:
        if study1['Study_id'] =="":
            for study2 in data2:
                if study2['Study_id'] =="":
                    estudio =f"study on 1: {study1['Study']} ${study1['Price']}\n Category: {study1['Category']}\n study on 2: {study2['Study']} ${study2['Price']}\n Category: {study2['Category']}"
                    valor = fuzz.partial_ratio(study1['Study'].lower(), study2['Study'].lower())
                    if valor > 85:
                        assign = str(input('Coinciden?:\n'+estudio+' valor: '+str(valor)+'\n'))
                        if assign.lower() == 'y':
                            study1['Study_id'] = counter
                            study2['Study_id'] = counter
                            counter+=1
                            break
                        if assign.lower() == 'b':
                            write_to_file(name=outfile1,data=data1)
                            write_to_file(name=outfile2,data=data2)
                        else:
                            continue
    write_to_file(name=outfile1,data=data1)
    write_to_file(name=outfile2,data=data2)
    return counter

def match_studies():
    with open("data_LMP.json",'r',encoding='latin-1') as lmpData:
        with open("data_Olab.json",'r',encoding='latin-1') as olabData:
            with open("data_Monar.json",'r',encoding='utf-8') as monarData:
                with open("data_salud_digna.json",'r',encoding='utf-8') as sdData:
        
        
                    new_counter =two_study_classifier(raw_read_data_1=monarData,raw_read_data_2=sdData,outfile1="monar_classified.json",outfile2="salud_digna_classified.json",counter=1)


                    
if __name__ == "__main__":
    match_studies()