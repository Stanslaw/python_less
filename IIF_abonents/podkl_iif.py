import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import matplotlib.pyplot as plt

data = pd.read_json('C:/Users/Stanslaw/Desktop/Jupiter/Clients_iif/result.json')

data.sort_values(by='datetime', inplace=True)
data.dropna(how='all', inplace=True)

data.drop(columns=['flat', 'house', 'tel', 'email', 'city', 'extra', 'street'], inplace=True)

print(data)

data['ones'] = 1

data['summ'] = data['ones'].cumsum()

data.drop(columns=['name', 'ones'], inplace=True)

data['hours'] = data['datetime'].dt.hour

print(data)
print(data.columns)

fig = px.scatter(data, x='datetime', y='summ')
fig.show()

# plt.style.use('ggplot')
# data.plot(x='datetime', y='summ')
# plt.show()


data_2 = data.groupby('hours', as_index=False).count()

print(data_2)


# fig = px.line(data_2, x='hours', y='datetime', title='Times of activity')
# # fig.update_layout(xaxis=dict(range=[0,24]))
# fig.update_xaxes(range=[0, 24], row=1, col=1)
# fig.show()



plt.style.use('ggplot')
fig, ax = plt.subplots()

ax.plot(data_2.datetime)
ax.grid(True)

plt.xticks(list(range(24)))
plt.xlabel('Часы')
plt.ylabel('Количество подключений')


# plt.style.use('ggplot')
# data_2.plot(x='hours', y='datetime')
# plt.xticks(list(range(24)))
# plt.xlabel('Часы')
# plt.ylabel('Количество подключений')

plt.show()
