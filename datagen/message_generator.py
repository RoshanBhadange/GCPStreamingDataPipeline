from random import randint
from datetime import datetime

def message_gen():
    trip_id = randint(10000,99999)
    start_time = str(datetime.utcnow())
    start_station_id = randint(200,205)
    bike_no = randint(100,999)
    duration_sec = randint(1000,9999)
    message_json = {'trip_id': trip_id,
                    'start_time': start_time,
                    'start_station_id': start_station_id,
                    'bike_no': bike_no,
                    'duration_sec': duration_sec,
                    }

    return message_json