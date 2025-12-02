import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import math
from scipy.stats import norm
from scipy.stats import f, t
from stat_lib.StatisticsFunctions import Statistics

# -----------------------------
# PROBLEM 2 FROM EXAM F2022 Q 2.1 - 2.2
# -----------------------------

# A manufacturing company is testing three different machines (M1, M2 and M3) 
# for their production. If there is no difference in the performances of these machines, 
# they aim to buy the cheapest one. For each machine they ran 5 tests(replications) 
# resulting in 15 randomly run tests.

# The proposed model is:
# y_ij = mu + tau_i + epsilon_ij
# where mu is the overall mean tau_i is the i'th machine effect with the sum of tau_i i=1 -> i=3 = 0
# epsilon_ij is the experimental error with NID(0, sigma^2)

# the following sum of squares are given:
SSM = 1180
SST = 3260

## QUESTION 2.1
# which of the following statements is correct for the above design?

# 1 - This is a randomized complete block design - false
    # No blocking factor is described; each test is a replication but there are no blocks that contain all treatments.

# 2 - The machines is a random effect - false
    # A random effect would mean the three machines are a random sample from a larger population and interest is in variance components.
    # The problem states specific machines (M1–M3) that the company wants to compare, so treating them as random is inappropriate.

# 3 - the machine is a fixed effect - true
    # The machines are specific treatments of direct interest (the company may choose one), so machine is a fixed factor in a one-way ANOVA.

# 4  The proposed model is called the means-model - true
    # the model is the standard one-way ANOVA (treatment/means) model — often called the means model or treatment effects model.

# 5 - none of the above - false
# 6  - do not know - false
# so 3 & 4 are correct

### Question 2.2
# What is the p-value for testing the machine effect?

SSE = SST - SSM
dfT = 3 - 1 # degrees of freedom for the treatments
dfE = 15 - 3 # degrees of freedom for the error


MSM = SSM / dfT # mean square for the treatments
MSE = SSE / dfE # mean square for the error
F = MSM / MSE # F statistic

P_value = 1 - f.cdf(F, dfT, dfE)
print(f"2.2 - P: {Statistics.truncate(P_value,3)}")
# P-value is 0.06