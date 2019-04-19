import math

def exec(alpha, beta, sobolSeq):
    hit = 0
    n = 0
    errorIsBig = True
    seqIter = iter(sobolSeq)
    
    while errorIsBig:
        x, y = next(seqIter)
        fx = math.exp(-alpha * x) * math.cos(beta * x)
            
        if y <= fx:
            hit += 1
        n += 1
        
        if n > 30:
            relError = (hit - hit ** 2/ n) ** 0.5 / hit
            errorIsBig = relError > 0.01
    
    estGamma = hit / n
    
    return (estGamma, n)