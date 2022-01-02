'''
inputs: month, day, daily_temp, daily_precip, daily_humidity, daily_pressure, daily_windDir,
        daily_windSpeed, daily_DNI, daily_DHI

output: daily_radiation
'''

# import modules
from flask import Flask, app, jsonify, request
import numpy as np
import joblib as jl

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_input():
    '''
    Flask script to interface between user request and ml model selected during POC    
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