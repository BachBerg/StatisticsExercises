import numpy as np
import pandas as pd
from scipy.stats import f

### -----------------------
### Exam S2023 - Problem V(17)
### -----------------------


# A 2^3 design in factors A, B and C replicated twice is 
# being considered. The following effect estimates are 
# obtained:
data = pd.DataFrame({
    "A": [-5],
    "B": [4],
    "C": [-8],
    "AB": [0.5],
    "AC": [-3],
    "BC": [0.5],
    "ABC": [1]
})

# the total sum of squares and the average response for 
# the 16 experiments are given as:
SS_Total = 510
y_bar = 30


## Question(17) V.1
# Among the bellow choices which is the minimum 
# significance level that will select all main effects 
# and AC interaction as significant?
#options 1%, 2,5%, 5%, 10%, 25%, do not know.

# Given effect estimates


SS_Total = 510
r = 2               # replicates
k = 3               # number of factors
n_runs = 2**k * r    # total experiments = 16

# SS formula factor
SS_factor = r * 2**(k-2)   # = 4

# Calculate SS for each effect
SS_effects = 4 * data**2
SS_effects = SS_effects.iloc[0]

# Model and error SS
SS_model = SS_effects.sum()
SS_error = SS_Total - SS_model

# Degrees of freedom
df_total = n_runs - 1       # 15
df_model = len(SS_effects)  # 7
df_error = df_total - df_model  # 8

# Mean squared error
MSE = SS_error / df_error

# Calculate F-values
F_values = SS_effects / MSE

print("Sum of squares for each effect:")
print(SS_effects)
print("\nF-values:")
print(F_values)

# Only main effects and AC
important_effects = ["A", "B", "C", "AC"]
min_F = F_values[important_effects].min()

# Possible significance levels
alphas = [0.10, 0.05, 0.025, 0.01]

# Check smallest alpha where all are significant
for alpha in sorted(alphas):   # go from 1% → 10%
    F_crit = f.ppf(1 - alpha, 1, df_error)
    if min_F > F_crit:
        chosen_alpha = alpha
        break

print("\nSmallest F among A, B, C, AC:", round(min_F, 2))
print("Minimum significance level:", chosen_alpha * 100, "%")
print("-----------------------")


### Problem IV(12)
# A factorial design in three factors A, B and C is used 
# for experimentation. The factor A is a categorical 
# factor and needs to be tested at 4 levels, but factors 
# B and C are quantitative factors and are tested at 2 
# levels. So, it is decided to tun a (4x2x2) factorial 
# design replicated twice yielding 32 experiments in 
# total. Together with SS_total=1448, the following 
# sums of squares are obtained:
# effect | SS
#   A    |  360
#   B    |  90
#   C    |  180
#  AB    |  30
#  AC    |  270
#  BC    |  50
#  ABC   |  60
## for questions 11 and 12 assume that the full model 
# with main effects, the second order interactions and 
# the third order interactions is used.

# Given data
SS_total = 1448

SS_effects = {
    "A": 360,
    "B": 90,
    "C": 180,
    "AB": 30,
    "AC": 270,
    "BC": 50,
    "ABC": 60
}

# Design info
levels = {"A": 4, "B": 2, "C": 2}
replicates = 2

# Total runs: 4 × 2 × 2 × 2
n_runs = 4 * 2 * 2 * replicates
df_total = n_runs - 1

# Degrees of freedom
df = {
    "A": levels["A"] - 1,
    "B": levels["B"] - 1,
    "C": levels["C"] - 1,
    "AB": (levels["A"] - 1) * (levels["B"] - 1),
    "AC": (levels["A"] - 1) * (levels["C"] - 1),
    "BC": (levels["B"] - 1) * (levels["C"] - 1),
    "ABC": (levels["A"] - 1) * (levels["B"] - 1) * (levels["C"] - 1)
}

# Model SS and df
SS_model = sum(SS_effects.values())
df_model = sum(df.values())

# Error
SS_error = SS_total - SS_model # = 408
df_error = df_total - df_model # = 16
MSE = SS_error / df_error # = 25.5

# The R^2_adj (adjusted R^2) of the full model is:
R2_adj = 1 - (SS_error / df_error) / (SS_total / df_total)
print("\nAdjusted R² of the full model:", round(R2_adj, 2))
print("-----------------------")

# Assuming that the lack of fit is not significant 
# the R^2_adj of the reduced model:

# Adjusted MSE for reduced model
MSE_reduced = (SS_error + 140) / 23

# Adjusted R²
R2_adj_reduced = 1 - MSE_reduced / (SS_total / df_total)
print("Adjusted R² (reduced model):", round(R2_adj_reduced, 2))
print("-----------------------")