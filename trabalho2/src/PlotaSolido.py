from typing import List

from matplotlib import pyplot as plt

from trabalho2.src.Solido import Solido


def inicia_grafico():
    """
    Inicia o gráfico com apenas um subplot
    :return:
    """
    fig = plt.figure(constrained_layout=True)
    ax = fig.add_subplot(111, projection='3d')
    return fig, ax


def plota_pontos(solido: Solido, ax) -> None:
    """
    Plota os pontos de um sólido, com texto, em um subplot
    :param solido: sólido a ser plotado
    :param ax: subplot
    :return: None
    """
    for nome, vertice in solido.vertices.items():
        ax.scatter(vertice[0], vertice[1], vertice[2])
        ax.text(vertice[0], vertice[1], vertice[2], nome, size=12, zorder=1, color='k')


def plota_arestas(solido: Solido, ax) -> None:
    """
    Plota os arestas de um sólido em um subplot
    :param solido:
    :param ax:
    :return: None
    """
    for key, value in solido.arestas.items():
        pontos = [solido.vertices[value[0]], solido.vertices[value[1]]]
        x = [pontos[0][0], pontos[1][0]]
        y = [pontos[0][1], pontos[1][1]]
        z = [pontos[0][2], pontos[1][2]]
        ax.plot(x, y, z, color=solido.cor)


def plota_solido(solido: Solido, com_arestas=True, com_pontos=False) -> None:
    """

    :param solido:
    :param com_arestas:
    :param com_pontos:
    :return:
    """
    fig, ax = inicia_grafico()

    if com_pontos:
        plota_pontos(solido, ax)

    if com_arestas:
        plota_arestas(solido, ax)

    ax.set_title(solido.titulo)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    plt.savefig("images/" + solido.titulo + ".png")
    plt.show()


def plota_solidos(solidos: List[Solido], com_arestas=True, com_pontos=False, titulo: str = "image") -> None:
    """

    :param solidos:
    :param com_arestas:
    :param com_pontos:
    :param titulo:
    :return:
    """
    fig, ax = inicia_grafico()

    for solido in solidos:
        if com_pontos:
            plota_pontos(solido, ax)

        if com_arestas:
            plota_arestas(solido, ax)

    ax.plot([40, -40], [0, 0], [0, 0], color='black', linestyle='dashed')
    ax.plot([0, 0], [40, -40], [0, 0], color='black', linestyle='dashed')
    ax.plot([0, 0], [0, 0], [40, -40], color='black', linestyle='dashed')

    ax.set_title(titulo)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_zlim(-15, 15)
    plt.savefig("images/" + titulo + ".png")
    plt.show()
