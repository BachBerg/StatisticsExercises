import math
from scipy.stats import norm
from scipy.stats import f
from scipy.stats import t
import numpy as np
from StatisticsFunctions import statistics as sf

# PROBLEM 1 FROM EXAM S2021 1.1-1.5
# A govermental agency needs to make a comparative test of two vacines
# as they use different technologies. A small emergency study is 
# conducted with 32 participants who are randomly split into two groups
# of 16 participants for each vaccine. After 30 days of administering
# the vaccines, the antibody levels of each participant were measured.
# However, 6 participants for the first vacine dropped out of the trial
# hence we have
n1, n2 = 10, 16
# The following average and standard deviations are calculated
y1, y2 = 11.8, 13.9
sigma1, sigma2 = 3.6, 2.1

# Question 1.1
# we first like to test the quality of the variances i.e.
# H0: sigma1 = sigma2 & H1: sigma1 != sigma2

# using alpha = 5% and sigma1^2 / sigma2^2 as the test statistic
# calculate the critical values for the test


crit = f.ppf(0.95,n1-1,n2-1)
print(f"1.1 - Critical value at alpha = 5% is: {sf.truncate(crit,3)}")
# So the cirtical value for the test is 2.587
# answer option 2




# Question 1.2
# What is the 95% two-sided confidence interval for sigma1^2 / sigma2^2?
lower_crit = f.ppf(1-0.05/2, n1-1, n2-1)
upper_crit = f.ppf(0.05/2, n1-1, n2-1)

# using the Confidence interval formula for the ration of variances
RoV = sigma1**2/sigma2**2

print(f"1.2 - {RoV/lower_crit}, {RoV/upper_crit}")
# So the 95% two-sided confidence interval is (0.941, 11.077)
# answer option 3




# Question 1.3
# for question 1.3-1.5 we assume that the true variances are equal but
# unknown ie sigma1 = sigma2 = sigma
# we like to test H0: mu1 = mu2 & H1: mu1 != mu2

# calculate the smallest significance level that leads to a rejection of
# null hypothesis

df = n1 + n2 - 2
Sp2 = ((n1-1)*sigma1**2 + (n2-1)*sigma2**2) / df
Sp = math.sqrt(Sp2)
Se = Sp * math.sqrt(1/n1 + 1/n2)
t0 = (y1 - y2) / Se

# the survival function (1-CDF) gives the area to the right of t0
# i.e. the one-tailed p-value, so we multiply by 2 for two-tailed
# the smallest alpha that rejects H0 the test is then the p-value

P_value = 2 * t.sf(np.abs(t0), df)
print(f"1.3 - P value for the test is: {sf.truncate(P_value,2)}")
# So the smallest alpha that rejects H0 the test is 0.071
# answer option 4 - 10 %

# Question 1.4
# find the 95% two-sided confidence interval for mu1 - mu2
# with up to two significant digits after the decimal point
margin_of_error = t.ppf(0.975, df) * Se

ci_lower = (y1 - y2) - margin_of_error
ci_upper = (y1 - y2) + margin_of_error
print(f"1.4 - mu1 - mu2 is: ({sf.truncate(ci_lower,2)}, {sf.truncate(ci_upper,2)})")
# So the 95% two-sided confidence interval
# for mu1 - mu2 is (-4.396, 0.19)
# answer option 5



# Question 1.5
# what is the minimun sample size for each group ie. n1 = n2 = n
# so that the power of the above test of the means is above 75%
# for a difference of sigma in the means i.e. |mu1 - mu2| = sigma?
# using alpha = 5%
alpha = 0.05
power = 0.75

# Sp is the pooled standard deviation, calculated above as:
# Sp = math.sqrt(Sp2)
# where Sp2 = ((n1-1)*sigma1**2 + (n2-1)*sigma2**2) / df
# It is used as an estimate of the common standard deviation when variances are assumed equal.
effect_size = Sp / Sp  # since we want |mu1 - mu2| = sigma
z_alpha = norm.ppf(1 - alpha / 2)

z_beta = norm.ppf(power)

n = 2 * ((z_alpha + z_beta)**2 / effect_size**2)
print(f"1.5 - n: {sf.truncate(n,2)}")
# So the minimum sample size for each group is 16
# answer option 