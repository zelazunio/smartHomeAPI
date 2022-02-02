from dbModels import *
import datetime

'''def energyCounterPulsesByHourQuerryNoLimit():
    return select(((str(i.data.year) + '-' + str(i.data.month) + '-' + str(i.data.day) + ' ' + str(
                i.data.hour)), sum(i.impulsy)) for i in EnergyCounterPulses).order_by(lambda: desc((str(i.data.year) + '-' + str(i.data.month) + '-' + str(i.data.day) + ' ' + str(
                i.data.hour))))
    
    
def energyCounterPulsesByHourQuerryWithLimit(resultsLimit):
    return select(((str(i.data.year) + '-' + str(i.data.month) + '-' + str(i.data.day) + ' ' + str(
                i.data.hour)), sum(i.impulsy)) for i in EnergyCounterPulses).order_by(lambda: desc((str(i.data.year) + '-' + str(i.data.month) + '-' + str(i.data.day) + ' ' + str(
                i.data.hour)))).limit(resultsLimit)

def getEnergyCounterPulsesByHour(startTime = 0, endTime = 0):
    with db_session:
            if resultsLimit > 0:
                querry = energyCounterPulsesByHourQuerryWithLimit(resultsLimit)
            else:
                querry = energyCounterPulsesByHourQuerryNoLimit()
            entities = {}
            for e in querry:
                dateElements = e[0].replace('-',',')
                dateElements = dateElements.replace(' ',',')
                dateElementsList = dateElements.split(',')
                entities[str(datetime.datetime(int(dateElementsList[0]),int(dateElementsList[1]),int(dateElementsList[2]),int(dateElementsList[3])))] = {'pulses': e[1]}
            return entities
'''

def getEnergyCounterPulsesByHour(startTime = 0, endTime = 0):
    with db_session:
        querry = select(((str(i.data.year) + '-' + str(i.data.month) + '-' + str(i.data.day) + ' ' + str(i.data.hour)),sum(i.impulsy))
                        for i in EnergyCounterPulses
                        if i.data >= datetime.datetime.fromtimestamp(startTime / 1000.0) and
                        i.data < datetime.datetime.fromtimestamp(endTime / 1000.0))
        entities = {}
        for e in querry:
                dateElements = e[0].replace('-',',')
                dateElements = dateElements.replace(' ',',')
                dateElementsList = dateElements.split(',')
                entities[str(datetime.datetime(int(dateElementsList[0]),int(dateElementsList[1]),int(dateElementsList[2]),int(dateElementsList[3])))] = {'pulses': e[1]}
        return entities
    
def getEnergyCounterPulsesByDay(startTime = 0, endTime = 0):
    with db_session:
        querry = select(((str(i.data.year) + '-' + str(i.data.month) + '-' + str(i.data.day)),sum(i.impulsy))
                        for i in EnergyCounterPulses
                        if i.data >= datetime.datetime.fromtimestamp(startTime / 1000.0) and
                        i.data < datetime.datetime.fromtimestamp(endTime / 1000.0))
        entities = {}
        for e in querry:
                dateElements = e[0].replace('-',',')
                dateElements = dateElements.replace(' ',',')
                dateElementsList = dateElements.split(',')
                entities[str(datetime.datetime(int(dateElementsList[0]),int(dateElementsList[1]),int(dateElementsList[2])))] = {'pulses': e[1]}
        return entities
    
def addPulsesToEnergyCounter(pulses = 1):
    with db_session:
        try:
            item = EnergyCounterPulses(data = datetime.datetime.now(), impulsy = pulses)
            print(datetime.datetime.now())
            return {'pulsesAdded': pulses}, 200
        except:
            print('Error adding to db')
            return {'Error adding pulses to database'}, 200
