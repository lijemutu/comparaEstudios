from flask import Blueprint,request,render_template
from src.Models.Products import GetMatchedStudies

studies = Blueprint('studies',__name__)

@studies.route('/',methods=['GET'])
def Index(): 
    popularStudiesId = [79,84,87,92,104,108,124]
    multipleStudies = [GetMatchedStudies(StudyId=studyId) for studyId in popularStudiesId]
    
    return render_template("index.html",studies = multipleStudies)