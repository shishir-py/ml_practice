# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country',"drives_right"]])


# -------------------Method 2-------------------------------


# Print out first 3 observations
print(cars.iloc[:3])

# Print out fourth, fifth and sixth observation
print(cars.iloc[3:6])

# -------------------Method 3-------------------------------


# Print out observation for Japan
print(cars)
print(cars.loc['JPN'])
# Print out observations for Australia and Egypt
print(cars.loc[['AUS',"EG"]])

# -------------------Method 3-------------------------------

# Print out drives_right value of Morocco

print(cars.loc['MOR']['drives_right'])
# Print sub-DataFrame
print(cars.iloc[4:6][['country','drives_right']])

# -------------------Method 4-------------------------------

# Print out drives_right column as Series

print(cars.loc[:,"drives_right"])
# Print out drives_right column as DataFrame
print(cars.iloc[:,2:3])

# Print out cars_per_cap and drives_right as DataFrame

print(cars.loc[:,["cars_per_cap",'drives_right']])