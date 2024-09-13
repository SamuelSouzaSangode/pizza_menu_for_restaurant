import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
1# Renomeando colunas, renomea posicionalmente

2# eval(coluna0 + coluna1 + coluna2)

3# Seleciona vária colunas, reamostra essas colunas por semana e soma, ou seja
agrupa por semana, semana0 = soma(movimentações dessa semana)
LEMBRANDO QUE OS DADOS ESTÃO EM MARCA DE TEMPO DE HORA


4# Seleciona várias colunas, reamostra essas colunas por dia e soma, ou seja
agrupa por dia, dia0 = soma(movimentações dessa semana)

5# Aplica uma janela móvel(rolling), a janela considera 30 períodos de tempo 
ao redor do ponto atual, o resultado do ponto atual é a soma dos 30 pontos ao redor.

6# Aplica uma janela móvel(rolling), a janela considera 50 períodos de tempo
ao redor do ponto atual, porém usando o win_type='gaussian', os valores que
estão mais próximo do centro da janela, tem mais peso do que os valores que estão
mais distantes. então é feito a soma, o desvio padrão para a soma gaussiana é de 10
'''

data = pd.read_csv('FremontBrigde.csv', index_col='Date', parse_dates=True)
#parse_dates transforma o índex em tipo data, para poder trabalhar já no formato correto

#1
data.columns = ['South', 'West', 'East']

data['Total'] = data.eval('South + West + East')#2
weekly = data[['South', 'West', 'East']].resample('W').sum()#3
daily = data[['South', 'West', 'East']].resample('D').sum()#4
daily_rolling = daily.rolling(30, center=True).sum()#5
daily_rolling_gausian = daily.rolling(50, center=True, win_type='gaussian').sum(std=10)#6
#print(data.dropna().describe())

fig, axs = plt.subplots(2, 2)
data['Total'].plot(ax=axs[0, 0])
weekly.plot(ax=axs[0, 1], style=[':', '--', '-'])
daily_rolling.plot(ax=axs[1, 0], style=[':', '--', '-'])
daily_rolling_gausian.plot(ax=axs[1, 1], style=[':', '--', '-'])



axs[0, 0].set_ylabel('Hourly Bicicle Count')
axs[0, 1].set_ylabel('Weekly sum')
axs[1, 0].set_ylabel('Daily Rolling sum 30')
axs[1, 1].set_ylabel('Daily Rolling Gausian sum 50')


plt.show()
