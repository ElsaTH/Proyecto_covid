# @ElsaTH

import pandas as pd
import numpy
from folder_tb import open_dataset




def position_country(data):
    """
    limpiamos los datos para poder obtener de cada pais (España, Chile, Rusia, Colombia y Argentina) el total de muertes, casos y recuperaciones.
    """
    data2 = data.loc[:,["location","date", "total_deaths", "total_cases" ]].dropna()
    data2["recuperation"] = data2.total_cases - data2.total_deaths
    data2.set_index(["location"],inplace=True)
    data2 = data2.loc[["Argentina", "Spain", "Chile", "Russia", "Colombia"],:]
    data2.reset_index(inplace=True)
    data2.set_index("date", inplace=True)
    spain = data2[data2.location == 'Spain']
    argentina = data2[data2.location == 'Argentina']
    russia = data2[data2.location == 'Russia']
    colombia = data2[data2.location == 'Colombia']
    chile = data2[data2.location == 'Chile']

    return spain, argentina, russia, colombia, chile


def Spain_covid(data):

    data2 = data.loc[:,["location","date", "total_deaths", "total_cases" ]].dropna()
    data2["recuperation"] = data2.total_cases - data2.total_deaths
    data2.set_index(["location"],inplace=True)
    data2 = data2.loc[["Argentina", "Spain", "Chile", "Russia", "Colombia"],:]

    spain_covid = data2.loc["Spain",:]
    spain_covid.reset_index(inplace=True)
    spain_covid = spain_covid.set_index("date")

    return spain_covid

def Argentina_covid(data):
    """
    limpieza de datos para representar total de muertes, total de casos y recuperaciones en Argentina
    """
    data2 = data.loc[:,["location","date", "total_deaths", "total_cases" ]].dropna()
    data2["recuperation"] = data2.total_cases - data2.total_deaths
    data2.set_index(["location"],inplace=True)
    data2 = data2.loc[["Argentina", "Spain", "Chile", "Russia", "Colombia"],:]

    argentina_covid = data2.loc["Argentina",:]
    argentina_covid.reset_index(inplace=True)
    argentina_covid.set_index("date",inplace=True)

    return argentina_covid


def Colombia_covid(data):
    """
    limpieza de datos para representar total de muertes, total de casos y recuperaciones en Colombia
    """
    data2 = data.loc[:,["location","date", "total_deaths", "total_cases" ]].dropna()
    data2["recuperation"] = data2.total_cases - data2.total_deaths
    data2.set_index(["location"],inplace=True)
    data2 = data2.loc[["Argentina", "Spain", "Chile", "Russia", "Colombia"],:]

    colombia_covid = data2.loc["Colombia",:]
    colombia_covid.reset_index(inplace=True)
    colombia_covid.set_index("date",inplace=True)

    return colombia_covid


def Russia_covid(data):
    """
    limpieza de datos para representar total de muertes, total de casos y recuperaciones en Russia
    """
    data2 = data.loc[:,["location","date", "total_deaths", "total_cases" ]].dropna()
    data2["recuperation"] = data2.total_cases - data2.total_deaths
    data2.set_index(["location"],inplace=True)
    data2 = data2.loc[["Argentina", "Spain", "Chile", "Russia", "Colombia"],:]

    russia_covid = data2.loc["Colombia",:]
    russia_covid.reset_index(inplace=True)
    russia_covid.set_index("date",inplace=True)

    return russia_covid


def Chile_covid(data):
    """
    limpieza de datos para representar total de muertes, total de casos y recuperaciones en Chile
    """
    data2 = data.loc[:,["location","date", "total_deaths", "total_cases" ]].dropna()
    data2["recuperation"] = data2.total_cases - data2.total_deaths
    data2.set_index(["location"],inplace=True)
    data2 = data2.loc[["Argentina", "Spain", "Chile", "Russia", "Colombia"],:]

    chile_covid = data2.loc["Colombia",:]
    chile_covid.reset_index(inplace=True)
    chile_covid.set_index("date",inplace=True)

    return chile_covid


def argentina_new_cases(data):    
    """
    Limpieza de datos para poder obtener los nuevos casos de Argentina
    """                                                               
    data2 = data.loc[:,["location","date","new_cases"]]
    data2.set_index(["location"],inplace=True)
    data_argentina = data2.loc[["Argentina"],:]
    data_argentina.reset_index(inplace=True)
    data_argentina.set_index("date", inplace=True)

    return data_argentina


def chile_new_cases(data):                                                                  
    """
    Limpieza de datos para poder obtener los nuevos casos de Chile
    """ 
    data2 = data.loc[:,["location","date","new_cases"]]
    data2.set_index(["location"],inplace=True)
    data_chile = data2.loc[["Chile"],:]
    data_chile.reset_index(inplace=True)
    data_chile.set_index("date", inplace=True)
   
    return data_chile

def spain_new_cases(data):                                                                     
    """
    Limpieza de datos para poder obtener los nuevos casos de España
    """ 
    data2 = data.loc[:,["location","date","new_cases"]]
    data2.set_index(["location"],inplace=True)
    data_spain = data2.loc[["Spain"],:]
    data_spain.reset_index(inplace=True)
    data_spain.set_index("date", inplace=True)
  
    return data_spain


def russia_new_cases(data):                                                              
    """
    Limpieza de datos para poder obtener los nuevos casos de Rusia
    """ 
    data2 = data.loc[:,["location","date","new_cases"]]
    data2.set_index(["location"],inplace=True)
    data_russia = data2.loc[["Russia"],:]
    data_russia.reset_index(inplace=True)
    data_russia.set_index("date", inplace=True)
  
    return data_russia


def colombia_new_cases(data):                                                             
    """
    Limpieza de datos para poder obtener los nuevos casos de Colombia
    """ 
    data2 = data.loc[:,["location","date","new_cases"]]
    data2.set_index(["location"],inplace=True)
    data_colombia = data2.loc[["Colombia"],:]
    data_colombia.reset_index(inplace=True)
    data_colombia.set_index("date", inplace=True)
  
    return data_colombia
