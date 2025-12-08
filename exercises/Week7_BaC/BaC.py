import numpy as np
import pandas as pd
from scipy.stats import f


## question S2022
# a 2^5 design with factors A, B, C, D and E is being considered. The 
# following estimates for the main effects and 2nd order interactions are 
# calculated:
# source | effect
#   A    |   12   
#   B    |   -8   
#   C    |   3.5  
#   D    |   4    
#   E    |   -6   
#   AB   |   0.5  
#   AC   |   -2   
#   AD   |   0.25 
#   AE    |   0.5
#   BC    |   1 
#   BD    |   -1 
#   BE    |   2 
#   CD    |   -0.5 
#   CD    |   -1 
#   DE    |   0.5 

# the total sum og squares is given as 2890
# for question 19 and 20  assume that 3rd 4th and 5th order interactions are neglieble.
# consider the model with only the main effects and 2nd order interactions

# problem VIII.1 (19)
# what is the degree of freedom for the lack of fit?
r = 2**5
df_total = r -1

# Main effects: 5 df (A, B, C, D, E)
# 2nd order interactions: 10 df (AB, AC, AD, AE, BC, BD, BE, CD, CE, DE)
df_model = 5 +10

df_LoF= df_total - df_model

print("Degree of freedom for the lack of fit:", df_LoF)


# problem VIII.2 (20)
# what is the p-value associated with testing the effect of D?
# Step 1: Calculate SS for effect D
n = 1
Contrast_D = 4 * 16 
# SS = Contrast_D**2 / (n * 2**k)
# SS = 64**2 / (2* 2**5) = 4096 / 32 = 128
SS = Contrast_D**2 / (n * 2**5)
print("SS for effect D:", SS)

# Step 2: Calculate SS for Error (Lack of Fit)
SS_model = 2274.5
# Step 3: Calculate SS_Error
SS_Error = 2890 - SS_model
print("SS_Error:", SS_Error)

# Step 4: Calculate MS_Error
MSE = SS_Error / df_LoF
print("MSE:", MSE)

# Step 5: Calculate F-statistic for D
dfD = 1
MSD =SS / dfD
F = MSD / MSE
print("F-statistic for effect D:", round(F,3))

# Step 6: Find p-value
P_value = 1 - f.cdf(F, dfD, df_LoF)
print("P-value for testing the effect of D:", round(P_value,3))




# Question VIII.3 (21)
# what is the resulting design in A, B and E?

## after reducing and keeping A, B and E
## the resulting design becomes:
# 2**3 = 8 runs

# it's still a full factorial since we didn't rerun the experiment
# replication pr. setting:
# A,B,E = 32/8 = 4 reps

print("Full factorial design with 4 replications")