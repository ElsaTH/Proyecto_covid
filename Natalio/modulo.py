import pandas as pd 
import json
import requests
import numpy as np  


covid = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
def natalios(covid):
   covid1 = pd.read_csv(covid)
   Df1 = covid1[covid1['location'].isin(['Argentina','Chile','Colombia','Russia','Spain'])]
   Df1.dropna(subset=['new_cases'],axis=0, inplace=True)
   Df1 = Df1.drop(['iso_code', 'continent', 'total_cases',
      'total_deaths', 'new_deaths', 'total_cases_per_million',
      'new_cases_per_million', 'total_deaths_per_million',
      'new_deaths_per_million', 'new_tests', 'total_tests',
      'total_tests_per_thousand', 'new_tests_per_thousand',
      'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units',
      'stringency_index', 'population', 'population_density', 'median_age',
      'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
      'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
      'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
      'life_expectancy'], axis=1)
   Df1.rename(columns={'new_cases': 'c_average'},inplace=True)
   Df1 = Df1.groupby('date').mean()


   return Df1  



def natalioargentina(covid):
   df666 = covid1[covid1['location']=='Argentina']
   df6 = df666.dropna(subset=['new_cases'],axis=0, inplace=True)   
   df666 = df666.drop(['iso_code', 'continent', 'total_cases',
       'total_deaths', 'new_deaths', 'total_cases_per_million',
       'new_cases_per_million', 'total_deaths_per_million',
       'new_deaths_per_million', 'new_tests', 'total_tests',
       'total_tests_per_thousand', 'new_tests_per_thousand',
       'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units',
       'stringency_index', 'population', 'population_density', 'median_age',
       'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
       'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
       'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
       'life_expectancy'], axis=1)
   df666.groupby('date').mean()
   argentina = df666.rename(columns={'new_cases': 'E_average'},inplace=True)


   return df666



def nataliorussia(covid):
   dfx = covid1[covid1['location']=='Russia']
   dfx.dropna(subset=['new_cases'],axis=0, inplace=True)
   dfx= dfx.drop(['iso_code', 'continent', 'total_cases',
       'total_deaths', 'new_deaths', 'total_cases_per_million',
       'new_cases_per_million', 'total_deaths_per_million',
       'new_deaths_per_million', 'new_tests', 'total_tests',
       'total_tests_per_thousand', 'new_tests_per_thousand',
       'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units',
       'stringency_index', 'population', 'population_density', 'median_age',
       'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
       'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
       'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
       'life_expectancy'], axis=1) 
   dfx.groupby('date').mean()
   dfx.rename(columns={'new_cases': 'Z_average'},inplace=True)

   return dfx


def nataliocolombia(covid):
   dfc = covid1[covid1['location']=='Colombia']
   dfc.dropna(subset=['new_cases'],axis=0, inplace=True)
   dfc= dfc.drop(['iso_code', 'continent', 'total_cases',
       'total_deaths', 'new_deaths', 'total_cases_per_million',
       'new_cases_per_million', 'total_deaths_per_million',
       'new_deaths_per_million', 'new_tests', 'total_tests',
       'total_tests_per_thousand', 'new_tests_per_thousand',
       'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units',
       'stringency_index', 'population', 'population_density', 'median_age',
       'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
       'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
       'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
       'life_expectancy'], axis=1)
   dfc.groupby('date').mean()
   dfc.rename(columns={'new_cases': 'Col_average'},inplace=True)


   return dfc



def nataliospain(covid):
   dfs = covid1[covid1['location']=='Spain']
   dfs.dropna(subset=['new_cases'],axis=0, inplace=True)
   dfs= dfs.drop(['iso_code', 'continent', 'total_cases',
       'total_deaths', 'new_deaths', 'total_cases_per_million',
       'new_cases_per_million', 'total_deaths_per_million',
       'new_deaths_per_million', 'new_tests', 'total_tests',
       'total_tests_per_thousand', 'new_tests_per_thousand',
       'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units',
       'stringency_index', 'population', 'population_density', 'median_age',
       'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
       'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
       'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
       'life_expectancy'], axis=1)
   dfs.groupby('date').mean()
   dfs.rename(columns={'new_cases': 'Spa_average'},inplace=True)


   return dfs


def nataliochile(covid):
   dfcl = covid1[covid1['location']=='Chile']
   dfcl.dropna(subset=['new_cases'],axis=0, inplace=True)
   dfcl= dfcl.drop(['iso_code', 'continent', 'total_cases',
       'total_deaths', 'new_deaths', 'total_cases_per_million',
       'new_cases_per_million', 'total_deaths_per_million',
       'new_deaths_per_million', 'new_tests', 'total_tests',
       'total_tests_per_thousand', 'new_tests_per_thousand',
       'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units',
       'stringency_index', 'population', 'population_density', 'median_age',
       'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
       'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
       'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
       'life_expectancy'], axis=1)
   dfcl.groupby('date').mean()
   dfcl.rename(columns={'new_cases': 'Chi_average'},inplace=True)



