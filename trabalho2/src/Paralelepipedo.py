from trabalho2.src.Cubo import constroi_arestas  # Mesmas arestas que o cubo
from trabalho2.src.Solido import Solido


def constroi_vertices():
    vertices = dict()
    vertices["V1"] = (0, 0, 0)
    vertices["V2"] = (1.5, 0, 0)
    vertices["V3"] = (0, 0, -2.5)
    vertices["V4"] = (0, 5, 0)
    vertices["V5"] = (1.5, 0, -2.5)
    vertices["V6"] = (1.5, 5, 0)
    vertices["V7"] = (0, 5, -2.5)
    vertices["V8"] = (1.5, 5, -2.5)
    return vertices


class Paralelepipedo(Solido):
    """
    Paralelepípedo com lados iguais a 1.5 em x, 5.0 em y e 2.5 em z, com origem em
    um dos vértices pertencentes ao retângulo inferior e aresta paralela ao eixo y
    """

    def __init__(self, titulo: str = "Paralelepipedo"):
        super(Paralelepipedo, self).__init__(constroi_vertices(), constroi_arestas(), titulo)
