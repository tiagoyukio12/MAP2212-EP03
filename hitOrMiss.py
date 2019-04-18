import random
import math

def exec(alpha, beta):
    hit = 0
    n = 0
    errorIsBig = True
    
    while errorIsBig:
        x = random.random()
        y = random.random()
        fx = math.exp(-alpha * x) * math.cos(beta * x)
            
        if y <= fx:
            hit += 1
        n += 1
        
        if n > 30:
            relError = (hit - hit ** 2/ n) ** 0.5 / hit
            errorIsBig = relError > 0.01 / 1.96
    
    estGamma = hit / n
    
    return (estGamma, n)