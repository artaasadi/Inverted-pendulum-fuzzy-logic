import fuzzyRules, fuzzySets
import numpy as np
import math

def calculate(input) :
    points = np.linspace(-100, 100, 1000)
    force = fuzzySets.Force(fuzzyRules.Inferrence(fuzzySets.Inputs(input)))
    sum1 = 0
    sum2 = 0
    for p in points :
        sum1 += p * force.get_membership(p)
        sum2 += force.get_membership(p)
    if math.isnan((sum1 / sum2)) :
        return 0
    else :
        return (sum1 / sum2)