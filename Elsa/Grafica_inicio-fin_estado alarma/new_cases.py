import pandas as pd
import numpy
import matplotlib.pyplot as plt 
import requests
import json

def argentina_new_cases (url):    
    """
    Creamos una gráfica para los new cases de Argentina
    """                                                               # @ElsaTH
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
    plt.savefig('new_cases_argentina.png')

    return ### falta el retorno


def chile_new_cases (url):         
    """
    Creamos una gráfica para los new cases de Chile
    """                                                          # @ElsaTH
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
    plt.savefig('new_cases_chile.png')

    return ### falta el retorno
    
def spain_new_cases (url):  
    """
    Creamos una gráfica para los new cases de España
    """                                                               # @ElsaTH
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
    plt.savefig('new_cases_spain.png')

    return ### falta el retorno