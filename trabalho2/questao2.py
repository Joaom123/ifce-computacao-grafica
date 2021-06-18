"""
2) Componha uma cena contendo os diversos sólidos modelados anteriormente
em um sistema de coordenadas do mundo, de tal maneira a não haver
sobreposição ou intersecção entre tais objetos.

a. O cubo e a pirâmide devem estar localizados em apenas um octante do
espaço, bem como o paralelepípedo e o tronco devem estar em apenas
um octante. Além disso, pelo menos dois octantes adjacentes devem
possuir sólidos.

b. O maior valor possível para cada uma das componentes de um vértice é 6.
Se necessário aplique transformações de escala para que os sólidos
sejam localizados respeitando tais limites.

c. Apresente os diversos sólidos neste sistema de coordenadas em 3D.
"""
import matplotlib.pyplot as plt
import numpy

from trabalho2.Cubo import Cubo
from trabalho2.Paralelepipedo import Paralelepipedo

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

cubo = Cubo()
cubo.adiciona_matriz(10)

paralelepipedo = Paralelepipedo()

for vertice in cubo.converte_vertices_para_matriz():
    ax.scatter(vertice[0], vertice[1], vertice[2])

for vertice in paralelepipedo.converte_vertices_para_matriz():
    ax.scatter(vertice[0], vertice[1], vertice[2])

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_zlim(-20, 20)

plt.show()
