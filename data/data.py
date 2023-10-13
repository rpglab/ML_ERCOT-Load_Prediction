import pandas as pd
import os

select_stations = [121,41,53,96,46,97,33,123]


load_data = pd.read_csv(os.path.join(os.path.dirname(__file__), '2011-2021_reduced.csv'))
load_data['time'] = pd.to_datetime(load_data.time)

dropped = []
for i in select_stations:
    n = str(i)
    load_data['windm'+n] = (load_data['windz'+n]**2 + load_data['windm'+n]**2)**0.5
    load_data = load_data.rename(columns={'windm'+n:'wind'+n})
    dropped += ['windz'+n]

    
load_data['day'] = pd.DatetimeIndex(load_data['time']).day_of_week
load_data['hour'] = pd.DatetimeIndex(load_data['time']).hour
load_data['month'] = pd.DatetimeIndex(load_data['time']).month

load_data = load_data.set_index(['time'])
load_data = load_data.drop(dropped, axis=1)