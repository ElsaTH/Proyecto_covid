# @ElsaTH

import pandas as pd



# Función para abrir el dataset. Convertimos el csv en dataframe y establecemos que "date" es tipo fecha:
url="https://covid.ourworldindata.org/data/owid-covid-data.csv"

def open_dataset():
   """ 
    Dataframe obtenido y actualizado de la url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
   """
   data = pd.read_csv(url, date_parser="date")
   return data