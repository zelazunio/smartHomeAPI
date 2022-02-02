from flask_restful import Resource, reqparse
from dbFunctions import *


class EnergyCounterGetPulsesByHour(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('startTime', required = False)
        parser.add_argument('endTime', required = False)
        args = parser.parse_args();
        try:
            start_time = int(args.startTime)
        except:
            start_time = 0
        try:
            end_time = int(args.endTime)
        except:
            end_time = datetime.datetime.now().timestamp() * 1000
        return get_energy_counter_pulses_by_hour(start_time, end_time)
    
    
# class EnergyCounterGetPulsesByDay(Resource):
#     def get(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('startTime', required = False)
#         parser.add_argument('endTime', required = False)
#         args = parser.parse_args();
#         try:
#             startTime = int(args.startTime)
#         except:
#             startTime = 0
#         try:
#             endTime = int(args.endTime)
#         except:
#             endTime = datetime.datetime.now().timestamp() * 1000
#         return getEnergyCounterPulsesByDay(startTime, endTime)

class EnergyCounterAddPulses(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('add', required = False)
        args = parser.parse_args()
        try:
            pulses = int(args.add)
            if pulses < 1:
                pulses = 1
        except:
            pulses = 1
        return add_pulses_to_energy_counter(pulses)
         