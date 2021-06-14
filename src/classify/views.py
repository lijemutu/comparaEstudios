from flask import Blueprint, request, render_template
from src.Models.Products import ViewNonClassifiedStudies
classify = Blueprint('classify', __name__)


@classify.route("/classify", methods=['GET'])
def ToClassify():
    nonClassifiedStudies = ViewNonClassifiedStudies()
    return render_template("classify.html", studies=nonClassifiedStudies)
