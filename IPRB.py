# Mendel's First Law

# Import comb (combination operation) from the scipy library
from scipy.special import comb

def calculateProbability(k, m, n):
    # Calculate total number of organisms in the population:
    totalPop = k + m + n
    # Calculate the number of combos that could be made (valid or not):
    totalCombos = comb(totalPop, 2)
    # Calculate the number of combos that have a dominant allele therefore are valid:
    validCombos = comb(k, 2) + k*m + k*n + .5*m*n + .75*comb(m, 2)
    probability = validCombos/totalCombos
    return probability

# Example Call:
print(calculateProbability(2, 2, 2))
# Example Output: 0.783333333333