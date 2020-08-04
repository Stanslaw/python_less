import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

data = pd.read_json('C:/Users/Stanslaw/Desktop/Jupiter/Clients_iif/result.json')

data.sort_values(by='datetime', inplace=True)
data.dropna(how='all', inplace=True)

data.drop(columns=['flat', 'house', 'tel', 'email', 'city', 'extra', 'street'], inplace=True)

# print(data)

data['ones'] = 1

data['summ'] = data['ones'].cumsum()

data.drop(columns=['name', 'ones'], inplace=True)

data['hours'] = data['datetime'].dt.hour

# print(data)


# Данные с абонентами. Подключения и отключения

data_2 = pd.read_json('C:/Users/Stanslaw/Desktop/Jupiter/Clients_iif/population_users.json', orient='index')

#Подключения
data_podkl = data_2.drop(columns='end_date')
data_podkl['ones'] = 1
data_podkl['podkl'] = data_podkl.ones.cumsum()
data_podkl.drop(columns='ones', inplace=True)
data_podkl['start_date'] = pd.to_datetime(data_podkl['start_date'])
data_podkl.rename(columns={'start_date': 'date'}, inplace=True)

#Отключения
data_otkl = data_2.drop(columns='start_date')
data_otkl = data_otkl[data_otkl.end_date != '1']
data_otkl.sort_values(by=['end_date'], inplace=True)
data_otkl['ones'] = 1
data_otkl['otkl'] = data_otkl.ones.cumsum()
data_otkl.drop(columns='ones', inplace=True)
data_otkl['end_date'] = pd.to_datetime(data_otkl['end_date'])
data_otkl.rename(columns={'end_date': 'date'}, inplace=True)

#Прирост абонентов подключения - отключения
data_podkl['inc_ab'] = 1
data_otkl['dwnc_ab'] = -1
data_incr = pd.concat([data_podkl[['date','inc_ab']], data_otkl[['date','dwnc_ab']]], axis=0, sort=False, ignore_index=True)
data_incr.sort_values(by=['date'], inplace=True)
data_incr.fillna(0, inplace=True)
data_incr['summ_abon'] = data_incr.inc_ab + data_incr.dwnc_ab
data_incr['final_summ_abon'] = data_incr.summ_abon.cumsum()

print(data_incr)

# print(data_podkl[['date','inc_ab']])
# print(data_otkl[['date','dwnc_ab']])

# print(data_podkl)
# print(data_otkl)

# data_podkl.plot(x='start_date', y='podkl')
# data_otkl.plot(x='end_date', y='otkl')


#
fig, ax = plt.subplots()
ax.plot(data_podkl.date, data_podkl.podkl, color='red', label='Подключения')
ax.plot(data_incr.date, data_incr.final_summ_abon, color='green', label='Прирост абонентов')
ax.plot(data_otkl.date, data_otkl.otkl, color='black', label='Отключения')


ax.set(xlabel='Дата', ylabel='Количество подключений / отключаний',
       title='Абоненты ИИФ', )
ax.grid()
ax.legend()

plt.show()