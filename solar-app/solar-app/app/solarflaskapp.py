'''

'''

# import modules
import re
from flask import Flask, app, jsonify, request
import numpy as np
import joblib as jl

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_input():
    '''
    
    '''
    # load packets
    packet=request.get_json(force=True)
    
    # extract and reshape input data
    input_data=list(packet.values())

    # reshape data
    data=np.array(input_data.reshape(1, 10))

    # load the ml model
    model_path='app/model_rfr.plk'
    model=jl.load(model_path)

    # generate prediction
    solar_irr=model.predict(data)[0]

    return jsonify('solar irradiation': solar_irr)