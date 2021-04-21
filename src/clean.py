import json
import re
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
                study['Study_id'] = ''
                clean_data.append(study)
        with open('data_LMP.json', 'w', encoding="utf-8") as outfile:
            json.dump(clean_data, outfile, ensure_ascii=False)


def clean_monar():
    clean_data = []
    with open('response_monar.json','r',encoding='utf-8') as responseMonar:
        jsonMonar = json.load(responseMonar)
        for estudioCategoriaName, dict in jsonMonar.items():
            for estudioName, estudioInfo in dict.items():
                study = {}
                estudioInfo1 = estudioInfo.split('\t\t\t\t\t')
                study['Study'] = estudioName
                study['Description'] = estudioInfo1[0].strip() + ' '+ estudioInfo1[1].strip()
                study['Price'] = float(re.search(r"[-+]?\d*\.\d+|\d+", estudioInfo1[2].strip()).group())
                study['Category'] = estudioCategoriaName
                study['Study_id'] = ''
                clean_data.append(study)
        with open('data_Monar.json', 'w', encoding="utf-8") as outfile:
            json.dump(clean_data, outfile, ensure_ascii=False)

if __name__ == "__main__":
    clean_monar()