import math
from scipy.stats import beta as betaDistr

def run(alpha, beta, betaSeq):
    sumDiv = 0
    sumDiv2 = 0
    n = 0
    errorIsBig = True
    a = 1
    b = 1.5
    
    seqIter = iter(betaSeq)
    
    while errorIsBig:
        x = next(seqIter)  # Utiliza a seq Sobol e itera para o prox.
        fx = math.exp(-alpha * x) * math.cos(beta * x)
        gx = betaDistr.pdf(x, a, b)
        
        sumDiv += fx / gx
        sumDiv2 += (fx / gx) ** 2
        n += 1
        
        # Criterio de parada
        if n > 100:
            estGamma = sumDiv / n
            varGamma = (sumDiv2 / n - (sumDiv / n) ** 2) / (n - 1)
            relError = varGamma ** 0.5 / estGamma
            errorIsBig = relError > 0.01
    
    return (estGamma, n)