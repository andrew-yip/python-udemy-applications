import os #os is to see the path at which it goes to
os.listdir() #to see everything that is it that path

import pandas #pandas is for data analysis of multidimensional arrays

df1 = pandas.read_csv("supermarkets.csv") #loading it (comma seperated values)
df1 #reading it

#Reading json files
df2 = pandas.read_json("supermarkets.json")
df2

#Reading excel files
df3 = pandas.read_excel("supermarkets.xlsx", sheet_name = 0)
df3

#Reading text files as csv because csv default is seperated by commas
df4 = pandas.read_csv("supermarkets-commas.txt") #seperated by commas (csv) (character seperated values)
df4

#reading csv that is seperated by semi colons
df5 = pandas.read_csv("supermarkets-semi-colons.txt", sep = ';') #default is comma but you change it with sep
df5

#pandas.read_csv? # to help find functions to read a csv

#reading a csv file that has no header
df8 = pandas.read_csv("data.txt", header = None) #seting headers columns to none
df8

#changing the columns names
df8.columns = ["ID", "Address", "City", "Zip", "Country", "Name", "Employees"] #setting column headers
df8

#setting the index as the first one
df8.set_index("ID") #doesn't alter the existing data frame

df8 #see how just because we set it in the line above it didn't alter the df8 object

#setting the set index ("ID") to a new obj called df9
df9 = df8.set_index("ID") #how to change the index
df9

#Setting Name as the first one, inplace keeps everything in place and doesn't drop anything
df8.set_index("Name", inplace = True, drop = False) #inplace switches the whole thing and doesn't delete anything
df8

df10 = df8.set_index("Address")
df10

#how to access elements using the .loc method
df10.loc["735 Dolores St":"332 Hill St", "Zip":"Employees"] #accessing elements from this table

df10 = df8.set_index("Address")
df10

#the iloc method allows you to use numbers to access 
df10.iloc[1:3, 1:3] #accessing elements from this table

#how to delete columns/rows           1 is for columns and 0 is for rows
df8.drop("Address",1) #drop is to delete (when you put 0 as the argument it refers to rows and 1 is for columns)

#how to drop multiple rows at a time

df8.drop(df8.index[0:2], 0) #dropping index from 0-2, 0 (second argument) represents the row

df8

#dropping multiple at a time (columns)
df8.drop(df8.columns[0:2], 1) #dropping columns from 0-2, 1 (second argument) represents the columns

print('index(rows): ', df8.index)
print('columns:' , df8.columns)

#adding columns

df11 = df4.set_index("Address") #df11 obj 
#df11["Continent"] = ["North America", "North America", "North America", "North America", "North America", "North America"]
# or could've done

df11["Continent"]=  df11.shape[0]*["North America"]
df11

#modifying added columns

df11["Continent"] = df11["Country"] + "," + "North America"
df11

#Adding rows

#no easy way to do it besides switching it

df11_t = df11.T #rows become columns and columns become rows
df11_t
df11_t["My Address"] = ["7", "Honolulu", "HI 96814", "USA", "Andrew", "100", "USA, North America"] #adding a new column

#converts it back to a row but storing all this in a new variable
df12 = df11_t.T
df12

#columns are a lot easier to modify. so we switch the whole position of the whole thing then switch it back with the.T method

#to modify existing rows/columns in data frames we just change df11_t["My Address"] instead of 
# "My Address" we change it to the name that we want to modify

type(df12)

#Geocoding using geopy

from geopy.geocoders import ArcGIS
nom = ArcGIS()
n = nom.geocode("3995 23rd St, San Francisco, CA 94114") #pass address as a string

n.longitude #longitude
print(n.longitude)
print(type(n))

#restarting (going to add longitude and latitude)

import pandas
df = pandas.read_csv("supermarkets.csv")
df

#making so the whole address is is in one section under address
df["Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]

#now we need to send this to the geocode method to get the latitude and longitude
df

#makes a coordinate and fetches the coordinates
df["Coordinates"] = df["Address"].apply(nom.geocode)
df.Coordinates[0].longitude

df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x!= None else None)
df

df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x!= None else None)
df
