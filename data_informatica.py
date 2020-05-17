import numpy as np
import matplotlib.pyplot as plt
import pandas as  pd
from collections import Counter

#Primero cargo el archivo .csv

df = pd.read_csv('encuesta_informatica.csv')

a = df.Internet.value_counts()
b = pd.Series(Counter(df.Lenguajes.str.split(',').sum()))
b = b.sort_values(ascending=False)/sum(b)*100
c = df.Nivel.value_counts()
d = pd.Series(Counter(df.Trabajos.str.split(',').sum()))
d = d.sort_values(ascending=False)/sum(d)*100

# Plot
fig = plt.figure()
ax = fig.add_subplot(111)
a.plot.pie(autopct='%1.0f%%', fontsize=14)
ax.set_title('Acceso a internet', fontsize=18)
ax.tick_params(labelsize=18)
fig.tight_layout()
plt.savefig('figures_statistic/acceso_internet.png', dpi=100)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
b.plot(kind='bar')
ax.set_title('¿En qué lenguaje programaron?', fontsize=18)
ax.set_ylabel('Porcentaje', fontsize=16)
ax.tick_params(labelsize=14)
ax.grid(linestyle='--')
fig.tight_layout()
plt.savefig('figures_statistic/lenguajes.png', dpi=100)

fig = plt.figure()
ax = fig.add_subplot(111)
c.plot.pie(autopct='%1.0f%%', fontsize=14)
ax.set_title('Nivel de programación', fontsize=18)
ax.tick_params(labelsize=18)
fig.tight_layout()
plt.savefig('figures_statistic/nivel.png', dpi=100)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
d.plot(kind='bar')
ax.set_title('Trabajos realizados', fontsize=18)
ax.set_ylabel('Porcentaje', fontsize=16)
ax.tick_params(labelsize=14)
ax.grid(linestyle='--')
fig.tight_layout()
plt.savefig('figures_statistic/trabajos.png', dpi=100)
