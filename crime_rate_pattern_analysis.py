#--CRIME RATE PATTERN ANALYSIS---#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score


#data collection & preprocessing::
df = pd.read_csv('NCRB_Table_crime_rate.csv')
print(df)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df=df.dropna()

df["crime_2020"] = df["crime_2020"].astype(int)
df["crime_2021"] = df["crime_2021"].astype(int)
df["crime_2022"] = df["crime_2022"].astype(int)

df = df[~df["State/UT"].str.contains("Total", case=False, na=False)]
print(df.tail())
#creation of new column
#avegare crime

df['avg_crime'] = (df['crime_2020']+df['crime_2021']+df['crime_2022']) / 3
df["avg_crime"] = df["avg_crime"].astype(int)
print(df['avg_crime'])

#crime growth
df['crime_growth'] = (df['crime_2022'] - df['crime_2020']) 
print(df['crime_growth'])

#crime per population
df['crime_per_population'] = (df['crime_2022']/df['Mid-Year Projected Population (in Lakhs) (2022)']) 
print(df['crime_per_population'])



#EXPLORATORY DATA ANALYSIS:

#top 5 states by crime ( 2022)
top_states = df.sort_values(by='crime_2022', ascending=False).head(5)
print("Top 5 states by crime in 2022:",top_states)  

plt.bar(top_states['State/UT'],top_states['crime_2022'])
plt.title("Top 5 States by Crime in 2022")
plt.xlabel("Crime Count")
plt.ylabel("Frequency")
plt.show()

#crime trend total
total_crime = df[['crime_2020', 'crime_2021', 'crime_2022']].sum()
plt.figure()
plt.plot(total_crime.index, total_crime.values, marker='o')
plt.title("crime trend over yeears")
plt.show()


#crime rate vs population
plt.scatter(df["Mid-Year Projected Population (in Lakhs) (2022)"],df["crime_2022"])
plt.xlabel("population")
plt.ylabel("crime rate")
plt.title("population vs crime rate")
plt.show()

#chargesheet rate analysis
plt.figure()
plt.scatter(df["Chargesheeting Rate (2022)"], df["crime_2022"],c='Red')
plt.xlabel("Chargesheet Rate")
plt.ylabel("Crime Count")
plt.title("Chargesheet Rate vs Crime")
plt.show()



#model analysis

#part1:predict 2022 (model accuracy)
x = df[["crime_2020","crime_2021","Mid-Year Projected Population (in Lakhs) (2022)","Chargesheeting Rate (2022)"]]
y = df["crime_2022"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)
model = LinearRegression()
model.fit(x_train,y_train)

#predict on test data
y_pred = model.predict(x_test)

#evaluate model
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print("model evaluation (2022 prediction)")
print("mean squared error:",mse)
print("R squared:",r2)



#part 2:predict 2023 ( future trend)

new_data = [[
    df["crime_2021"].mean(),
    df["crime_2022"].mean(),
    df["Mid-Year Projected Population (in Lakhs) (2022)"].mean(),
    df["Chargesheeting Rate (2022)"].mean()
]]

pred_2023=model.predict(new_data)
print("Predicted crime count for 2023:",pred_2023[0])


df.to_csv("updated_crime_rate_pattern_analysis.csv", index=False)