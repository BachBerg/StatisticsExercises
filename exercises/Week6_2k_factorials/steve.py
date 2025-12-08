import numpy as np
import pandas as pd

# Create design matrix
data = pd.DataFrame({
    "A": [-1, 1, -1, 1],
    "B": [-1, -1, 1, 1],
    "y": [90, 100, 60, 80]
})

# Create interaction column
data["AB"] = data["A"] * data["B"]

print(data)
print("-----------------")

### Calculate contrasts
def contrast(data, column):
    return np.sum(data[column] * data["y"])

k = 2
n = 1

C_A = contrast(data, "A")
C_B = contrast(data, "B")
C_AB = contrast(data, "AB")

print("Contrast A:", C_A)
print("Contrast B:", C_B)
print("Contrast AB:", C_AB)
print("-----------------")

### EFFECTS
effect_A = C_A / (2**(k-1) * n)
effect_B = C_B / (2**(k-1) * n)
effect_AB = C_AB / (2**(k-1) * n)

print("Effect A:", effect_A)
print("Effect B:", effect_B)
print("Effect AB:", effect_AB)
print("-----------------")

### SUM OF SQUARES
SS_A = C_A**2 / (2**k * n)
SS_B = C_B**2 / (2**k * n)
SS_AB = C_AB**2 / (2**k * n)

print("SS A:", SS_A)
print("SS B:", SS_B)
print("SS AB:", SS_AB)
print("-----------------")


### TOTAL SUM OF SQUARES
y_mean = np.mean(data["y"])

SST = np.sum((data["y"] - y_mean)**2)
SSE = SST - (SS_A + SS_B + SS_AB)

print("SST:", SST)
print("SSE:", SSE)
print("-----------------")