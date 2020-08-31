import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import json


url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

def rosario (url):
    data = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', date_parser='date')
    covid = data.loc[:,['location','date','new_cases']]
    covid.set_index('location', inplace=True)
    covid.dropna()
    covid.loc[['Argentina','Colombia','Chile','Russia','Spain'],:]
    c_averages = covid.groupby(['date']).mean()

    return c_averages