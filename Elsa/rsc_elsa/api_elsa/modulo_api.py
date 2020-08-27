import pandas as pd
import numpy
import requests
import json
                                                                    # @Elsa TH

def elsa (url):
    
    data = pd.read_csv(url, date_parser="date")
    data2 = data.loc[:,["location","date","new_cases"]]
    location = data2.set_index("location").dropna()
    pais = location.loc[["Spain","Argentina","Chile","Colombia","Russia"],:]
    c_averages = pais.groupby("date").mean().round(2)
    c_averages.rename(columns={"new_cases":"c_averages"}, inplace=True)
   #c_averages.to_json()
    #c_averages =c_averages.to_json("c_averages.json")

    return c_averages