import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import math
from scipy.stats import norm
from scipy.stats import f, t
from stat_lib.StatisticsFunctions import Statistics

#-----------------------------
# PROBLEM 3 question 6-9 FROM EXAM s2020
#-----------------------------

# Three different types of drugs are to be tested against 
# placebo to determine their effect on weight loss. Hence, four 
# types of drugs(D); three new drugs and the placebo, are used 
# for experimentation. However, it is also desired to test the 
# effects of two different types of diets(F); fatty  and 
# non-fatty, and feeding frequency (M); once, three times and 
# five times a day, on the weight loss. Hence a factorial 
# experiment with 4x2x3 number of runs is used where D, F and M 
# are tested at four, two and three levels respectively. 
# Furthermore, each experiment is replicated twice hence making 
# the total number of runs equal to 48.

# the incomplete ANOVA table for the model is given below:
SS_Model = 210
SS_D = 45
SS_F = 56
SS_M = 62
SS_FM = 22
SS_LOF = 28
SS_Total = 320

D = 4
F = 2
M = 3
reps = 2


## QUESTION 6 - What is the degrees of freedom for the pure error?
# degrees of freedom is:
df_pure_error =  D * F * M * (reps - 1)
print(f"6 - Degrees of freedom for the pure error: {df_pure_error}")
# answer: 24, option 4


## Question 7 - What is the F-ration for testing the model 
# given above?

# df model is the sum of treatments used in regression
df_model = D + F + M + reps
df_saturated = 4 * 2 * 3 - 1
df_LOF = df_saturated - df_model

# we calculate the SS_Error and df_Error
SS_Error = SS_Total - SS_Model
df_Error = df_LOF + df_pure_error

# We calculate the mean squares
MS_Model = SS_Model / df_model
MS_Error = SS_Error / df_Error

# calculate the F-ratio
F0 = MS_Model / MS_Error
print(f"7 - F-ratio for testing the model: {Statistics.truncate(F0,2)}")
# answer: 6.24, option 2

# Question 8 - what is the degrees of freedom for the lack of fit?
# the df_LOF is 12 the df_FM is 3
df_LOF = df_LOF + 3
print(f"8 - Degrees of freedom for the lack of fit: {df_LOF}")
# answer: 15, option 3

# Question 9 - What is the F-ration of the main effect of D?

# we use
# SS_Model = SS_D + SS_F + SS_M + SS_DF + SS_FM or something:(
# if we add up all the known sum of squares we can find SS_DM
# 45 + 56 + 62 + 22 + = 185
SS_DF = 210 - 185 # = 25
MS_D = SS_D / (D - 1) # = 15
MS_E = (SS_Error + SS_DF) / (df_LOF + df_pure_error) # = 3.46153846154
F = MS_D / MS_E
print(f"9 - F-ratio for main effect of D: {Statistics.truncate(F,2)}")
# answer: 4.33, option 1