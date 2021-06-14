from flask import Flask
from src.compara.views import studies 
from src.classify.views import classify
app = Flask(__name__)
app.register_blueprint(studies)
app.register_blueprint(classify)

