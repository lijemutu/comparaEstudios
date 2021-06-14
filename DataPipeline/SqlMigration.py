import json
import pyodbc
import pandas as pd



def ReadJsonFiles(file):
    with open(file=file,mode='r',encoding='utf-8') as jsonRead:
        return json.load(jsonRead)

def InsertRecordToStudyTB(db:str,table:str,StudyName:str,Category:str,Description:str):

    ConnectionString = 'DRIVER={ODBC Driver 17 for SQL Server};'\
                                        'Server=ERLOTO;'\
                                        f'Database={db};'\
                                        'Trusted_Connection=yes;'
    with pyodbc.connect(ConnectionString) as CurrentConnection:
        CursorDatabase = CurrentConnection.cursor()
        
        CursorDatabase.execute(f"INSERT INTO dbo.StudyTB (StudyName, Description ,Category)  VALUES (?,?);",(StudyName,Description,Category))
        CursorDatabase.commit()

def InsertManyRecordToStudyTB(db:str,table:str,records:list):
    ConnectionString = 'DRIVER={ODBC Driver 17 for SQL Server};'\
                                        'Server=ERLOTO;'\
                                        f'Database={db};'\
                                        'Trusted_Connection=yes;'
    with pyodbc.connect(ConnectionString) as CurrentConnection:
        CursorDatabase = CurrentConnection.cursor()
        CursorDatabase.fast_executemany = True
        CursorDatabase.executemany(f"INSERT INTO dbo.StudyTB (StudyName, Description,Category)  VALUES (?,?,?);",records)
        CursorDatabase.commit()

def InsertRecordToStudyTB(db:str,table:str,StudyName:str,Category:str):

    ConnectionString = 'DRIVER={ODBC Driver 17 for SQL Server};'\
                                        'Server=ERLOTO;'\
                                        f'Database={db};'\
                                        'Trusted_Connection=yes;'
    with pyodbc.connect(ConnectionString) as CurrentConnection:
        CursorDatabase = CurrentConnection.cursor()
        
        CursorDatabase.execute(f"INSERT INTO dbo.StudyTB (StudyName, Category)  VALUES (?,?);",(StudyName,Category))
        CursorDatabase.commit()

def InsertManyRecordToLaboratoryTB(db:str,records:list):
    ConnectionString = 'DRIVER={ODBC Driver 17 for SQL Server};'\
                                        'Server=ERLOTO;'\
                                        f'Database={db};'\
                                        'Trusted_Connection=yes;'
    with pyodbc.connect(ConnectionString) as CurrentConnection:
        CursorDatabase = CurrentConnection.cursor()
        CursorDatabase.fast_executemany = True
        CursorDatabase.executemany(f"INSERT INTO dbo.LaboratoryTB (Name, Telephone, Location,Website)  VALUES (?,?,?,?);",records)
        CursorDatabase.commit()

def InsertManyRecordToStudiesTB(db:str,table:str,records:list):
    ConnectionString = 'DRIVER={ODBC Driver 17 for SQL Server};'\
                                        'Server=ERLOTO;'\
                                        f'Database={db};'\
                                        'Trusted_Connection=yes;'
    with pyodbc.connect(ConnectionString) as CurrentConnection:
        CursorDatabase = CurrentConnection.cursor()
        CursorDatabase.fast_executemany = True
        CursorDatabase.executemany(f"INSERT INTO dbo.StudiesTB (StudyId, LaboratoryId, Price)  VALUES (?,?,?);",records)
        CursorDatabase.commit()



def MigrateStudyTB():
    studyInfo = ReadJsonFiles('DataPipeline/study_id.json')
    matchStudyToGetCategoryFile = ReadJsonFiles('DataPipeline/classified_data.json')
    studyList = []
    for study in studyInfo:
        elementWithFoundMatch = next(item for item in matchStudyToGetCategoryFile if item['Study_id'] in study['Study_id'] )
        if elementWithFoundMatch['Description'] is None or "":
            elementWithFoundMatch['Description'] = "No description available"
        studyToAppend =(study['study_names'][0],elementWithFoundMatch['Description'],elementWithFoundMatch['Category'])
        studyList.append(studyToAppend)
    InsertManyRecordToStudyTB("EstudiosClinicosDB","dbo.StudyTB",records=studyList)

def FindForeignKeys(db:str,table:str,compareString:str,where:str):
    ConnectionString = 'DRIVER={ODBC Driver 17 for SQL Server};'\
                                        'Server=ERLOTO;'\
                                        f'Database={db};'\
                                        'Trusted_Connection=yes;'
    with pyodbc.connect(ConnectionString) as CurrentConnection:
        CursorDatabase = CurrentConnection.cursor()
        id =CursorDatabase.execute(f"SELECT Id FROM {table} WHERE {where} = ?",(compareString,)).fetchall()
        return id

def MigrateStudiesTB(): 
    
    studies = ReadJsonFiles('DataPipeline/classified_data.json')
    studyList = []

    for study in studies:
        StudyId = FindForeignKeys(db="EstudiosClinicosDB",table="dbo.StudyTB",compareString=study['Study'],where="StudyName")
        if len(StudyId) == 0:
            continue
        LaboratoryId = FindForeignKeys(db="EstudiosClinicosDB",table="dbo.LaboratoryTB",compareString=study['Lab'],where="Name")
        studyToAppend =(StudyId[0][0],LaboratoryId[0][0],study['Price'])
        studyList.append(studyToAppend)
    InsertManyRecordToStudiesTB("EstudiosClinicosDB","dbo.StudiesTB",records=studyList)

# Insert laboratories

# MigrateStudyTB()
MigrateStudiesTB()
# InsertManyRecordToLaboratoryTB("EstudiosClinicosDB",records=\
#     [("Laboratorio Medico Monar","7222148489","PINO SUÁREZ NORTE No. 200, esquina 1° de Mayo, Colonia Sta. Clara, TOLUCA, Estado de México, C.P. 50060",\
#         "http://www.laboratoriomonar.com/"),\
#     ("Olab Diagnósticos Medicos","5547478100","Av. Licenciado Benito Juárez García 761, Real De Arcos, Metepec, Estado de México, México, C.P: 52158. Frente Al Club De Golf San Carlos.",\
#        "https://www.olab.com.mx/"),\
#     ("Laboratorio Médico Polanco","7222151580","Hidalgo 406 - B","https://lmpolanco.com/"),\
#     ("Salud Digna","7222105352","Felipe Berriozabal S/N, entre calle Alfredo Manzo Velez y Alfredo Zarate Albarran, Col. Santa María de las Rosas C.P. 50140. Toluca de Lerdo",\
#         "https://salud-digna.org/")])
