"""
4) Faça uma transformação de projeção paralela ortogonal dos sólidos contidos no
volume de visão e, para isto, projete as arestas dos sólidos em 2 dimensões. Cada
sólido deve conter arestas com mesma cor, mas sólidos diferentes devem ter
cores diferentes.

a. Apresente tais objetos em 2D.
"""
import numpy as np
from matplotlib import pyplot as plt

from trabalho2.questao3 import solidos

# Matriz de projeção paralela ortogonal nos eixos x e y.
P = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
])

if __name__ == '__main__':
    # Aplicando a transformação nos sólidos
    for solido in solidos:
        solido.multiplicacao_por_matriz(P)

    # Plotando o gráfico 2D
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title("Projeção nos eixos x e y dos sólidos")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    # ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 0)
    for solido in solidos:
        # Plotando vértices
        # for nome, vertice in solido.vertices.items():
        #     ax.scatter(vertice[0], vertice[1])
        #     ax.text(vertice[0], vertice[1], nome, size=12, zorder=1, color='k')
        # Plotando arestas
        for key, value in solido.arestas.items():
            pontos = [solido.vertices[value[0]], solido.vertices[value[1]]]
            x = [pontos[0][0], pontos[1][0]]
            y = [pontos[0][1], pontos[1][1]]
            ax.plot(x, y, color=solido.cor)

    plt.savefig("images/" + "projecao2D.png")
    plt.show()
