import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

covid_data = pd.read_csv("full_data.csv")
#import the full_data.csv file and it is read as a dataframe
print("the date and the new_cases for rows 10 to 20 are:")
print(covid_data.iloc[9:20,[0,2]])
#show the first column "date" and the third column "new_cases" from rows 10 to 20


all_location = covid_data.loc[:,"location"]
#get all the data in the "location" column and define these data as "all_location"
Afghanistan_rows = (all_location=="Afghanistan")
#When the data in all_location is "Afghanistan", the Boolean is True. Otherwise the Boolean is False.
#Get all Boolean values for the location column
print("The total cases in Afghanistan are:")
print(covid_data.loc[Afghanistan_rows,"total_cases"])
#Find the rows where Afghanistan is located. Print the values in these rows and in the "total_class" column.

china_rows = (covid_data["location"]=="China")
#find all the rows which belong to China
china_new_data = covid_data.loc[china_rows,["date","new_cases","new_deaths"]]
#creat a new object called "china_new_data" to save the date,new cases and new deaths
print("The mean of new_cases in China is:")
new_cases_mean = np.mean(china_new_data["new_cases"])
print(new_cases_mean)
#use np.mean to calculate the mean of the new cases in China
print("The mean of new_deaths in China is:")
new_deaths_mean = np.mean(china_new_data["new_deaths"])
print(new_deaths_mean)
proportion = new_deaths_mean/new_cases_mean
#use np.mean to calculate the mean of the new deaths in China
print("The mean of the new cases and the mean of the new deaths are different.The proportion of new cases that kill the infected person is",proportion)

plt.boxplot([china_new_data["new_cases"],china_new_data["new_deaths"]],labels=["new_cases","new_deaths"])
plt.title('the new cases and new deaths in China')
plt.show()
#plot the new_cases and new_deaths in China as a box plot

china_dates = covid_data.loc[china_rows,"date"]
china_new_cases = covid_data.loc[china_rows,"new_cases"]
china_new_deaths = covid_data.loc[china_rows,"new_deaths"]
#find the date,new cases and new deaths in China
plt.plot(china_dates,china_new_cases,'bo')
plt.plot(china_dates,china_new_deaths,'ro')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.title("compare the new cases and new deaths in China over time")
#set the title of the plot
plt.xlabel("date")
plt.ylabel("number")
#set the label of the x axis and the y axis
plt.show()

#Answer the question.Find the countries that havenot yet been more than 10 total infections
latest_date = (covid_data["date"]=="2020-03-31")
#find all the rows that belong to the 2020-03-31
latest_data = covid_data.loc[latest_date,["location","total_cases"]]
print("These conturies below have not yet been more than 10 total infections:")
print(latest_data.loc[latest_data["total_cases"]<=10,"location"])
#find the countries whose the total cases are less than 10
