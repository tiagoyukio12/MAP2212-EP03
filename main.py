import sobol_seq
import chaospy
import crude
import hitOrMiss
import importance
import controlVariates

import matplotlib.pyplot as plt

# Parametros de f(x)
alpha = 0.534548064
beta = 0.9350011

gReal = 0.6804991098  # Valor real da integral. Nao usado no criterio de parada,
                      # apenas na verificacao posterior do erro relativo.

name = ["CRUDE", "HIT OR MISS", "IMPORTANCE SAMPLING", "CONTROL VARIATES"]
g = [0, 0, 0, 0]
n = [0, 0, 0, 0]

sobolSeq = sobol_seq.i4_sobol_generate(2, 25000)
a = 1
b = 1.5
distribution = chaospy.Beta(a, b)
betaSeq = distribution.sample(25000, 'S')

# Recebe o valor esperado de gamma e o numero de iteracoes por metodo
g[0], n[0] = crude.run(alpha, beta, sobolSeq)
g[1], n[1] = hitOrMiss.run(alpha, beta, sobolSeq)
g[2], n[2] = importance.run(alpha, beta, betaSeq)
g[3], n[3] = controlVariates.run(alpha, beta, sobolSeq)

for i in range(len(g)):
    print(name[i])
    print("Estimativa de gamma: " + str(g[i]))
    print("Numero de iteracoes: " + str(n[i]))
    relError = 100 * abs(gReal - g[i]) / gReal
    print("Erro relativo: " + "{:3.4f}".format(relError) + " %" + "\n")