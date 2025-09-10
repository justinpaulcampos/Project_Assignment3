# Project Assignment 3

### Table of Content:
#### Problem 1: https://github.com/justinpaulcampos/Project_Assignment3/tree/main#normalization-problem
#### Problem 2:
## Normalization Problem
The goal of this Program is to normalize a random 5 by 5 array.
#### Problem 1
Import pandas
``` python
import numpy as np
```
Read cars.csv
``` python
cars = pd.read_csv('cars.csv')
```
Displays the following rows containing the indexes of 0 to 5 and 27 to 31.
``` python
display = cars.loc[(cars.index<5)|(cars.index>len(cars)-6)]
```
Display the text description of the table
``` python
print('these are the first and last 5 entries')
```
Display the table
``` python
display
```
Entire code:
``` python
import pandas as pd
cars = pd.read_csv('cars.csv')
display = cars.loc[(cars.index<5)|(cars.index>len(cars)-6)]
print('these are the first and last 5 entries')
display
```
## Problem 2
Import numpy
``` python
import pandas as pd
```
#### a)Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
Read cars.csv
``` python
cars = pd.read_csv('cars.csv')
```
displays the odd-numbered columns using a list of odd-numbered columns.
``` python
cars.loc[:,['Model','cyl','hp','wt','vs','gear']]
```
#### b)Display the row that contains the ‘Model’ of ‘Mazda RX4’.
This line locates and displays the column of Mazda
``` python
cars.loc[cars['Model']=="Mazda RX4"]
```
#### c) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
locates the certain cyl of a Camaro Z28
``` python
cars.loc[cars['Model']=="Camaro Z28", ['cyl']]
```
#### d)Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
Initialize a list of the given Models
``` python
lst = [ 'Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
```
initialize an empty DataFrame
``` python
display = pd.DataFrame()
```
This 'for' loop combines all the info of the Models to one dataframe
``` python
for x in lst:
    # locates the models and its properties
    temp = cars.loc[cars['Model'] == x, ['cyl','gear']]
    #Concatenates the temp array to the display array
    display = pd.concat([display, temp], axis=0)
```
Breaking down the for loop, I first located the specific models and its properties of cyl and gear
``` python
temp = cars.loc[cars['Model'] == x, ['cyl','gear']]
```
Then concatenates the temp array to the display array
``` python
display = pd.concat([display, temp], axis=0)
```
That 'for loop' loops around until all of the models and their properties are in one file

display the dataframe
``` python
display
```
