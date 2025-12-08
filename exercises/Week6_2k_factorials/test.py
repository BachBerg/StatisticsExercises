import numpy as np
import pandas as pd
from scipy.stats import f

# Given effect estimates
data = pd.DataFrame({
    "A": [-5],
    "B": [4],
    "C": [-8],
    "AB": [0.5],
    "AC": [-3],
    "BC": [0.5],
    "ABC": [1]
})

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
