# @ElsaTH

import pandas as pd
import numpy
import matplotlib.pyplot as plt 
from folder_tb import open_dataset
import mining_data_tb




def total_deaths(spain, argentina, russia, colombia, chile):
    """
    Representación de la gráfica del total de las muertes por covid en los paises de España, Argentina,Russia, Colombia y chile
    """

    plt.figure(figsize=(10, 8))
    spain.total_deaths.plot(kind="line",label='Spain')
    argentina.total_deaths.plot(kind="line",label='Argentina')
    russia.total_deaths.plot(kind="line",label='Russia')
    colombia.total_deaths.plot(kind="line",label='Colombia')
    chile.total_deaths.plot(kind="line",label='Chile')
    plt.legend(loc='top_right')
    plt.title('Histogram Total Deaths', size=20, color="#138D75")
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.xticks(rotation=45)
    #plt.savefig('total_deats_covid.png')
    plt.show()
    
#total_deaths(mining_data_tb.position_country(open_dataset())[0], mining_data_tb.position_country(open_dataset())[1], mining_data_tb.position_country(open_dataset())[2], mining_data_tb.position_country(open_dataset())[3], mining_data_tb.position_country(open_dataset())[4])

def total_cases(spain, argentina, russia, colombia, chile):
    """
    Representación de la gráfica del total de casos por covid en los paises de España, Argentina,Russia, Colombia y chile
    """
    plt.figure(figsize=(10, 8))
    spain.total_cases.plot(kind="line",label='Spain')
    argentina.total_cases.plot(kind="line",label='Argentina')
    russia.total_cases.plot(kind="line",label='Russia')
    colombia.total_cases.plot(kind="line",label='Colombia')
    chile.total_cases.plot(kind="line",label='Chile')
    plt.legend(loc='top_right')
    plt.title('Histogram Total Cases', size=20, color="#138D75")
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.xticks(rotation=45)
    #plt.savefig('total_cases_covid.png')
    plt.show()
#total_cases(mining_data_tb.position_country(open_dataset())[0], mining_data_tb.position_country(open_dataset())[1], mining_data_tb.position_country(open_dataset())[2], mining_data_tb.position_country(open_dataset())[3], mining_data_tb.position_country(open_dataset())[4])


def recuperation(spain, argentina, russia, colombia, chile):
    """
    Representación de la gráfica del total de recuperados por covid en los paises de España, Argentina,Russia, Colombia y chile
    """
    plt.figure(figsize=(10, 8))
    spain.recuperation.plot(kind="line",label='Spain')
    argentina.recuperation.plot(kind="line",label='Argentina')
    russia.recuperation.plot(kind="line",label='Russia')
    colombia.recuperation.plot(kind="line",label='Colombia')
    chile.recuperation.plot(kind="line",label='Chile')
    plt.legend(loc='top_right')
    plt.title('Histogram Recuperation', size=20, color="#138D75")
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.xticks(rotation=45)
    #plt.savefig('recuperation_covid.png')
    plt.show()
#recuperation(mining_data_tb.position_country(open_dataset())[0], mining_data_tb.position_country(open_dataset())[1], mining_data_tb.position_country(open_dataset())[2], mining_data_tb.position_country(open_dataset())[3], mining_data_tb.position_country(open_dataset())[4])



def Spain_total(spain_covid):
    """
    Representación de la gráfica de las columnas total de muertes, total de casos y recuperaciones en España.
    """
    spain_covid.plot(figsize=(9,9), rot=-45)
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.title("Spain Covid 19 ", size=20, color="#138D75")
    #plt.savefig('Spain_covid.png')
    plt.show()

#Spain_total(mining_data_tb.Spain_covid(open_dataset()))

def Argentina_total(argentina_covid):
    """
    Representación de la gráfica de las columnas total de muertes, total de casos y recuperaciones en Argentina.
    """
    argentina_covid.plot(figsize=(9,9), rot=-45)
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.title("Argentina Covid 19 ", size=20, color="#138D75")
    #plt.savefig('Argentina_covid.png')
    plt.show()

#Argentina_total(mining_data_tb.Argentina_covid(open_dataset()))

def Colombia_total(colombia_covid):
    """
    Representación de la gráfica de las columnas total de muertes, total de casos y recuperaciones en Colombia.
    """
    colombia_covid.plot(figsize=(9,9), rot=-45)
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.title("Colombia Covid 19 ", size=20, color="#138D75")
    #plt.savefig('Colombia_covid.png')
    plt.show()

#Colombia_total(mining_data_tb.Colombia_covid(open_dataset()))

def Russia_total(russia_covid):
    """
    Representación de la gráfica de las columnas total de muertes, total de casos y recuperaciones en Russia.
    """
    russia_covid.plot(figsize=(9,9), rot=-45)
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.title("Russia Covid 19 ", size=20, color="#138D75")
    #plt.savefig('Russia_covid.png')
    plt.show()

#Russia_total(mining_data_tb.Russia_covid(open_dataset()))

def Chile_total(chile_covid):
    """
    Representación de la gráfica de las columnas total de muertes, total de casos y recuperaciones en Chile.
    """
    chile_covid.plot(figsize=(9,9), rot=-45)
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.title("Chile Covid 19 ", size=20, color="#138D75")
    #plt.savefig('Chile_covid.png')
    plt.show()

#Chile_total(mining_data_tb.Chile_covid(open_dataset()))



def argentina_new_cases (data_argentina):                                                               
    """
    Representación de la gráfica de los nuevos casos en Argentina
    """
    data_argentina.plot(figsize=(9,9), rot=-45, color="orange")
    plt.xlabel("Date", size=14, color="#0E6655")
    plt.plot([38,38],[0,12000],'k-', lw=2, color="m")
    plt.title("NEW CASES ARGENTINA", size=14, color="#0E6655")
    #plt.savefig('new_cases_argentina.png')
    plt.show()

#argentina_new_cases(mining_data_tb.argentina_new_cases(open_dataset()))   


def argentina_new_cases_outliers(data_argentina):
    """
    Representación de outliers de los nuevos casos en Argentina
    """
    plt.boxplot(data_argentina.new_cases,
                notch=True, patch_artist=None,
                capprops=dict(color="orange",markerfacecolor='g'),
                medianprops=dict(color="orange", alpha=0.3),
                whiskerprops=dict(color="green",alpha=0.9, markersize=17,linestyle = 'dotted'),
                flierprops=dict(color="green",alpha=0.9, markersize=5,markerfacecolor="orange", marker='o'),
                boxprops=dict(color="orange",alpha=0.9, markersize=5),
                showmeans=dict(color="green",alpha=0.9, markersize=5),
                showfliers=dict(color="green",alpha=0.9, markersize=5),
                showbox=dict(color="green",alpha=0.9, markersize=5),
                showcaps=dict(color="green",alpha=0.9, markersize=5)
            )        
    plt.title("OUTLIERS ARGENTINA",size=14, color="#0E6655")
    plt.xticks([1], ['Argentina'])
    plt.xlabel("Date", size=14, color="#0E6655")
    #plt.savefig('outliers_argentina.png')
    plt.show()

#argentina_new_cases_outliers(mining_data_tb.argentina_new_cases(open_dataset()))  


def chile_new_cases (data_chile):                                                                   
    """
    Representación de la gráfica de los nuevos casos en Chile
    """
    data_chile.plot(figsize=(9,9), rot=90)
    plt.xlabel("DATE")
    plt.plot([23,23],[0,35000],'k-', lw=2, color="m")
    plt.plot([125,125],[0,35000],'k-', lw=2, color="g")
    plt.title("Chile")
    #plt.savefig('chile_new_cases.png')
    plt.show()

#chile_new_cases(mining_data_tb.chile_new_cases(open_dataset()))  
    

def chile_new_cases_outliers(data_chile):
    """
    Representación de outliers de los nuevos casos en Chile
    """
    plt.boxplot(data_chile.new_cases,
            notch=True, patch_artist=None,
            capprops=dict(color="#C39BD3",markerfacecolor='g'),
            medianprops=dict(color="orange", alpha=0.3),
            whiskerprops=dict(color="green",alpha=0.9, markersize=17,linestyle = 'dotted'),
            flierprops=dict(color="green",alpha=0.9, markersize=5,markerfacecolor="#C39BD3", marker='o'),
            boxprops=dict(color="#C39BD3",alpha=0.9, markersize=5),
            showmeans=dict(color="green",alpha=0.9, markersize=5),
            showfliers=dict(color="green",alpha=0.9, markersize=5),
            showbox=dict(color="green",alpha=0.9, markersize=5),
            showcaps=dict(color="green",alpha=0.9, markersize=5)
          )       
    plt.title("OUTLIERS CHILE",size=14, color="#0E6655")
    plt.xticks([1], ['Chile'])
    plt.xlabel("Date", size=14, color="#0E6655")
    #plt.savefig('outliers_chile.png')
    plt.show()
#chile_new_cases_outliers(mining_data_tb.chile_new_cases(open_dataset()))  


def spain_new_cases (data_spain):                                                                    
    """
    Representación de la gráfica de los nuevos casos en España
    """
    data_spain.plot(figsize=(9,9), rot=90)
    plt.xlabel("DATE")
    plt.plot([174,174],[0,20000],'k-', lw=2, color="g")
    plt.plot([110,110],[0,20000],'k-', lw=2, color="m")
    plt.title("NEW CASES SPAIN")
    #plt.savefig('spain_new_cases.png')
    plt.show()
#spain_new_cases(mining_data_tb.spain_new_cases(open_dataset()))  
    
def spain_new_cases_outliers(data_spain):
    """
    Representación de outliers de los nuevos casos en España
    """
    plt.boxplot(data_spain.new_cases,
            notch=True, patch_artist=None,
            capprops=dict(color="#85C1E9",markerfacecolor='g'),
            medianprops=dict(color="orange", alpha=0.3),
            whiskerprops=dict(color="green",alpha=0.9, markersize=17,linestyle = 'dotted'),
            flierprops=dict(color="green",alpha=0.9, markersize=5,markerfacecolor="#85C1E9", marker='o'),
            boxprops=dict(color="#85C1E9",alpha=0.9, markersize=5),
            showmeans=dict(color="green",alpha=0.9, markersize=5),
            showfliers=dict(color="green",alpha=0.9, markersize=5),
            showbox=dict(color="green",alpha=0.9, markersize=5),
            showcaps=dict(color="green",alpha=0.9, markersize=5)
          )  
    plt.title("OUTLIERS SPAIN",size=14, color="#0E6655")
    plt.xticks([1], ['Spain'])
    plt.xlabel("Date", size=14, color="#0E6655")
    #plt.savefig('outliers_spain.png')
    plt.show()

#spain_new_cases_outliers(mining_data_tb.spain_new_cases(open_dataset()))


def colombia_new_cases (data_colombia): 
    """
    Representación de la gráfica de los nuevos casos en Colombia
    """
    data_colombia.plot(figsize=(9,9), rot=-45)
    plt.xlabel("DATE", size=14, color="g")
    plt.plot([75,75],[0,12000],'k-', lw=2, color="m")
    plt.plot([177,177],[0,12000],'k-', lw=2, color="g")
    plt.title("NEW CASES COLOMBIA", size=14)
    #plt.savefig('colombia_new_cases.png')
    plt.show()

#colombia_new_cases(mining_data_tb.colombia_new_cases(open_dataset()))  
    

def colombia_new_cases_outliers(data_colombia):
    """
    Representación de outliers de los nuevos casos en Colombia
    """
    plt.boxplot(data_colombia.new_cases,
            notch=True, patch_artist=None,
            capprops=dict(color="#DC7633",markerfacecolor='g'),
            medianprops=dict(color="orange", alpha=0.3),
            whiskerprops=dict(color="green",alpha=0.9, markersize=17,linestyle = 'dotted'),
            flierprops=dict(color="#DC7633",alpha=0.9, markersize=5,markerfacecolor="#DC7633", marker='o'),
            boxprops=dict(color="orange",alpha=0.9, markersize=5),
            showmeans=dict(color="green",alpha=0.9, markersize=5),
            showfliers=dict(color="green",alpha=0.9, markersize=5),
            showbox=dict(color="green",alpha=0.9, markersize=5),
            showcaps=dict(color="green",alpha=0.9, markersize=5)
          )          
    plt.title("OUTLIERS COLOMBIA",size=14, color="#0E6655")
    plt.xticks([1], ['Colombia'])
    plt.xlabel("Date", size=14, color="#0E6655")
    #plt.savefig('outliers_colombia.png')
    plt.show()

#colombia_new_cases_outliers(mining_data_tb.colombia_new_cases(open_dataset()))  




def russia_new_cases (data_russia): 
    """
    Representación de la gráfica de los nuevos casos en Rusia
    """
    data_russia.plot(figsize=(9,9), rot=-45)
    plt.xlabel("DATE", size=14, color="g")
    plt.plot([58,58],[0,12000],'k-', lw=2, color="m")
    plt.plot([103,103],[0,12000],'k-', lw=2, color="g")
    plt.title("NEW CASES RUSSIA", size=14)
    #plt.savefig('russia_new_cases.png')
    plt.show()

#russia_new_cases(mining_data_tb.russia_new_cases(open_dataset()))  


def russia_new_cases_outliers(data_russia):
    """
    Representación de outliers de los nuevos casos en Rusia
    """
    plt.boxplot(data_russia.new_cases,
            notch=True, patch_artist=None,
            capprops=dict(color="orange",markerfacecolor='g'),
            medianprops=dict(color="orange", alpha=0.3),
            whiskerprops=dict(color="green",alpha=0.9, markersize=17,linestyle = 'dotted'),
            flierprops=dict(color="#52BE80 ",alpha=0.9, markersize=5,markerfacecolor="#5D6D7E", marker='o'),
            boxprops=dict(color="orange",alpha=0.9, markersize=5),
            showmeans=dict(color="green",alpha=0.9, markersize=5),
            showfliers=dict(color="green",alpha=0.9, markersize=5),
            showbox=dict(color="green",alpha=0.9, markersize=5),
            showcaps=dict(color="green",alpha=0.9, markersize=5)
          )      
    plt.title("OUTLIERS RUSSIA",size=14, color="#0E6655")
    plt.xticks([1], ['Russia'])
    plt.xlabel("Date", size=14, color="#0E6655")
    #plt.savefig('outliers_russia.png')
    plt.show()

#russia_new_cases_outliers(mining_data_tb.russia_new_cases(open_dataset())) 



#### GRAFICAS OPCION B:

def Country_argentina(argentina):

    argentina = argentina.loc["2020-03-26":,:]
    argentina.total_deaths.plot(kind='bar',figsize=(20,10), rot=-45, color="#D5F5E3")

    plt.xlabel("Date", size=14, color="#0E6655")
    plt.ylabel("Person", size=14, color="#0E6655")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")
    plt.title("TOTAL DEATHS ARGENTINA" ,size=14, color="#0E6655")
    plt.plot ([0,90], [70,588],lw = 2,color='m',linestyle="--")
    plt.plot ([90,174], [588,7563],lw = 2,color='m',linestyle="--")

    #plt.savefig('evolucion_muertes_diarias_argentina.png')
    plt.show()

#Country_argentina(mining_data_tb.Country(open_dataset())[0])


def Country_colombia(colombia):
    colombia = colombia.loc["2020-03-31":,:]
    colombia.total_deaths.plot(kind='bar',figsize=(20,10), rot=-45, color="#DC7633")

    plt.xlabel("Date", size=14, color="#0E6655")
    plt.ylabel("Numero de muertes", size=14, color="#0E6655")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")
    plt.title("TOTAL DEATHS COLOMBIA",size=14, color="#0E6655")
    plt.plot ([0,50], [50,613],lw = 2,color='m',linestyle="--")
    plt.plot ([50,149], [613,17889],lw = 2,color='m',linestyle="--")

    #plt.savefig('evolucion_muertes_diarias_colombia.png')
    plt.show()

#country_colombia(mining_data_tb.Country(open_dataset())[3])


def Country_spain(spain):
    spain = spain.loc["2020-03-11":,:]
    spain.total_deaths.plot(kind='bar',figsize=(20,10), rot=-45, color="#85C1E9")

    plt.xlabel("Date", size=14, color="#0E6655")
    plt.ylabel("Numero de muertes", size=14, color="#0E6655")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")
    plt.title("TOTAL DEATHS SPAIN",size=14, color="#0E6655")
    plt.plot ([0 ,72], [72,28752],lw = 2,color='m',linestyle="--")
    plt.plot ([72 ,75], [28752,28752],lw = 2,color='y',linestyle="--")
    plt.plot ([75 ,76], [28752,27136],lw = 2,color='g',linestyle="--")
    plt.plot ([76 ,100], [27136,27136],lw = 2,color='y',linestyle="--")
    plt.plot ([100 ,101], [27136,28315],lw = 2,color='m',linestyle="--")
    plt.plot ([101 ,170], [28315, 28924],lw = 2,color='m',linestyle="--")

    #plt.savefig('evolucion_muertes_diarias_spain.png')
    plt.show()

#Country_spain(mining_data_tb.Country(open_dataset())[2])



def Country_russia(russia):
    russia = russia.loc["2020-04-02":,:]
    russia.total_deaths.plot(kind='bar',figsize=(20,10), rot=-45, color="#5D6D7E")

    plt.xlabel("Date", size=14, color="#0E6655")
    plt.ylabel("Numero de muertes", size=14, color="#0E6655")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")
    plt.title("TOTAL DEATHS RUSSIA",size=14, color="#0E6655")
    plt.plot ([0 ,147], [147,16568],lw = 2,color='m',linestyle="--")

    #plt.savefig('evolucion_muertes_diarias_rusia.png')
    plt.show()

#Country_russia(mining_data_tb.Country(open_dataset())[4])


def chi(chile):
    chile = chile.loc["2020-04-07":,:]
    chile.total_deaths.plot(kind='bar',figsize=(20,10), rot=-45, color="#C39BD3")

    plt.xlabel("Date", size=14, color="#0E6655")
    plt.ylabel("Numero de muertes", size=14, color="#0E6655")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")
    plt.title("TOTAL DEATHS CHILE",size=14, color="#0E6655")
    plt.plot ([0 ,142], [142,10958],lw = 2,color='m',linestyle="--")

    #plt.savefig('evolucion_muertes_diarias_chile.png')
    plt.show()

#Country_chile(mining_data_tb.Country(open_dataset())[2])


def Grafico_linea_total_deaths(countries_total_deaths):
    countries_total_deaths.plot(kind="line",figsize=(10, 8),color=["#D5F5E3","#C39BD3","#DC7633","#5D6D7E","#85C1E9"])

    plt.legend(loc='top_right')
    plt.title('TOTAL DEATHS', size=20, color="#138D75")
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.xticks(rotation=45)

    #plt.savefig('line_total_deaths_5_countries.png')
    plt.show()

#Grafico_linea_total_deaths(mining_data_tb.Countries_total(open_dataset()))

def Grafico_linea_new_cases(countries_new_cases):
    countries_new_cases.plot(kind="line",figsize=(10, 8),color=["#D5F5E3","#C39BD3","#DC7633","#5D6D7E","#85C1E9"])

    plt.legend(loc='top_right')
    plt.title('NEW CASES', size=20, color="#138D75")
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.xticks(rotation=45)

    #plt.savefig('line_new_cases_5_countries.png')
    plt.show()

#Grafico_linea_new_cases(mining_data_tb.Countries_new(open_dataset()))

def Grafico_bar_total_deaths(countries_total_deaths):

    total_deaths=countries_total_deaths.sum() 
    total_deaths.plot(kind="bar",figsize=(10, 8),color=["#D5F5E3","#C39BD3","#DC7633","#5D6D7E","#85C1E9"])

    plt.title('TOTAL DEATHS', size=20, color="#138D75")
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.xticks(rotation=0,FontSize=12)
    plt.yticks(rotation=0,FontSize=12)

    #plt.savefig('bar_total_deaths_5_countries.png')
    plt.show()

#Grafico_bar_total_deaths(mining_data_tb.Countries_total(open_dataset()))

def Grafico_bar_new_cases(countries_new_cases):
    new_cases = countries_new_cases.sum() 
    new_cases.plot(kind="bar",figsize=(10, 8),color=["#D5F5E3","#C39BD3","#DC7633","#5D6D7E","#85C1E9"])

    plt.title('NEW CASES', size=20, color="#138D75")
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.xticks(rotation=0,FontSize=12)
    plt.yticks(rotation=0,FontSize=12)

    #plt.savefig('bar_new_cases_5_countries.png')
    plt.show()

#Grafico_bar_new_cases(mining_data_tb.Countries_new(open_dataset()))

def Grafico_pie_total_deaths(countries_total_deaths):
    total_deaths=countries_total_deaths.sum() 
    total_deaths.plot(kind="pie",figsize=(10, 8),colors=["#D5F5E3","#C39BD3","#DC7633","#5D6D7E","#85C1E9"])

    plt.legend(loc='top_left')
    plt.title('TOTAL DEATHS', size=20, color="#138D75")
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.xticks(rotation=0,FontSize=12)
    plt.yticks(rotation=0,FontSize=12)

    #plt.savefig('pie_total_deaths_5_countries.png')
    plt.show()

#Grafico_pie_total_deaths(mining_data_tb.Countries_total(open_dataset())) 


def Grafico_pie_new_cases(countries_new_cases):
    new_cases = countries_new_cases.sum() 
    new_cases.plot(kind="pie",figsize=(10, 8),colors=["#D5F5E3","#C39BD3","#DC7633","#5D6D7E","#85C1E9"])

    plt.legend(loc='top_left')
    plt.title('NEW CASES', size=20, color="#138D75")
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")
    plt.xticks(rotation=0,FontSize=12)
    plt.yticks(rotation=0,FontSize=12)

    #plt.savefig('pie_new_cases_5_countries.png')
    plt.show()

#Grafico_pie_new_cases(mining_data_tb.Countries_new(open_dataset()))


def Grafico_scatter_total_deaths(countries_total_deaths):
    plt.scatter(countries_total_deaths.Argentina, countries_total_deaths.Spain, countries_total_deaths.Chile, countries_total_deaths.Russia)
    plt.title("TOTAL DEATHS", size=20, color="#138D75")
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")

    #plt.savefig('scatter_total_deaths_5_countries.png')
    plt.show()

#Grafico_scatter_total_deaths(mining_data_tb.Countries_total(open_dataset()))


def Grafico_scatter_new_cases(countries_new_cases):
    plt.scatter(countries_new_cases.Argentina, countries_new_cases.Spain, countries_new_cases.Chile, countries_new_cases.Russia)
    plt.title("NEW CASES", size=20, color="#138D75")
    plt.xlabel('Date', size=14, color="#138D75")
    plt.ylabel('Person',size=14, color="#138D75")

    #plt.savefig('scatter_new_cases_5_countries.png')
    plt.show()

#Grafico_scatter_new_cases(mining_data_tb.Countries_new(open_dataset()))