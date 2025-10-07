import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from scipy.stats import f, t
from stat_lib.StatisticsFunctions import Statistics

# -----------------------------
# PROBLEM 1 FROM EXAM S2020 1.1-1.4
# -----------------------------
# Chicken breeds Breed 1 & Breed 2 Company selling the chickens
# offer this experimental study to convince farmers to buy Breed 2
# 18 chickens are randomly selected with 8 chickens for breed 1 and 10 chickens for breed 2
n1 = 8
n2 = 10
# the egg production pr month were recorded
# the results were:
mean_estimante1 = 18.6
mean_estimante2 = 20.4
sigma1 = 2.1
sigma2 = 1.2

# -----------------------------
# Question 1.1 - F-test
# -----------------------------
# Using alpha = 5% and sigma1^2 / sigma2^2
# as the test statistic, which one of the below values is a critical value for the test?
# (up to two significant digits)

F = Statistics.f_test(sigma1, sigma2)
print(f"F test value is: {F}")

critical_value_1 = f.ppf(0.95, dfn=n1-1, dfd=n2-1)
print(f"1.1 - Critical value at alpha = 5% is: {critical_value_1}")
# So the cirtical value for the test is 3.29
# answer option 1


# -----------------------------
# Question 1.2 - P-value for F-test
# -----------------------------
# Now assume that a new test for the same data is performed for
# H0: mu1 = mu2 against H1: mu1 != mu2

# using sigma1^2 / sigma2^2 as the test statistic
# calculatet the p value for the test

P = Statistics.p_value(F, two_tailed=True)
print(f"1.2 - P value for the test is: {P}")
# answer option 1


# -----------------------------
# Question 1.3 - Critical value for t-test
# -----------------------------
# Using alpha = 1%, what is the critical value for the test?
# with up to three significant digits after the decimal point
crit = t.ppf(0.99, df=n1+n2-2)
print(f"1.3 - Critical value at alpha = 1% is: {crit}")
# So the cirtical value for the test is 2.920
# answer option 1

# -----------------------------
# Question 1.4 - P-value for t-test
# -----------------------------
# Calculatet the p-value for the test in question 1.3
P_value = Statistics.p_value(Statistics.z_test(mean_estimante1, mean_estimante2, sigma1, sigma2, n1, n2), two_tailed=True)
print(f"1.4 - P value for the test is: {P_value}")
# så p-værdien er 0.03
# answer option 2