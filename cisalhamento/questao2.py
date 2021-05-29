# Faça uma transformação em cisalhamento no cubo unitário, que tem um dos seus pontos na origem (0,0,0),
# usando a seguinte matriz M1 = [1 0.4 0; 0 1 0; 0 0 1]. Faça o mesmo para esta outra matriz M2 = [1 0 0; 0.4 1 0; 0
# 0 1] de transformação. Implemente isso em matlab (scilab, octave ou python) e mostre o objeto antes e depois de
# cada transformação usando o comando plot ou similar.
from itertools import combinations
import numpy as np
from matplotlib import pyplot as plt

# Cubo Unitário, considerando sua origem em (0, 0, 0)
cubo_unitario = np.matrix('0 0 0; 0 1 0; 1 0 0; 1 1 0; '
                          '0 0 1; 0 1 1; 1 0 1; 1 1 1')

# Matrizes de Cisalhamento
M1 = np.matrix('1 0.4 0; 0 1 0; 0 0 1')
M2 = np.matrix('1 0 0; 0.4 1 0; 0 0 1')

# Multiplicação
cubo_unitarioM1 = cubo_unitario * M1
cubo_unitarioM2 = cubo_unitario * M2

# Plot dos cubos
fig = plt.figure(figsize=(7, 14), constrained_layout=True)

# Plot do Cubo Unitário Original
ax = fig.add_subplot(311, projection='3d')
ax.set_title("Cubo Unitário Original")

for s, e in combinations(cubo_unitario.getA(), 2):
    if np.sum(np.abs(s - e)) == cubo_unitario.max() - cubo_unitario.min():
        ax.plot3D(*zip(s, e), color="green")

# Plot do Cubo Unitário M1
ax = fig.add_subplot(312, projection='3d')
ax.set_title("Cubo Unitário M1")

for s, e in combinations(cubo_unitarioM1.getA(), 2):
    if np.sum(np.abs(s - e)) <= cubo_unitarioM1.max() - cubo_unitarioM1.min():
        ax.plot3D(*zip(s, e), color="green")

# Plot do Cubo Unitário M2
ax = fig.add_subplot(313, projection='3d')
ax.set_title("Cubo Unitário M2")

for s, e in combinations(cubo_unitarioM2.getA(), 2):
    if np.sum(np.abs(s - e)) <= cubo_unitarioM2.max() - cubo_unitarioM2.min():
        ax.plot3D(*zip(s, e), color="green")

plt.show()
