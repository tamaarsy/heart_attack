import pandas as pd

from flask import Flask, request, jsonify
import pickle
from class_mixin import selectionFiture
import __main__

__main__.selectionFiture = selectionFiture

app = Flask(__name__)



with open("fix_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


@app.route("/", methods=['POST'])
def model_prediction():
    content = request.json
    print(content)
    
    feature_new = pd.DataFrame(content, index=[0])
    
    predict = model.predict(feature_new)
    classes = ['Tidak Terjangkit', 'Terjangkit']
    responses = {'status' : 'success',
                 'code' : 200,
                 'data' :{'result': classes[predict[0]]}
                }
    print(f'response {responses}')
    #print(f'jno : {jsonify(responses)}')
    return jsonify(responses)

#app.run(debug=True)


