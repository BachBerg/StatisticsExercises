import math
from scipy.stats import norm
import numpy as np


class statistics():
    def __init__(self):
        pass

    def mean(self, data):
        if not data:
            return 0
        return sum(data) / len(data)

    def median(self, data):
        if not data:
            return 0
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self, data):
        if not data:
            return None
        frequency = {}
        for item in data:
            frequency[item] = frequency.get(item, 0) + 1
        max_count = max(frequency.values())
        modes = [key for key, count in frequency.items() if count == max_count]
        if len(modes) == len(frequency):
            return None  # No mode
        return modes
        
    def variance(self, data):
        if not data:
            return 0
        mean_value = self.mean(data)
        return sum((x - mean_value) ** 2 for x in data) / len(data)
    
    def standard_deviation(self, data):
        return math.sqrt(self.variance(data))

    def z_test(mean1, mean2, sigma1, sigma2, n1, n2):
        numerator = mean1 - mean2
        denominator = math.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
        z0 = numerator / denominator
        return z0

    def p_value(z0, two_tailed=True):
        if two_tailed:
            p = 2 * (1 - norm.cdf(abs(z0)))
        else:
            p = 1 - norm.cdf(z0)
        return p

    def f_test(sigma1, sigma2):
        return (sigma1 * sigma1) / (sigma2 * sigma2)


    def truncate(number, digits) -> float:
        # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
        nbDecimals = len(str(number).split('.')[1]) 
        if nbDecimals <= digits:
            return number
        stepper = 10.0 ** digits
        return math.trunc(stepper * number) / stepper
    

    ## ---------------------------------------
    ## ANOVA functions
    ## ---------------------------------------
    
    def ss_between(groups, grand_mean, self):
        ssb = sum(len(group) * (self.mean(group) - grand_mean) ** 2 for group in groups)
        return ssb
    
    def ss_within(groups, self):
        ssw = sum(sum((x - self.mean(group)) ** 2 for x in group) for group in groups)
        return ssw
    
    def ss_total(groups, grand_mean):
        sst = sum(sum((x - grand_mean) ** 2 for x in group) for group in groups)
        return sst
    
    # degrees of freedom
    def df_between(groups):
        return len(groups) - 1
    
    def df_within(groups):
        return sum(len(group) - 1 for group in groups)
    
    # mean squares
    def ms_between(ssb, dfb):
        return ssb / dfb if dfb != 0 else 0
    
    def ms_within(ssw, dfw):
        return ssw / dfw if dfw != 0 else 0
    
    ## effect size
    def eta_squared(ssb, sst):
        return ssb / sst if sst != 0 else 0
    
    def omega_squared(ssb, ssw, dfb, dfw):
        return (ssb - (dfb * (ssw / dfw))) / (ssb + ssw + (ssw / dfw)) if (ssb + ssw + (ssw / dfw)) != 0 else 0
    
