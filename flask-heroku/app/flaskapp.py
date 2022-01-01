# import function and modules
from app.bmicalc import bmi_calculator
from flask import Flask, jsonify, request

# instantiate a flask object
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def get_inputs():
    '''
    Function gets request using flask and return the result of the funtion bmi_calculator()
    '''

    packet = request.get_json(force=True)
    weight = packet['weight']
    height = packet['height']

    bmi = bmi_calculator(weight, height)

    return jsonify(packet, bmi)