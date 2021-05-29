# Considerando o triangulo com pontos P1 = (1,1) , P2 = (3,1) e P3 = (2,3),
# aplique a matriz de cisalhamento : M1 = [ 1 0.2 ; 0 1], M2 = [ 1 0 ; 0.3 1] e M3 = [ 1 0.2 ; 0.3 1]
# para obter os novos valores para os pontos do triângulo. Implemente isso em matlab (scilab, octave ou phyton)
# e mostre o objeto antes e depois de cada transformação usando o comando plot ou similar.

import numpy as np
import matplotlib.pyplot as plt

# Pontos do triângulo
triangulo = np.matrix('1 1; 3, 1; 2, 3')

# Matrizes de Cisalhamento
M1 = np.matrix('1 0.2; 0 1')
M2 = np.matrix('1 0; 0.3 1')
M3 = np.matrix('1 0.2; 0.3 1')

# Multiplicações
trianguloM1 = triangulo * M1
trianguloM2 = triangulo * M2
trianguloM3 = triangulo * M3

# Plot dos triângulos
fig, axs = plt.subplots(2, 2, constrained_layout=True)
axs[0, 0].set_title("Triângulo Original")
axs[0, 0].fill(triangulo.getA()[:, 0], triangulo.getA()[:, 1])

axs[0, 1].set_title("Triângulo M1")
axs[0, 1].fill(trianguloM1.getA()[:, 0], trianguloM1.getA()[:, 1])

axs[1, 0].set_title("Triângulo M2")
axs[1, 0].fill(trianguloM2.getA()[:, 0], trianguloM2.getA()[:, 1])

axs[1, 1].set_title("Triângulo M3")
axs[1, 1].fill(trianguloM3.getA()[:, 0], trianguloM3.getA()[:, 1])

plt.show()
