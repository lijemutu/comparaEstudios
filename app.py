from flask import Flask, request, jsonify, Response, render_template
from flask_pymongo import PyMongo
from mongoengine import StringField, FloatField
from bson import ObjectId, json_util

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/comparaEstudios"
mongo = PyMongo(app)
#db.init_app(app)


@app.route('/',methods=['GET','POST'])
def Index(): 
    if request.method == 'POST':
        jsonResponse,priceMin = searchBar()
        return render_template("index.html",studies = jsonResponse,priceMin=priceMin)
    else:
        study = mongo.db.studyID.find_one_or_404({"match_study_id":"00655466-77aa-445e-819e-08ee6be61264"})
        ids = study['Study_id']
        studies = mongo.db.studyDB.find({"Study_id":{"$in": ids}})
        response = json_util.dumps(studies)
        jsonResponse = json_util.loads(response)
        priceMin = min([study['Price'] for study in jsonResponse])
        return render_template("index.html",studies = jsonResponse,priceMin=priceMin)


@app.route('/all',methods=['GET'])
def query_all(): 
    #print(request.json)
    allStudies = mongo.db.studyDB.find()
    response = json_util.dumps(allStudies)
    return Response(response=response,mimetype='application/json')

@app.route('/<id>',methods=['GET'])
def find_study(id):
    # Find by match_url_study returns all associated studies
    study = mongo.db.studyID.find_one_or_404({"match_study_id":id})
    ids = study['Study_id']
    studies = mongo.db.studyDB.find({"Study_id":{"$in": ids}})
    response = json_util.dumps(studies)
    jsonResponse = json_util.loads(response)
    priceMin = min([study['Price'] for study in jsonResponse])
    return render_template("index.html",studies = jsonResponse,priceMin=priceMin)


@app.route('/search',methods=['GET','POST'])
def searchBar():
    query = request.form.get('q')
    q = '/'+query+'/i'
    studies = mongo.db.studyID.find({"study_names":{"$in": [q]}})
    studiesList = [s for s in studies]
    #ids = study['Study_id']
    studies = mongo.db.studyDB.find({"Study_id":{"$in": q}})
    response = json_util.dumps(studies)
    jsonResponse = json_util.loads(response)
    priceMin = min([study['Price'] for study in jsonResponse])
    return jsonResponse,priceMin


@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        "message":"Resource not found" + request.url,
        "status": 404
    })
    response.status_code = 404
    return response
if __name__=="__main__":
    
    app.run(debug=True)
