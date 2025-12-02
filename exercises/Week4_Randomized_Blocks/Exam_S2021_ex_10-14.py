import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import math
from scipy.stats import norm
from scipy.stats import f, t
from stat_lib.StatisticsFunctions import Statistics


# -----------------------------
# Problem 10-14 FROM exam set s2021 , week 4 exercises
# -----------------------------

# Lane markings on highways need to be regularly  painted. 
# To lower the cost, the municipal authority would like to 
# test the durability of three different paint brands, 
# A, B and C. The test is conducted by painting the lane 
# markings in a segment of a highway and recording the 
# average wear on that segment after two months, which is 
# the same for all experiments. It is decided to use 6 
# replications for each brand in a completely randomized 
# design. The following statistics are obtained after the 
# experimentation:

SST = 560  # total sum of squares
SSE = 390 # error sum of squares

## QUESTION 10
# How many segments of highway are needed for these 
# experiments?

# answer: In a completely randomized design with 3 paint 
# brands (A, B, C) and 6 replications for each brand, 
# the total number of experimental 
# units (highway segments) is simply:
# Total segments=(number of treatments)×(replications per treatment)
Ts = 3 * 6
print(f"10.1 - Total segments: {Ts}")
#answer: 3 = 18 segments

## QUESTION 11
# the p-value for testing the paint is?
k = 3 # number of brands
replications = 6 # replications per brand
N = 18 # segments
# step 1: calculate SSB (SSB can also be called SSTreatments)
SSB = SST - SSE
# step 2: calculate degrees of freedom
dfb = k - 1
dfe = N - k
# step 3: calculate mean squares
MSB = SSB / dfb
MSE = SSE / dfe
# step 4: calculate F statistic
F = MSB / MSE
# step 5: calculate p-value
P = 1 - f.cdf(F, dfb, dfe)
print(f"10.2 - P-value: {Statistics.truncate(P,3)}")
# P =  0.066 , answer is 4

# Since segments are exposed to different intensities of 
# traffic, it is decided that randomly selecting the 
# segments introduces excessive variation. Therefore,
# it is decided to run a new set of experiments and 
# apply all brands of paint in each segment. That is, 
# the experiments are blocked into 6 blocks
# which represents the segments. each segments is then
# divided into 3 pieces in a row to apply the paints.

## QUESTION 12
# Which one of the following is a proper configuration 
# corresponding to the randomized complete block 
# design(RCBD) where each segment of highway constitutes 
# a block?

# answer: In a randomized complete block design (RCBD), 
# each block (segment of highway) contains all treatments
# (paint brands A, B, and C). Therefore, each of the 6
# segments should be divided into 3 pieces, with each
# piece receiving a different paint brand.

# Thus, the proper configuration is: answer 5

## QUESTION 13
# in the new RCBD, the MSBlock is calculated using(Note that 
# y^_i and y^_j, are the average responses for the i'th
# treatment effect and j'th block effect respectively)
# similarly y^ is the grand average

 # SSBlock would be calculated as:
#  SS_block = k * np.sum((y_block_means - y_grand)**2)
# answer: 1

# from the dataset obtained from the new RCBD,
# described above, we have the following sum of squares:
SST = 640 # total sum of squares
SSB = 290
SSE = 160

## QUESTION 14
# what is the p-value for testing the paint effect?

# step 1: calculate degrees of freedom
b = 6
k= 3
dft = k - 1
dfe = (k - 1) * (b - 1)

# step 2: calculate mean squares
MST = SSB / dft
MSE = SSE / dfe

# step 3: calculate F statistic
F_14 = MST / MSE

# step 4: calculate p-value
P_14 = 1 - f.cdf(F_14, dft, dfe)
print(f"14 - P-value: {Statistics.truncate(P_14,5)}")
# P_value = 0.006 , answer is 1(p-value < 0.01) 

