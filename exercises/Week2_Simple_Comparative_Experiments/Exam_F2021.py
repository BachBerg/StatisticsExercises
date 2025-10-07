import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import math
from scipy.stats import norm
from scipy.stats import f, t
from stat_lib.StatisticsFunctions import Statistics

# -----------------------------
# PROBLEM 1 FROM EXAM F2021 1.1-1.4
# -----------------------------
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

# -----------------------------
# Question 1.1 - F-test for equal variances
# -----------------------------
# we first like to test the quality of the variances i.e.
# H0: sigma1 = sigma2 & H1: sigma1 != sigma2
# using sigma1^2 / sigma2^2 as the test statistic
# which is the smallest significance level that leads to a
# rejection of the null hypothesis?

# we want an F-test of equal variances
F = Statistics.f_test(sigma1, sigma2)
dfn, dfd = n1 - 1, n2 - 1

# now we compute the p-value(two-sided: we multiply by 2 the one-sided p-value)
P_value = 2 * min(f.cdf(F, dfn, dfd), 1 - f.cdf(F, dfn, dfd))
print(f"1.1 - P: {Statistics.truncate(P_value,2)}")
# So the smallest alpha that leads to a rejection of the H0 is: 0.06
# answer option 4: 10 %



# -----------------------------
# Question 1.2 - P-value for t-test
# -----------------------------

# Assuming that the true variances are the same and unknown
# calculate the p-value for the test of
# H0: mu1 = mu2 against H1: mu1 != mu2

df = n1 + n2 - 2
Sp2 = ((n1 - 1) * sigma1**2 + (n2 - 1) * sigma2**2) / df
Sp = math.sqrt(Sp2) # pooled standard deviation
Se = Sp * math.sqrt(1/n1 + 1/n2) # standard error

t0 = (y1 - y2) / Se # test statistic
# the survival function (1-CDF) gives the area to the right of t0
# i.e. the one-tailed p-value, so we multiply by 2 for two
# the smallest alpha that rejects H0 the test is then the p-value
P_value = 2 * t.sf(abs(t0), df)
print(f"1.2 - P value for the test is: {Statistics.truncate(P_value,2)}")
# So the smallest alpha that rejects H0 the test is 0.03



# -----------------------------
# Question 1.3 - Critical value for t-test
# -----------------------------
# For the above hypothesis test, the manufacturer would like to know a 
# differnece of 8% wear in the emnas ie mu1 = mu2 + 8
# with  a high certanty. What will be the probability
# of detecting such a difference in the menas 
# i.e. rejecting the null hypothesis when mu1 = mu2 + 8,
# using a significane level of 5%
# (assume true variances are the same and equal to 16)

alpha = 0.05
n1 = n2 = 10
sigma2 = 16  # variance
delta = 8  # difference in means we want to detect

Se = math.sqrt(sigma2/n1 + sigma2/n2)
t_obs = delta / Se

z_alpha = norm.ppf(1 - alpha/2)
P_reject = norm.cdf(t_obs - z_alpha) + (1 - norm.cdf(t_obs + z_alpha))
print("1.3 - P_reject:", Statistics.truncate(P_reject, 3))
# Output ≈ 0.994

