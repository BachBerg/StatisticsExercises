import math


class Statistics:

    # --------------------
    # Descriptive statistics
    # --------------------
    @staticmethod
    def mean(data):
        return sum(data) / len(data) if data else 0

    @staticmethod
    def median(data):
        if not data:
            return 0
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2 if n % 2 == 0 else sorted_data[mid]

    @staticmethod
    def mode(data):
        if not data:
            return None
        frequency = {}
        for item in data:
            frequency[item] = frequency.get(item, 0) + 1
        max_count = max(frequency.values())
        modes = [k for k, v in frequency.items() if v == max_count]
        return None if len(modes) == len(frequency) else modes

    @staticmethod
    def variance(data):
        if not data:
            return 0
        m = Statistics.mean(data)
        return sum((x - m) ** 2 for x in data) / len(data)

    @staticmethod
    def standard_deviation(data):
        return math.sqrt(Statistics.variance(data))

    # --------------------
    # Hypothesis testing
    # --------------------
    @staticmethod
    def z_test(mean1, mean2, sigma1, sigma2, n1, n2):
        numerator = mean1 - mean2
        denominator = math.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
        return numerator / denominator

    @staticmethod
    def p_value(z0, two_tailed=True):
        # lazy import avoids unnecessary import if method is never called
        from scipy.stats import norm
        if two_tailed:
            return 2 * (1 - norm.cdf(abs(z0)))
        return 1 - norm.cdf(z0)

    @staticmethod
    def f_test(sigma1, sigma2):
        return (sigma1 ** 2) / (sigma2 ** 2)

    @staticmethod
    def truncate(number, digits):
        """
        Truncate a float to a fixed number of decimal places without rounding.
        Handles negative numbers correctly.
        """
        if digits < 0:
            raise ValueError("digits must be non-negative")
        
        factor = 10.0 ** digits
        if number >= 0:
            return math.floor(number * factor) / factor
        else:
            return math.ceil(number * factor) / factor

    # --------------------
    # ANOVA
    # --------------------
    @staticmethod
    def ss_between(groups, grand_mean):
        return sum(len(g) * (Statistics.mean(g) - grand_mean) ** 2 for g in groups)

    @staticmethod
    def ss_within(groups):
        return sum(sum((x - Statistics.mean(g)) ** 2 for x in g) for g in groups)

    @staticmethod
    def ss_total(groups, grand_mean):
        return sum(sum((x - grand_mean) ** 2 for x in g) for g in groups)

    @staticmethod
    def df_between(groups):
        return len(groups) - 1

    @staticmethod
    def df_within(groups):
        return sum(len(g) - 1 for g in groups)

    @staticmethod
    def ms_between(ssb, dfb):
        return ssb / dfb if dfb != 0 else 0

    @staticmethod
    def ms_within(ssw, dfw):
        return ssw / dfw if dfw != 0 else 0

    @staticmethod
    def eta_squared(ssb, sst):
        return ssb / sst if sst != 0 else 0

    @staticmethod
    def omega_squared(ssb, ssw, dfb, dfw):
        """
        Calculate omega squared effect size for ANOVA.

        Parameters:
            ssb : float - sum of squares between
            ssw : float - sum of squares within
            dfb : int   - degrees of freedom between
            dfw : int   - degrees of freedom within

        Returns:
            float - omega squared (0 if denominator is 0)
        """
        if dfw == 0:
            return 0
        msw = ssw / dfw
        denominator = ssb + ssw + msw
        numerator = ssb - dfb * msw
        return numerator / denominator if denominator != 0 else 0

