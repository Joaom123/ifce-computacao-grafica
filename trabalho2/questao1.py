"""
1) Modele os seguintes sólidos/objetos

a. cubo de lado igual a 1.5, com origem no centro do quadrado inferior do
cubo e aresta do quadrado inferior paralela ao eixo x;

b. paralelepípedo com lados iguais a 1.5 em x, 5.0 em y e 2.5 em z, com origem em
um dos vértices pertencentes ao retângulo inferior e aresta paralela ao eixo y;

c. pirâmide com base quadrada de lado igual a 2.0 e altura igual a 3.0, com
origem no centro do quadrado da pirâmide e de tal maneira que uma
aresta do quadrado faça ângulo de 45 graus com o eixo x; e

d. tronco de pirâmide com bases quadradas de lados, respectivamente, iguais a 3.0 e 1.3, com altura de 2.5.

Na construção dos sólidos, considere vértices e arestas, de tal maneira que cada
um seja descrito em termos de seu próprio sistema de coordenadas de objeto.
"""
from matplotlib import pyplot as plt

from trabalho2.Cubo import Cubo
from trabalho2.Paralelepipedo import Paralelepipedo

cubo = Cubo()
cubo.set_vertices(10)
print()

vertices1 = cubo.vertices
arestas = cubo.arestas

fig = plt.figure(constrained_layout=True)
ax = fig.add_subplot(111, projection='3d')

for nome, vertice in vertices1.items():
    ax.scatter(vertice[0], vertice[1], vertice[2])
    # ax.text(vertice[0], vertice[1], vertice[2], nome, size=20, zorder=1, color='k')

for key, value in arestas.items():
    pontos = [vertices1[value[0]], vertices1[value[1]]]
    x = [pontos[0][0], pontos[1][0]]
    y = [pontos[0][1], pontos[1][1]]
    z = [pontos[0][2], pontos[1][2]]
    ax.plot(x, y, z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title("Cubo")

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)


plt.show()
