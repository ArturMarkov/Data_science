from datetime import datetime
import os
import glob
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#%matplotlib inline

INDEX = {
    1: 24,  # newindex:NOAAindex
    2: 25,  # INDEX[newindex]>>NOAAindex
    3: 5,
    4: 6,
    5: 27,
    6: 23,
    7: 26,
    8: 7,
    9: 11,
    10: 13,
    11: 14,
    12: 15,
    13: 16,
    14: 17,
    15: 18,
    16: 19,
    17: 21,
    18: 22,
    19: 8,
    20: 9,
    21: 10,
    22: 1,
    23: 3,
    24: 2,
    25: 4,

}


def data_delimer(line):
    if '/' in line:
        return ''
    line = line.replace(' ', ',', 2)
    return (line + '\n')

def load_all_data_to_pd(path):
    df = pd.DataFrame(
        columns=['Year', 'Week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI'])
    for file in glob.glob(os.path.join(path, "province-*.csv")):
        temp = pd.read_csv(file, header=0)
        #specify province
        temp['Province'] = file.split('-')[1].split(".")[0]
        df = df.append(temp, ignore_index=True)

       #change types for memory saving
        df['Province'] = df['Province'].astype("int32")
    #chagne colums consequence
    df = df[['Year', 'Week', 'Province', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI']]

    return df

    
#df = load_all_data_to_pd("D:\python_data_science\lab1\data")


   {"type": 'dropdown',
    "label": "Choose Year",
    "options": [{'label': str(i), 'value': i} for i in range(1982, 2020)],
    'key': 'year',
    'value': '1982'
        },
        
        {
            "type":'slider',
            "label":'Choose min_week',
            "action_id":"min_week"
        },
        {
            "type": 'slider',
            "label": 'Choose maxn_week',
            "action_id": "max_week"
        }


f = df[df.Year == Year].filter(['Year', 'Week', 'VHI', 'TCI', 'VCI'])
        final = f[(f['Week'] >= float(min_week)) &
                  (f['Week'] <= float(max_week))]
        final['Week'] = final['Week'].astype(int)
        final['Week'] = final['Week'].astype(str)




(ds_lab1_2) D:\python_data_science>C:/Users/PK/anaconda3/envs/ds_lab1_2/python.exe d:/python_data_science/lab2/lab2.py 
WARNING:root:Warning: unable to set defaultencoding to utf-8
[24/Apr/2020:23:01:12] ENGINE Listening for SIGTERM.
INFO:cherrypy.error:[24/Apr/2020:23:01:12] ENGINE Listening for SIGTERM.
[24/Apr/2020:23:01:12] ENGINE Bus STARTING
INFO:cherrypy.error:[24/Apr/2020:23:01:12] ENGINE Bus STARTING
CherryPy Checker:
The Application mounted at '' has an empty config.



"options": [
            {"label": "VCI", "value": "VCI"},
            {"label": "TCI", "value": "TCI"},
            {"label": "VHI", "value": "VHI"},
            {"label": "all the above", "value": "all"}
        ],
        "key": 'choose_by',


    },
        {
        "type": "dropdown",
            "label": "Choose province",
            "options": [
                {"label": "Вінницька", "value": 1},
                {"label": "Волинська", "value": 2},
                {"label": "Дніпропетровська", "value": 3},
                {"label": "Донецька", "value": 4},
                {"label": "Житомирська", "value": 5},
                {"label": "Закарпатська", "value": 6},
                {"label": "Запорізька", "value": 7},
                {"label": "Івано-Франківська", "value": 8},
                {"label": "Київська", "value": 9},
                {"label": "Кіровоградська", "value": 10},
                {"label": "Луганська", "value": 11},
                {"label": "Львівська", "value": 12},
                {"label": "Миколаївська", "value": 13},
                {"label": "Одеська", "value": 14},
                {"label": "Полтавська", "value": 15},
                {"label": "Рівенська", "value": 16},
                {"label": "Сумська", "value": 17},
                {"label": "Тернопільська", "value": 18},
                {"label": "Харківська", "value": 19},
                {"label": "Херсонська", "value": 20},
                {"label": "Хмельницька", "value": 21},
                {"label": "Черкаська", "value": 22},
                {"label": "Чернівецька", "value": 23},
                {"label": "Чернігівська", "value": 24},
                {"label": "Республіка Крим", "value": 25}
