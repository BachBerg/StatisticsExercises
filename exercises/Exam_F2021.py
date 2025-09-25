import math
from scipy.stats import norm
from scipy.stats import f
from scipy.stats import t
import numpy as np
from StatisticsFunctions import statistics as sf

# PROBLEM 1 FROM EXAM F2021 1.1-1.4

# A sporting goods manufactturing company is working on two new soles
# fr their popular running shoes. They would like to test the
# difference in these new soles with respecct to wear. For that,
# they run some experiements using 20 randomly selected subjects.
# For the same model of running shoes already avaiable in the market,
# for each subject they randomly select one shoe and replace its sole
# with one of the the new soles. That means that for each subject is
# wearing a pair of shoes with one of the shoes with regular sole and
# the other with one of the new soles. Hence, they have 20 subjects
# half of whom wearing a shoe with one of the new soles and the other
# half wearing a shoe with the other new sole. ie n1 = 10 and n2 = 10.
# The subjects were asked to wear the shoes for 3 months and the
# amount of wear (in %) on the new soles was recorded.
n1, n2 = 10, 10
y1, y2 = 11.9, 17.8
sigma1, sigma2 = 6.2, 3.2

# Question 1.1
# we first like to test the quality of the variances i.e.
# H0: sigma1 = sigma2 & H1: sigma1 != sigma2
# using sigma1^2 / sigma2^2 as the test statistic
# which is the smallest significance level that leads to a
# rejection of the null hypothesis?

# we want an F-test of equal variances
F = sf.f_test(sigma1, sigma2)
dfn, dfd = n1 - 1, n2 - 1

# now we compute the p-value(two-sided: we multiply by 2 the one-sided p-value)
P_value = 2 * min(f.cdf(F, dfn, dfd), 1 - f.cdf(F, dfn, dfd))
print(f"1.1 - P: {sf.truncate(P_value,2)}")
# So the smallest alpha that leads to a rejection of the H0 is: 
# answer option 4 - 10 %

