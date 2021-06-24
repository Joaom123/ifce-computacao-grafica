from typing import List

from matplotlib import pyplot as plt

from trabalho2.src.Solido import Solido


def inicia_grafico():
    """
    Inicia o gráfico com apenas um subplot
    :return: Figure e Subplot
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
    :param solido: Solido a ser plotado
    :param ax: Subplot
    :return: None
    """
    for key, value in solido.arestas.items():
        pontos = [solido.vertices[value[0]], solido.vertices[value[1]]]
        x = [pontos[0][0], pontos[1][0]]
        y = [pontos[0][1], pontos[1][1]]
        z = [pontos[0][2], pontos[1][2]]
        ax.plot(x, y, z, color=solido.cor)


def plota_eixos(ax) -> None:
    """
    Plota eixos no subplot
    :param ax: Subplot
    :return: None
    """
    ax.plot([40, -40], [0, 0], [0, 0], color='black', linestyle='dashed')
    ax.plot([0, 0], [40, -40], [0, 0], color='black', linestyle='dashed')
    ax.plot([0, 0], [0, 0], [40, -40], color='black', linestyle='dashed')


def plota_solido(solido: Solido, com_arestas=True, com_pontos=False, com_eixos=True) -> None:
    """
    Plota o sólido em um subplot
    :param solido: O sólido a ser plotado
    :param com_arestas: True, se arestas devem ser plotadas. False caso contrário.
    :param com_pontos: True, se vertices devem ser plotadas. False caso contrário.
    :param com_eixos: True, se eixos devem ser plotadas. False caso contrário.
    :return: None
    """
    fig, ax = inicia_grafico()

    if com_pontos:
        plota_pontos(solido, ax)

    if com_arestas:
        plota_arestas(solido, ax)

    if com_eixos:
        plota_eixos(ax)

    ax.set_title(solido.titulo)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)

    plt.savefig("images/" + solido.titulo + ".png")
    plt.show()


def plota_solidos(solidos: List[Solido], com_arestas=True, com_pontos=False, com_eixos=True,
                  titulo: str = "image", *args) -> None:
    """
    Recebe uma lista de sólidos e os plota em um mesmo gráfico 3D
    :param solidos: Lista de sólidos a serem plotados
    :param com_arestas: True, se arestas devem ser plotadas. False caso contrário.
    :param com_pontos: True, se vertices devem ser plotadas. False caso contrário.
    :param com_eixos: True, se eixos devem ser plotadas. False caso contrário.
    :param titulo: Nome do arquivo e legenda
    :return: None
    """
    fig, ax = inicia_grafico()

    for solido in solidos:
        if com_pontos:
            plota_pontos(solido, ax)

        if com_arestas:
            plota_arestas(solido, ax)

    if com_eixos:
        plota_eixos(ax)

    ax.set_title(titulo)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_zlim(-15, 15)

    plt.savefig("images/" + titulo + ".png")
    plt.show()
