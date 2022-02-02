import datetime

from dbModels import *


def get_energy_counter_pulses_by_hour(start_time=0, end_time=0):
    with db_session:
        query = select(((str(i.date.year) + '-' + str(i.date.month) + '-' + str(i.date.day) + ' ' + str(i.date.hour)),
                        sum(i.pulses))
                        for i in EnergyCounterPulses
                         if i.date >= datetime.fromtimestamp(start_time / 1000.0) and
                         i.date < datetime.fromtimestamp(end_time / 1000.0))
        entities = {'pulsesByHour': {}}  
        for e in query:
            strptime = datetime.strptime(e[0], "%Y-%m-%d %H")
            timestamp = int(datetime.timestamp(strptime))
            entities['pulsesByHour'][timestamp] = e[1];
        return entities


# def getEnergyCounterPulsesByDay(startTime=0, endTime=0):
#     with db_session:
#         querry = select(((str(i.data.year) + '-' + str(i.data.month) + '-' + str(i.data.day)), sum(i.impulsy))
#                         for i in EnergyCounterPulses
#                         if i.data >= datetime.datetime.fromtimestamp(startTime / 1000.0) and
#                         i.data < datetime.datetime.fromtimestamp(endTime / 1000.0))
#         entities = {}
#         for e in querry:
#             dateElements = e[0].replace('-', ',')
#             dateElements = dateElements.replace(' ', ',')
#             dateElementsList = dateElements.split(',')
#             entities[str(datetime.datetime(int(dateElementsList[0]), int(dateElementsList[1]),
#                                            int(dateElementsList[2])))] = {'pulses': e[1]}
#         return entities
#

def add_pulses_to_energy_counter(pulses=1):
    with db_session:
        try:
            item = EnergyCounterPulses(date=datetime.datetime.now(), pulses=pulses)
            print(datetime.datetime.now())
            return {'pulsesAdded': pulses}, 200
        except:
            print('Error adding to db')
            return {'Error adding pulses to database'}, 200
