from app import app
from flask import render_template
from flask import request
from flask_swagger_ui import get_swaggerui_blueprint
#import pandas

@app.route('/')
def home():
   return "hello no  world!"

@app.route('/template',methods=['POST','GET'])
def template():
    output = request.args.values()
    return render_template('home.html',prediction_text="Listen to me... In this world, wherever there is light, there are always shadows. As long as there is a concept of victory, the vanquished will also exist. The selfish desire for peace give rise to war. And hatred is born in order to protect love. Wouldn't you agree {}?".format(list(output)[:]))
    

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

@app.route("/static/swagger.json")
def specs():
    return send_from_directory(os.getcwd(), "swagger.json")

@app.route('/predict')
def predict():
    return render_template('index.html')


