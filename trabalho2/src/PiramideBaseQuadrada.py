import math

from trabalho2.src.Solido import Solido


def constroi_vertices():
    vertices = dict()
    vertices["V1"] = [0, 0, 3]
    vertices["V2"] = [-math.sqrt(2), 0, 0]
    vertices["V3"] = [0, math.sqrt(2), 0]
    vertices["V4"] = [math.sqrt(2), 0, 0]
    vertices["V5"] = [0, -math.sqrt(2), 0]
    return vertices


def constroi_arestas():
    arestas = dict()
    arestas["A1"] = ("V1", "V2")
    arestas["A2"] = ("V1", "V3")
    arestas["A3"] = ("V1", "V4")
    arestas["A4"] = ("V1", "V5")
    arestas["A5"] = ("V2", "V3")
    arestas["A6"] = ("V2", "V5")
    arestas["A7"] = ("V3", "V4")
    arestas["A8"] = ("V4", "V5")
    return arestas


class PiramideBaseQuadrada(Solido):
    """
    Pirâmide com base quadrada de lado igual a 2.0 e altura igual a 3.0, com
    origem no centro do quadrado da pirâmide e de tal maneira que uma
    aresta do quadrado faça ângulo de 45 graus com o eixo x
    """

    def __init__(self, titulo: str = "Piramide Base Quadrada", cor: str = "r"):
        super().__init__(constroi_vertices(), constroi_arestas(), titulo, cor)
