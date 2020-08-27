import pandas as pd
import numpy
import matplotlib.pyplot as plt 
import requests
import json

def chile_new_cases (url):                                                              # @ElsaTH
    data = pd.read_csv(url, date_parser="date")
    data2 = data.loc[:,["location","date","new_cases"]]
    data2.set_index(["location"],inplace=True)
    data2 = data2.loc[["Spain"],:]
    data2.reset_index(inplace=True)
    data2.set_index("date", inplace=True)
    # Grafica:
    data2.plot(figsize=(9,9), rot=90)
    plt.xlabel("date")
    plt.plot([174,174],[0,8000],'k-', lw=2, color="g")
    plt.plot([110,110],[0,8000],'k-', lw=2, color="m")
    plt.title("Spain")

    return ### falta el retorno