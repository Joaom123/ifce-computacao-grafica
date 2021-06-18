import math

from trabalho2.Solido import Solido


def constroi_vertices():
    vertices = dict()
    vertices["V1"] = [-math.sqrt(1.3), 0, 2.5]
    vertices["V2"] = [-math.sqrt(3), 0, 0]
    vertices["V3"] = [0, math.sqrt(3), 0]
    vertices["V4"] = [math.sqrt(3), 0, 0]
    vertices["V5"] = [0, -math.sqrt(3), 0]
    vertices["V6"] = [0, -math.sqrt(1.3), 2.5]
    vertices["V7"] = [math.sqrt(1.3), 0, 2.5]
    vertices["V8"] = [0, math.sqrt(1.3), 2.5]
    return vertices


def constroi_arestas():
    arestas = dict()
    arestas["A1"] = ("V1", "V2")
    arestas["A2"] = ("V1", "V6")
    arestas["A3"] = ("V1", "V8")
    arestas["A4"] = ("V3", "V8")
    arestas["A5"] = ("V2", "V3")
    arestas["A6"] = ("V2", "V5")
    arestas["A7"] = ("V3", "V4")
    arestas["A8"] = ("V4", "V5")
    arestas["A9"] = ("V4", "V7")
    arestas["A10"] = ("V5", "V6")
    arestas["A11"] = ("V6", "V7")
    arestas["A12"] = ("V7", "V8")
    return arestas


class TroncoPiramide(Solido):
    """
    Tronco de pirâmide com bases quadradas de lados, respectivamente, iguais a 3.0 e 1.3,
    com altura de 2.5.
    """

    def __init__(self):
        super().__init__(constroi_vertices(), constroi_arestas())
