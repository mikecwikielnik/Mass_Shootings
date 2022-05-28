"""
Looking into the gun violence archive to gain insights
into states with at least one person killed in a shooting
"""

import pandas as pd
from matplotlib import colors, pyplot as plt

# Read the data

df = pd.read_csv(r'C:/Users/mikec/Google Drive/Py_files/Python/Mass Shootings/shootingdata1.csv')

# Make sure we have the correct table

print(df)
type(df)

# Make a states list

states = []
for i in df.iloc[:,0]:
    states.append(i)
    
# Make a killed list

killed = []
for i in df.iloc[:,1]:
    killed.append(i)
    
# Setting x,y values

xvalues = states
yvalues = killed


# Building a visual

plt.style.use('dark_background')
fig, ax = plt.subplots()
list = ["Texas", "Illinois", "California"]
colors = ["red" if i in list 
          else "purple" for i in states]
ax.bar(xvalues, yvalues, color = 'blue')
ax.set_xlabel("States with at least one shooting death", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Count of shootings with at least one death", fontsize=16)
ax.set_title("Count of shootings with at least one death per state\nSept 2018 - May 2022\ngunviolence.org/reports/mass-shooting\n", fontsize = 10)
plt.tick_params(axis='x', which='major', labelsize=7)
plt.show()
plt.clf()