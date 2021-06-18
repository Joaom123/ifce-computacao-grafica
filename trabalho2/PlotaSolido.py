from matplotlib import pyplot as plt

from trabalho2.Solido import Solido


def plota_solido(solido: Solido, com_arestas=True, com_pontos=False):
    fig = plt.figure(constrained_layout=True)
    ax = fig.add_subplot(111, projection='3d')

    vertices = solido.vertices
    arestas = solido.arestas

    if com_pontos:
        for nome, vertice in vertices.items():
            ax.scatter(vertice[0], vertice[1], vertice[2])
            ax.text(vertice[0], vertice[1], vertice[2], nome, size=12, zorder=1, color='k')

    if com_arestas:
        for key, value in arestas.items():
            pontos = [vertices[value[0]], vertices[value[1]]]
            x = [pontos[0][0], pontos[1][0]]
            y = [pontos[0][1], pontos[1][1]]
            z = [pontos[0][2], pontos[1][2]]
            ax.plot(x, y, z)

    ax.set_title(solido.titulo)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    plt.savefig("images/" + solido.titulo + ".png")
    plt.show()
