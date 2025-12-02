import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import math
from scipy.stats import norm
from scipy.stats import f, t
from stat_lib.StatisticsFunctions import Statistics


# -----------------------------
# PROBLEM 2 FROM EXAM s2024 6-8
# -----------------------------

# A factorial design in three factors A, B and C is used 
# for experimentation. The factors B and C are tested 
# at 3 levels whereas factor A is tested at 4 levels. 
# the design is replicated two times yielding (4x3x3)x2=72 
# experiments in total. We first consider the full model 
# with all the main effects and interactions.

# for question 6,7 and 8, assume that the three-factor 
# interaction is deemed insignificant and dropped out of 
# the model.
# Furthermore, also assume that the experimentation took 
# 2 days. But instead of running all 72 experiments in a 
# completely randomized way, each replicate is run on one 
# day. to account and test for a possible day to day block 
# effect, each replicate is then considered as a block. 
# Note that the experiments within a day are run in a 
# randomized order. we as per usual assume that the 
# interaction between the blocks and treatments is negligible.


## QUESTION 6
# what are the degrees of freedom for the block effect?

# the experimentation took 2 days, so there are 2 blocks
dfb = 2 -1
# answer: 1, option 2


## QUESTION 7
# what is the degrees of freedom for the pure error?

# given that the replicates have been split into blocks
#  there are no more replicates. thus, the degrees of 
# freedom for the pure error is 0
df_pure_error = 0
# answer: 0, option 1


## QUESTION 8
# the degrees of freedom for the lack of fit is:
# step 1 - total degrees of freedom
df_total = 72-1

# step 2 calculate model degrees of freedom
df_a = 4 - 1
df_b = 3 - 1
df_c = 3 - 1
#two factor interactions:
AB = df_a * df_b
AC = df_a * df_c
BC = df_b * df_c

df_block= 2- 1

df_model = df_a + df_b + df_c + AB + AC + BC

# step 3 - error degrees of freedom
dfe = df_total - df_model
# step 4 - lack of fit degrees of freedom
df_LOF = df_total - df_pure_error - df_model - df_block
print(f"8 - df lack of fit: {df_LOF}")
# answer: df_LOF = 47, option 4

