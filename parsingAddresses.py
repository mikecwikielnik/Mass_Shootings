"""
A exercise in parsing addresses and driving original insights into mass shootings. 
"""


from cProfile import label
from shutil import which
from turtle import color, width
import usaddress
import pandas as pd
from matplotlib import colors, pyplot as plt    

# usaddress.tag('Cwikielnik House, 9 Southview ST, Dorchester, Ma 02125')\
    
dotaddress = usaddress.parse('Cwikielnik House, 9 Southview ST, Dorchester, Ma 02125')

print(dotaddress[6])

# pandas read csv

df = pd.read_csv(r'C:/Users/mikec/Google Drive/SQL/shootingdata.csv')

# test to get states only

print(df)
print(df['State'])

states = []
for i in df['State']:
    states.append(i)

# Counting each occurance per state

frequencies = []
for i in states:
    frequency = states.count(i)
    frequencies.append(frequency)

# Printing a slice of info, similar to head in R

print(states[0:3])

xvalues = states
print(xvalues[1])   # test

# Building a visual

plt.style.use('bmh')
fig, ax = plt.subplots()
list = ["Texas", "Illinois", "Massachusetts"]
colors = ["red" if i in list 
          else "blue" for i in states]
ax.bar(xvalues, frequencies, color = colors)
ax.set_xlabel('States', fontsize=8, edgecolors='black', label='Number of shootings')
fig.autofmt_xdate()
ax.set_ylabel("Count")
ax.set_title("\nCount of Mass Shootings per State\nSept 2018- May 2022\ngunviolence.org/reports/mass-shooting\n", fontsize = 10)
plt.tick_params(axis='both', which='major', length=6, width=3, colors='black', labelsize=8)
plt.show()
plt.clf()