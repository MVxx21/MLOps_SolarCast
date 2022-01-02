'''
inputs: month, day, Daily_Temp, Daily_Precip, Daily_Humidity, Daily_Pressure, Daily_WindDir,
        Daily_WindSpeed, Daily_DNI, Daily_DHI

output: Daily_radiation
'''

# import modules
from flask import Flask, jsonify, request
import numpy as np
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_input():
    '''
    Flask script to interface between user request and ml model selected during POC    
    '''
    # load packets
    packet = request.get_json(force=True)
    
    # extract and reshape input data
    input_data = list(packet.values())

    # reshape data
    data = np.array(input_data).reshape(1, 10)

    # load the ml model
    model_path = 'app/model_rfr.pkl'
    model = joblib.load(model_path)

    # generate prediction
    solar_irr = model.predict(data)[0]

    return jsonify(packet, {'Solar irradiation':solar_irr})