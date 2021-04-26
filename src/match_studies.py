from fuzzywuzzy import fuzz
import json

def write_to_file(name,data):
    with open(name,"w",encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
def match_studies():
    with open("log.txt",'w',encoding='latin-1') as log:
        with open("data_LMP.json",'r',encoding='latin-1') as lmpData:
            with open("data_Olab.json",'r',encoding='latin-1') as olabData:
                with open("data_Monar.json",'r',encoding='latin-1') as monarData:
                    with open("data_salud_digna.json",'r',encoding='latin-1') as sdData:
            
                        lmp = json.load(lmpData)
                        olab = json.load(olabData)
                        monar = json.load(monarData)
                        sd = json.load(sdData)
                        i = 1
                        for studylmp in lmp:
                            if studylmp['Study_id'] == "":

                                for studyOlab in olab:
                                    estudio =f"study on LMP: {studylmp['Study']} ${studylmp['Price']} study on Olab: {studyOlab['Study']} ${studyOlab['Price']}"
                                    valor = fuzz.partial_ratio(studylmp['Study'].lower(), studyOlab['Study'].lower())
                                    if valor > 85:
                                        assign = str(input('Coinciden?:\n'+estudio+' valor: '+str(valor)+'\n'))
                                        if assign.lower() == 'y':
                                            studylmp['Study_id'] = i
                                            studyOlab['Study_id'] = i
                                            i+=1
                                            break
                                        if assign.lower() == 'b':
                                            write_to_file(name="classified_LMP.json",data=lmp)
                                        else:
                                            continue

                        write_to_file(name="classified_LMP.json",data=lmp)


                    
if __name__ == "__main__":
    match_studies()