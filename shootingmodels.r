# Trying to build a regression model 

library(dplyr)
library(rattle)
rattle()

data <- read.csv("shootingdata.csv")
summary(data)

# I could not build a regression model or anything of significance. I tried to make the state a factor.
# This led to nowhere. Within Rattle, I tried to build decision trees, random forests and even k-clustering models. 
# I did think the statistics below were interesting. If you look at Georgia being the max with 99 shootings, this is alarming information.
# Moreover, I think the descriptive statistics of "Killed" are profound. Why? 
3 Because you can expect 1.029 persons to die per shooting in America. 



# State    No..of.shootings.with.at.least.one.death
# Arizona   : 1   Min.   : 1.00                           
# California: 1   1st Qu.: 4.75                           
# Colorado  : 1   Median :12.00                           
# Delaware  : 1   Mean   :25.41                           
# Florida   : 1   3rd Qu.:38.25                           
# Georgia   : 1   Max.   :99.00                           
# (Other)   :26  

# X..Killed     
# Min.   : 0.000  
# 1st Qu.: 0.000  
# Median : 1.000  
# Mean   : 1.029  
# 3rd Qu.: 1.000  
# Max.   :22.000  
# 
# X..Injured    
# Min.   : 0.000  
# 1st Qu.: 3.000  
# Median : 4.000  
# Mean   : 4.061  
# 3rd Qu.: 5.000  
# Max.   :20.000 