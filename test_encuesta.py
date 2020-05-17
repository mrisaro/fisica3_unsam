import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

df_encuesta = pd.read_csv('encuesta_informatica.csv')

list = df_encuesta['Lenguajes'].to_list()

list_expand = [i.split(',') for i in list]

list_lenguajes = [item for sublist in list_expand for item in sublist]

letter_counts = Counter(list_lenguajes)
df = pd.DataFrame.from_dict(letter_counts, orient='index')
df.plot(kind='bar')
