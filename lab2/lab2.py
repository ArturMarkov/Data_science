

import os

import seaborn as sns
sns.set(style="whitegrid")

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
         "options": [{'label': str(i), 'value': i} for i in range(1991, 2020)],
            'key': 'year',
            'value': '1991'
         },
        {
            "type": 'slider',
            "label": 'Choose min_week',
            "key": "min_week",
            "value": 10
    },
        {
            "type": 'slider',
            "label": 'Choose max_week',
            "key": "max_week",
            "value": 52
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
         },
        {'type': 'plot',
            'id': 'another',
            'control_id': "button2",
            'tab': 'Another'


         }
         ]

    controls = [{"type": "button",
                 "label": "show data",
                 "id": "button1"},

                {"type": "button",
                 "label": "some button",
                 "id": "button2"

                 }]

    tabs = ['Table', 'Plot','Another']

    def getData(self, params):

        year = params['year']
        pr = params['province']
        # D:\python_data_science\lab2\data\province-1.csv
        path = os.path.normpath(f"lab2/data/province-{pr}.csv")
        min_week = params['min_week']
        max_week = params['max_week']
        df = pd.read_csv(path, header=0)


        df["Year"] = df["Year"].astype(str)
        # df["Week"] = df["week"].astype(int)
        p = df[df["Year"] == year]

        result = p[(p.Week >= min_week) & (p.Week <= max_week)]
        #print(result)

        print(type(year))
        result.Year = result.Year.astype(int)
        return result

    def data(self,params, year):
        
        pr = params['province']
        # lab2\data\province-1.csv
        # D:\python_data_science\lab2\data\province-1.csv
        path = os.path.normpath(f"lab2/data/province-{pr}.csv")
        min_week = params['min_week']
        max_week = params['max_week']
        df = pd.read_csv(path, header=0)


        df["Year"] = df["Year"].astype(str)
        # df["Week"] = df["week"].astype(int)
        p = df[df["Year"] == year]

        result = p[(p.Week >= min_week) & (p.Week <= max_week)]
        #print(result)

        print(type(year))
        result.Year = result.Year.astype(int)
        return result

    def plot1(self, params):
        df = self.getData(params)
        option = params['choose_by']
        #print(option)
        # df[option] = df[option].astype(str)
        #print(type(option))
        if str(option) == 'all':
            t = df.set_index("Week")
            #re = t[["VHI", "TCI", "VCI"]]
            re=t.loc[:, ("VHI", "TCI", "VCI")]
            return sns.lineplot(data=re).get_figure()
        else:
            
            return sns.lineplot(x='Week', y=params['choose_by'], data=df).get_figure()
        
        
    def another(self,params):
      
        df = self.data(params,"1995")
        t = df.set_index("Week")
        re = t.loc[:, ("VHI")]
        #rankings_pd.columns = ['TEST', 'ODI', 'T-20']
        #print(an)
        #.rename(columns = {'test':'TEST', 'odi':'ODI','t20': 'T20'}, inplace = True)
        
        df1 = self.data(params,'2015')
        t1 = df1.set_index("Week")
        re1 = t1.loc[:, ("VHI")]  # .rename(columns={"VHI": "2015"})
        result = pd.concat([re, re1], axis=1, sort=False)
        print(result)
        
        return sns.lineplot(data=result).get_figure()
    


app = SimpleApp()
app.launch()
