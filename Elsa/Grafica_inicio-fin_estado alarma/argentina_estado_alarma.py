import pandas as pd
import numpy
import matplotlib.pyplot as plt 
import requests
import json

def argentina_new_cases (url):                                                                   # @ElsaTH
    data = pd.read_csv(url, date_parser="date")
    data2 = data.loc[:,["location","date","new_cases"]]
    data2.set_index(["location"],inplace=True)
    data2 = data2.loc[["Argentina"],:]
    data2.reset_index(inplace=True)
    data2.set_index("date", inplace=True)
    # Grafica:
    data2.plot(figsize=(9,9), rot=90)
    plt.xlabel("date")
    plt.plot([38,38],[0,8000],'k-', lw=2, color="m")
    plt.title("Argentina")

    return ### falta el retorno
    