import json
from uuid import UUID

def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.
    
     Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}
    
     Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.
    
     Examples
    --------
    >>> is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')
    True
    >>> is_valid_uuid('c9bf9e58')
    False
    """
    
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test

def queryResults(match_study_id,dbFile,idFile):
    with open(dbFile,'r',encoding='utf-8') as db:    
        with open(idFile,'r',encoding='utf-8') as study_id_file:
            if is_valid_uuid(match_study_id) == True:
                # Find by match_study_id
                db = json.load(db)
                ids = json.load(study_id_file)

                match_study_ids = [study['Study_id'] for study in ids if study['match_study_id'] == match_study_id][0]
                items = [study for study in db if study['Study_id'] in match_study_ids]
                return items
            else:
                raise Exception("Not a valid study identifier")

if __name__ == "__main__":
    match_study_id = "cc071adc-477b-4f24-a711-9ae3a3701dbe"
    dbFile = "classified_data.json"
    idFile = "study_id.json"
    resultItems =queryResults(match_study_id,dbFile,idFile)
    print(resultItems)