import pyodbc
import json


def GetMatchedStudies(db: str = "EstudiosClinicosDB", name: str = "", StudyId: int = 0):
    ConnectionString = 'DRIVER={ODBC Driver 17 for SQL Server};'\
        'Server=ERLOTO;'\
        f'Database={db};'\
        'Trusted_Connection=yes;'
    with pyodbc.connect(ConnectionString) as CurrentConnection:
        CursorDatabase = CurrentConnection.cursor()
        if name != "":
            return
        if StudyId != 0:
            Studies = CursorDatabase.execute(f""" 
            SELECT StudiesTB.Price,StudyTB.StudyName,LaboratoryTB.Name, StudyTB.Category, LaboratoryTB.Website,LaboratoryTB.Telephone  FROM StudiesTB
            INNER JOIN StudyTB ON StudiesTB.StudyId = StudyTB.Id
            INNER JOIN LaboratoryTB ON StudiesTB.LaboratoryId = LaboratoryTB.Id
            WHERE StudyTB.Id = ?""", (StudyId,)).fetchall()

            formattedStudies = [{'Study': name, 'Price': int(price), 'Lab': lab, 'Category': category, 'LabWebsite': website,
                                 'LabTelephone': telephone} for price, name, lab, category, website, telephone in Studies]
            priceMin = min([study['Price'] for study in formattedStudies])
            formattedStudiesWithPrice = {
                'Studies': formattedStudies, 'PriceMin': priceMin}
            return formattedStudiesWithPrice


def ViewNonClassifiedStudies(db: str = "EstudiosClinicosDB"):
    from itertools import groupby
    from operator import itemgetter


    with open("DataPipeline\classified_data.json", 'r', encoding='utf-8') as toBeClassified:
        toBeClassified = json.load(toBeClassified)
        nonClassified = [
            study for study in toBeClassified if study['match_study_id'] == '']
        INFO = sorted(nonClassified, key=itemgetter("Category"))
    
        byCategory = [{key:list(value)} for key,value in groupby(INFO, itemgetter("Category"))]
        # for key, value in groupby(INFO, itemgetter("category")):
        #     print(key)
        #     print(list(value))
        return byCategory

