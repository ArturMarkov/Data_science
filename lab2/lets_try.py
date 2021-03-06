import sys
import os
import pandas as pd
from spyre import server


class SimpleApp(server.App):
    title = "Lab2"
# VCI, TCI, VHI
    inputs = [{
        "type": "dropdown",
        "label": "Choose data",
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
            "options":
            [
                {"label": "Vinnytska", "value": 1},
                {"label": "Volinska", "value": 2},
                {"label": "Dnipropetrovska", "value": 3},
                {"label": "Donetska", "value": 4},
                {"label": "Zhytomyrska", "value": 5},
                {"label": "Zakarpattya", "value": 6},
                {"label": "Zaporizka", "value": 7},
                {"label": "Ivano-Frankivska", "value": 8},
                {"label": "Kyivska", "value": 9},
                {"label": "Kyrovohradska", "value": 10},
                {"label": "Luganska", "value": 11},
                {"label": "Lvivska", "value": 12},
                {"label": "Mykolaivska", "value": 13},
                {"label": "Odeska", "value": 14},
                {"label": "Poltavska", "value": 15},
                {"label": "Rivnenska", "value": 16},
                {"label": "Sumska", "value": 17},
                {"label": "Ternopilska", "value": 18},
                {"label": "Kharkyvska", "value": 19},
                {"label": "Khersonska", "value": 20},
                {"label": "Khmelnitska", "value": 21},
                {"label": "Cherkaska", "value": 22},
                {"label": "Chernivetska", "value": 23},
                {"label": "Chernihivska", "value": 24},
                {"label": "Crimean", "value": 25}],
        'key': 'province',
        'value': '1'


    },
        {"type": 'dropdown',
         "label": "Choose Year",
         "options": [{'label': str(i), 'value': i} for i in range(1982, 2020)],
            'key': 'year',
            'value': '1982'
         },
        {
            "type": 'slider',
            "label": 'Choose min_week',
            "key": "min_week",
            "value": '10'
    },
        {
            "type": 'slider',
            "label": 'Choose max_week',
            "key": "max_week",
            "value": '52'
    }
    ]

    outputs = [
        {'type': 'table',
            'id': 'table1',
            'control_id': "button1",
            'tab': 'Table'
         },
        {'type': 'plot',
            'id': 'plot1',
            'control_id': "button1",
            'tab': 'Plot'
         }]

    controls = [{"type": "button",
                 "label": "show data",
                 "id": "button1"}]

    tabs = ['Table', 'Plot']

    def getData(self, params):

        year = params['year']
        pr = params['province']

        path = os.path.normpath(f"lab2/data/province-{pr}.csv")
        #min_week = params['min_week']
        #max_week = params['max_week']
        df = pd.read_csv(path, header=0)
        #df = pd.read_csv(path, sep='[, ]+', engine='python')
        # = df[df.Year == year]
        # если не str() то FutureWarning: elementwise comparison failed;
        # returning scalar,
        # but in the future will perform elementwise comparison
        #p = df[df["Year"] == int(year)]
        return df

    def getPlot(self, params):
        df = self.getData(params)
        return df.set_index(df['Week']).plot()


app = SimpleApp()
app.launch()
