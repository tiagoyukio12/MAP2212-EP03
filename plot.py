import sobol_seq
import chaospy
import matplotlib.pyplot as plt

sobolSeq = sobol_seq.i4_sobol_generate(2, 25000)
x = sobolSeq[:, 0]
y = sobolSeq[:, 1]

plt.scatter(x, y, s=0.25)
plt.show()

sobolSeq = sobol_seq.i4_sobol_generate(2, 4675)
x = sobolSeq[:, 0]
y = sobolSeq[:, 1]

plt.scatter(x, y, s=1)
plt.show()

a = 1
b = 1.5
distribution = chaospy.Beta(a, b)
betaSeq = distribution.sample(25000, 'S')
plt.hist(betaSeq, bins=100)
plt.show()