from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS, cross_origin

from apiResources import *
from gpio import *

import logging

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Content-Type"

logging.basicConfig(filename = 'work.log', format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.info('------------>> Program started')

db.bind('sqlite', '/home/pi/projektyPython/smartHome/database.sqlite', create_db = True)
db.generate_mapping(create_tables=True)

api.add_resource(EnergyCounterAddPulses, '/EnergyCounterAddPulses')
api.add_resource(EnergyCounterGetPulsesByHour, '/EnergyCounterGetPulsesByHour')
#api.add_resource(EnergyCounterGetPulsesByDay, '/EnergyCounterGetPulsesByDay') 
  
config_gpio()
logging.info('GPIO configured')
logging.info('Starting server')

if __name__ == '__main__':
    app.run(debug = False, host='0.0.0.0')
 
#prev = 0
#while True:
#    continue
    #if GPIO.input(23) != prev:
    #    print(GPIO.input(23))
    #    prev = GPIO.input(23)
