from app import app
from polyglot.detect import Detector
from flask import request
import json

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/languageDetect', methods=['POST']) #GET requests will be blocked
def languageDetect():
    req_data = request.get_json()
    
    try:
        detector = Detector(req_data['text'])

        data = {}
        data["name"] = detector.language.name
        data["code"] = detector.language.code
        data["confidence"] = detector.language.confidence
        
        if data.get["name"] == "":
            print(req_data)

    except:
        print(req_data)

    return '''
            {}'''.format(json.dumps(data))

@app.route('/multipleLang', methods=['POST']) #GET requests will be blocked
def multipleLang():
    req_data = request.get_json()
    
    response = ""
    
    list = []
    
    for language in Detector(req_data['text']).languages:
          #response += str(language) + "\n"
          data = {}
          data["name"] = language.name
          data["code"] = language.code
          data["confidence"] = language.confidence
          list.append(data)

    print(list)
    return '''
             {}'''.format(list)
