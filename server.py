import flask
from flask import *
import wikipedia
import spacy
from spacy import displacy
from waitress import serve

app = flask.Flask(__name__)
#app.config["DEBUG"] = True


nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/server',methods=['POST'])
def hello_name():
    if request.method=='POST':
        data=request.form.get('data')
        #print(data)
        result = wikipedia.summary(data) 
        doc = nlp(result)
        return displacy.render(doc, style="ent")
    #return displacy.render(doc, style="ent")
    #return 

serve(app,host='127.0.0.1', port=8000)