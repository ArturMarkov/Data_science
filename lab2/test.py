from spyre import server
import pandas as pd


class MyApp(server.App):
    title = "Visualization using Spyre"

    inputs = [{"type": 'dropdown',
               "label": "Choose Year",
               "options": [{'label': str(i), 'value': i} for i in range(1982, 2020)],
               'key': 'year',
               'value': '1982'},
              {"type": 'dropdown',
               "label": "Choose Province",
               "options": [{"label": "Vinnytska", "value": 1},
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
               'value': 1},
              {"type": 'text',
               "label": 'min Week',
               "key": 'min_week',
               "value": 1},
              {"type": 'text',
               "label": 'max Week',
               "key": 'max_week',
               "value": 52}]

    outputs = [{'type': 'table',
                'id': 'table1',
                'control_id': 'apply',
                'tab': 'Table'},
               {'type': 'plot',
                'id': 'plot1',
                'control_id': 'apply',
                'tab': 'Plot'}]

    controls = [{"type": 'button',
                 'id': 'apply',
                 'label': 'Apply'}]

    tabs = ['Table', 'Plot']

    def getData(self, params):
        path = 'lab2/data/province-{}.csv'
        Year = params['year']
        pr = params['province']
        min_week = params['min_week']
        max_week = params['max_week']
        df = pd.read_csv(path.format(pr), sep='[, ]+', engine='python')
        f = df[df.Year == Year].filter(['Year', 'Week', 'VHI', 'TCI', 'VCI'])
        final = f[(f['Week'] >= float(min_week)) &
                  (f['Week'] <= float(max_week))]
        final['Week'] = final['Week'].astype(int)
        final['Week'] = final['Week'].astype(str)
        return final

    def getPlot(self, params):
        df = self.getData(params)
        return df.set_index(df['Week']).plot()


app = MyApp()
app.launch()
