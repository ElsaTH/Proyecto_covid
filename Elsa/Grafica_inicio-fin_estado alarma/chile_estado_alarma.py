import pandas as pd
import numpy
import matplotlib.pyplot as plt 
import requests
import json

def chile_new_cases (url):                                                                   # @ElsaTH
    data = pd.read_csv(url, date_parser="date")
    data2 = data.loc[:,["location","date","new_cases"]]
    data2.set_index(["location"],inplace=True)
    data2 = data2.loc[["Chile"],:]
    data2.reset_index(inplace=True)
    data2.set_index("date", inplace=True)
    # Grafica:
    data2.plot(figsize=(9,9), rot=90)
    plt.xlabel("date")
    plt.plot([23,23],[0,35000],'k-', lw=2, color="m")
    plt.plot([125,125],[0,35000],'k-', lw=2, color="g")
    plt.title("Chile")

    return ### falta el retorno