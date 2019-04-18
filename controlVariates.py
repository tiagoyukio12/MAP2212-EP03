import math
import random

def exec(alpha, beta):
    sumDiff = 0
    sumDiff2 = 0
    n = 0
    errorIsBig = True
    sumVarGamma = 0
    integral = 0.77461  # integral conhecida de e^(-0.53454806*x) entre 0 e 1
    
    while errorIsBig:
        x = random.random()
        fx = math.exp(-alpha * x) * math.cos(beta * x)
        px = math.exp(-alpha * x)
        
        sumDiff += fx - px
        sumDiff2 += (fx - px) ** 2
        n += 1
        
        if n > 30:
            estGamma = integral + sumDiff / n
            varGamma = (sumDiff2 / n - (sumDiff / n) ** 2) / (n - 1)
            relError = varGamma ** 0.5 / estGamma
            errorIsBig = relError > 0.01 / 1.96
    
    return (estGamma, n)