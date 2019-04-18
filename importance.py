import math
import numpy
from scipy.stats import beta as betaFunc

def exec(alpha, beta):
    sumDiv = 0
    sumDiv2 = 0
    n = 0
    errorIsBig = True
    a = 1
    b = 1.5
    
    while errorIsBig:
        x = numpy.random.beta(a, b)
        fx = math.exp(-alpha * x) * math.cos(beta * x)
        gx = betaFunc.pdf(x, a, b)
        
        sumDiv += fx / gx
        sumDiv2 += (fx / gx) ** 2
        n += 1
        
        # Criterio de parada
        if n > 30:
            estGamma = sumDiv / n
            varGamma = (sumDiv2 / n - (sumDiv / n) ** 2) / (n - 1)
            relError = varGamma ** 0.5 / estGamma
            errorIsBig = relError > 0.01 / 1.96
    
    return (estGamma, n)