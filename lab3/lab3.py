import os
#import request

import numpy
import pandas as pd

"""
Обрати всі домогосподарства, у яких загальна активна споживана
потужність перевищує 5 кВт.
2. Обрати всі домогосподарства, у яких вольтаж перевищую 235 В.
3. Обрати всі домогосподарства, у яких сила струму лежить в межах
19-20 А, для них виявити ті, у яких пральна машина та холодильних
споживають більше, ніж бойлер та кондиціонер.
4. Обрати випадковим чином 500000 домогосподарств (без повторів
елементів вибірки), для них обчислити середні величини усіх 3-х
груп споживання електричної енергії, а також
5. Обрати ті домогосподарства, які після 18-00 споживають понад 6
кВт за хвилину в середньому, серед відібраних визначити ті, у яких
основне споживання електроенергії у вказаний проміжок часу
припадає на пральну машину, сушарку, холодильник та освітлення
(група 2 є найбільшою), а потім обрати кожен третій результат із
першої половини та кожен четвертий результат із другої половини.
"""
#df = pd.read_fwf('data\household_power_consumption.txt')
data = pd.read_csv('data\household_power_consumption.txt', sep=";", header=0)
#data.columns = ["a", "b", "c", "etc."]
print(data.head())


% %time
dtype = [('Active', "f4"),('Reactive',"f4"),('Voltage',"f4"),('Intensity',"f4"),('Sub_1',"i4"),('Sub_2',"i4"),('Sub_3',"i4")]
_data = np.genfromtxt("data/household_power_consumption.txt", delimiter=';',
                      usecols=range(2, 9), dtype=dtype, skip_header=True, missing_values=['?'])
_d = np.loadtxt("data/household_power_consumption.txt",
                delimiter=';', usecols=range(0, 1), dtype="U", skiprows=1)
_t = np.loadtxt("data/household_power_consumption.txt",
                delimiter=';', usecols=range(1, 2), dtype="U", skiprows=1)
data = rfn.append_fields(_data, 'Date', _d, usemask=False)
data = rfn.append_fields(data, 'Time', _t, usemask=False)


del _d, _t
data
