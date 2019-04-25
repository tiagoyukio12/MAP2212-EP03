import math

def run(alpha, beta, sobolSeq):
    sumFx = 0
    sumFx2 = 0
    n = 0
    errorIsBig = True
    seqIter = iter(sobolSeq)

    while errorIsBig:
        x = next(seqIter)[0]
        fx = math.exp(-alpha * x) * math.cos(beta * x)
        
        sumFx += fx
        sumFx2 += fx ** 2
        n += 1
        
        if n > 30:
            estGamma = sumFx / n
            varGamma = (sumFx2 / n - (sumFx / n) ** 2) / (n - 1)
            relError = varGamma ** 0.5 / estGamma
            errorIsBig = relError > 0.01
    
    return (estGamma, n)