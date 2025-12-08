import statsmodels.api as sm
from itertools import product
import numpy as np
import pandas as pd

# Generate a 2^3 design
design = pd.DataFrame(list(product([-1,1], repeat=3)), columns=["A", "B", "C"])

# Example response values (replace with your data)
design["y"] = [1154,1319,1234,1277,2089,1617,2178,1589]

# Add interactions
design["AB"] = design["A"] * design["B"]
design["AC"] = design["A"] * design["C"]
design["BC"] = design["B"] * design["C"]
design["ABC"] = design["A"] * design["B"] * design["C"]

# Regression model
X = design[["A","B","C","AB","AC","BC","ABC"]]
X = sm.add_constant(X)  # adds intercept
y = design["y"]

model = sm.OLS(y, X).fit()
print(model.summary())
