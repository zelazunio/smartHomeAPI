from pony.orm import *
from datetime import datetime

set_sql_debug(False)

db = Database()


class EnergyCounterPulses(db.Entity):
    _table_ = 'EnergyCounterPulses'

    date = Required(datetime)
    pulses = Required(int)