import json
import re
import uuid
def clean_LMP():
    clean_data = []

    with open('response_laboratorio_medico_polanco.json','r',encoding='utf-8') as responseLMP:
        jsonLMP = json.load(responseLMP)
        for estudioCategoriaName, dict in jsonLMP.items():
            for estudio in dict:
                study = {}
                study['Study'] = estudio['title']
                study['Description'] = estudio['description']
                study['Price'] = float(estudio['price_list'])
                study['Category'] = estudioCategoriaName
                study['Study_id'] = str(uuid.uuid4())
                study['match_study_id'] = ''
                study['Lab'] = 'Laboratorio Medico Polanco'
                clean_data.append(study)
        with open('data_LMP.json', 'w', encoding="utf-8") as outfile:
            json.dump(clean_data, outfile, ensure_ascii=False)


def clean_monar():
    clean_data = []
    with open('response_monar.json','r',encoding='utf-8') as responseMonar:
        jsonMonar = json.load(responseMonar)
        for estudioCategoriaName, dictMonar in jsonMonar.items():
            if estudioCategoriaName == 'electroencefalograma/':
                estudioCategoriaName = 'electroencefalograma'
            for estudioName, estudioInfo in dictMonar.items():
                study = {}
                estudioInfo1 = estudioInfo.split('\t\t\t\t\t')
                study['Study'] = estudioName
                study['Description'] = estudioInfo1[0].strip() + ' '+ estudioInfo1[1].strip()
                study['Price'] = float(re.search(r"[-+]?\d*\.\d+|\d+", estudioInfo1[2].strip()).group())
                study['Category'] = estudioCategoriaName
                study['Study_id'] = str(uuid.uuid4())
                study['match_study_id'] = ''
                study['Lab'] = 'Laboratorio Monar'
                clean_data.append(study)
        with open('data_Monar.json', 'w', encoding="utf-8") as outfile:
            json.dump(clean_data, outfile, ensure_ascii=False)


def clean_olab():
    clean_data = []
    with open('response_olab.json','r',encoding='utf-8') as responseOlab:
        jsonOlab = json.load(responseOlab)
        for estudioCategoriaName, dictOlab in jsonOlab.items():
            if estudioCategoriaName == 'estudios-de-laboratorio':
                estudioCategoriaName = 'analisis-clinicos'
            for estudio in dictOlab:
                study = {}
                study['Study'] = estudio[0]
                study['Description'] = ''
                try:
                    study['Price'] = float(re.search(r"[-+]?\d*\.\d+|\d+", estudio[1].strip()).group())
                except:
                    continue
                
                study['Category'] = estudioCategoriaName
                study['Study_id'] = str(uuid.uuid4())
                study['match_study_id'] = ''
                study['Lab'] = 'Laboratorio Olab'
                clean_data.append(study)
        with open('data_Olab.json', 'w', encoding="utf-8") as outfile:
            json.dump(clean_data, outfile, ensure_ascii=False)
        
def clean_salud_digna():
    clean_data = []
    with open('response_salud_digna.json','r',encoding='utf-8') as responseSD:
        jsonSaludDigna = json.load(responseSD)
        for estudioCategoriaName, dictSD in jsonSaludDigna.items():
            for estudio in dictSD:
                
                study = {}
                study['Study'] = estudio['Descripcion']
                study['Description'] = estudio['Preparacion']
                if estudio['Descuento'] != 0:
                    study['Price'] = round(float(re.search(r"[-+]?\d*\.\d+|\d+", estudio['Precio'].strip()).group()))*(100-float(estudio['Descuento']))/100
                else:
                    study['Price'] = round(float(re.search(r"[-+]?\d*\.\d+|\d+", estudio['Precio'].strip()).group())*1.16)
                study['Category'] = estudioCategoriaName
                study['Study_id'] = str(uuid.uuid4())
                study['match_study_id'] = ''
                study['Lab'] = 'Laboratorio Salud Digna'
                clean_data.append(study)
        with open('data_salud_digna.json', 'w', encoding="utf-8") as outfile:
            json.dump(clean_data, outfile, ensure_ascii=False)

def joinFiles():
    with open("data_LMP.json",'r',encoding='utf-8') as lmpData:
        with open("data_Olab.json",'r',encoding='utf-8') as olabData:
            with open("data_Monar.json",'r',encoding='utf-8') as monarData:
                with open("data_salud_digna.json",'r',encoding='utf-8') as sdData:
                    result = []
                    lmpData = json.load(lmpData)
                    olabData = json.load(olabData)
                    monarData = json.load(monarData)
                    sdData = json.load(sdData)

                    for study in lmpData:
                        result.append(study)

                    for study in olabData:
                        result.append(study)

                    for study in monarData:
                        result.append(study)

                    for study in sdData:
                        result.append(study)
                    
                    with open("dataLab.json","w",encoding='utf-8') as res:
                        json.dump(result,res,ensure_ascii=False)

if __name__ == "__main__":
    joinFiles()