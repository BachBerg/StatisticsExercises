import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import math
from scipy.stats import norm
from scipy.stats import f, t
from stat_lib.StatisticsFunctions import Statistics


# -----------------------------
# Problem 4 question 10-12 from exam set s2024
# -----------------------------


# A large-scale egg-based flu vaccine producer would like to 
# test the suppliers from which they get the eggs as well as 
# the incubator machines they use for the incubation of the ggs. 
# For that they consider an experimental study  involving 3 egg 
# suppliers and 4 incubators. They replicate the experiments 
# 3 times yielding (3x4)x3=36 experiments in total. as the 
# response they consider the yield from each incubation. they 
# are considering the following model:

# y_ijk = mu + tau_i + beta_j + (tau*beta)_ij + epsilon_ijk

# where mu is the overall mean, tau_i is the effect of the i'th 
# supplier with sum of tau__i = 0. B_j is the effect of the j'th 
# incubator with the sum of b_j = 0. (tau*beta)_ij is the 
# interaction effect with the sum over i and j equal to 0. 
# epsilon_ijk is the experimental error with NID(0, sigma^2). 
# The sum of squares calculation yield:

SS_supplier = 14
SS_incubator = 16
SS_interaction= 18
SST = 82

u_hat = 78.2

# Question 10 - what is the the degrees of freedom for the model?
# we have a two factor experiment with replication.
a = 3 # number of suppliers
b = 4 # number of incubators
n = 3 # number of replications pr. cell

# Total number of observations
N = a * b * n

# Degrees of freedom for a two way ANOVA with interaction
df_supplier = a -1
df_incubator = b -1
df_interaction = (a -1) * (b -1)
df_error = a * b * (n - 1)
df_total = N -1

# degrees of freedom for the model
df_model = df_supplier + df_incubator + df_interaction
print(f"10 - Degrees of freedom for the model: {df_model}")
# answer: 11, option 3

# Question 11 - what is the p-value assosiated with testing
# the supplier effect?

# first we find the erro sum of squares
SSE = SST - SS_supplier - SS_incubator - SS_interaction

# Then we can calulate the mean squares
MS_supplier = SS_supplier / df_supplier
MSE = SSE / df_error

# F statistic for supplier effect
F_supplier = MS_supplier / MSE
# p-value
P_supplier = 1 - f.cdf(F_supplier, df_supplier, df_error)
print(f"11 - P-value for supplier effect: {P_supplier}")
# answer: ~0.016, option 2 0.025 > p > 0.01

# for question 12, the following information is available:
    # (i) The sum of the responses for supplier 3 is 792
    # (ii) The sum of the responses for incubator 1 is 756
    # (iii) The estimate of the interaction effect for supplier 3 
    # and incubator 1 is (tau*beta)_31 = 10.3

# question 12 what is the effect estimate for incubator 1, ie beta_1?
y_hat_1 = 756 / (a * n)
beta_1 = y_hat_1 - u_hat
print(f"12 - Effect estimate for incubator 1: {Statistics.truncate(beta_1,2)}")
# answer: 5.79, option 1
