import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import json
import pandas as pd 
import time
import random
from newcasesaverage import rosario

app = Flask(__name__)  # init

@app.route("/")  # Default path
def default():
    return '<h><p style="color:blue"> Aca la API. Para ver los datos, ingresa en tu navegdor el siguiente endpoint: http://localhost:6060/comida_china/?id=A137<h><p style="color:blue">'


@app.route('/get_token/', methods=['GET'])
def give_id():
    x=request.args['id']
    if x == 'A' + str(31+41+36+29):
        return {'token': 'A249191580208185295299619560'}
    else: 
        return 'INCORRECTOOOO - Try again!'


@app.route('/get_data/', methods=['GET'])
def trabajo():
    y=request.args['id']
    if y == 'A249191580208185295299619560':
        answer = rosario(url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv')
        return answer.to_json()    
    else:
        return 'NO WAY'


def main():

    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    
    # Get the settings fullpath
    settings_file = os.path.dirname(__file__) + "/settings.json"
    # Load json from file 
    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")
            
if __name__ == "__main__":
    main()