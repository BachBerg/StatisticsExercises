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

# A pharmacutical company is testing four different drug
# formulations(A, B, C and D) on mice. The tests are replicated
# 4 times for all formulations resulting in 16 randomly
# selected mice. The proposed model is:

# y_ij = mu + tau_i + epsilon_ij
# where mu si the overall mean tau_i is the i'th formulation effect
# with the sum of tau_i i=1 -> i=4 = 0
# epsilon_ij is the experimental error with NID(0, sigma^2)

# the following sum of squares are given:
SSF =52.5 # sum of squares for the formulations
SST = 121 # total sum of squares

## QUESTION 2.1
# whhich of the following statements is correct for the above design?

# 1 - The degrees of freedom for the pure error is 4
    # Pure error degrees of freedom = total observations − number of treatment means
    # There are 16 observations and 4 treatments → df_pure_error = 16 − 4 = 12
    # so 1 is incorrect

# 2  This is latin square design
    # Latin square design requires two blocking factors (rows and columns), with treatments arranged so that each treatment appears exactly once per row and column.
    # Here, there is no mention of two blocking factors, only 16 mice randomly assigned to 4 treatments.
    # so 2 is incorrect

# 3 - The mice are the block effect
    # A block effect implies that we explicitly account for blocks in the model (like row or column in a Latin square).
    # Here, each mouse seems to be a random experimental unit, not a block.
# 4 - all of the above
    # Since 1, 2, and 3 are all incorrect → statement 4 is incorrect.
# 5 - None of the above
    # Correct :)
# 6  - do not know


## QESTION 2.2
# What is the p-value for testing the formulation?

# H0: tau_1 = tau_2 = tau_3 = tau_4 = 0
# H1: at least one tau_i != 0

dfT = 4 - 1 # degrees of freedom for the treatments
dfE = 16 - 4 # degrees of freedom for the error


MST = SSF / dfT # mean square for the treatments
MSE = (SST - SSF) / dfE # mean square for the error

F = MST / MSE # F statistic

P_value = 1 - f.cdf(F, dfT, dfE)
print(f"2.2 - P: {Statistics.truncate(P_value,2)}")