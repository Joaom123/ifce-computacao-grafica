from trabalho2.src.Solido import Solido


def constroi_vertices(tamanho_aresta: float):
    vertices = dict()
    vertices["V1"] = [-tamanho_aresta / 2, -tamanho_aresta / 2, 0]
    vertices["V2"] = [tamanho_aresta / 2, -tamanho_aresta / 2, 0]
    vertices["V3"] = [-tamanho_aresta / 2, tamanho_aresta / 2, 0]
    vertices["V4"] = [-tamanho_aresta / 2, -tamanho_aresta / 2, tamanho_aresta]
    vertices["V5"] = [tamanho_aresta / 2, tamanho_aresta / 2, 0]
    vertices["V6"] = [tamanho_aresta / 2, -tamanho_aresta / 2, tamanho_aresta]
    vertices["V7"] = [-tamanho_aresta / 2, tamanho_aresta / 2, tamanho_aresta]
    vertices["V8"] = [tamanho_aresta / 2, tamanho_aresta / 2, tamanho_aresta]
    return vertices


def constroi_arestas():
    arestas = dict()
    arestas["A1"] = ("V1", "V2")
    arestas["A2"] = ("V1", "V3")
    arestas["A3"] = ("V1", "V4")
    arestas["A4"] = ("V2", "V5")
    arestas["A5"] = ("V2", "V6")
    arestas["A6"] = ("V3", "V5")
    arestas["A7"] = ("V3", "V7")
    arestas["A8"] = ("V4", "V6")
    arestas["A9"] = ("V4", "V7")
    arestas["A10"] = ("V5", "V8")
    arestas["A11"] = ("V6", "V8")
    arestas["A12"] = ("V7", "V8")
    return arestas


def constroi_faces():
    faces = dict()
    faces["F1"] = ("V1", "V2", "V5", "V3")
    faces["F2"] = ("V1", "V2", "V6", "V4")
    faces["F3"] = ("V4", "V6", "V8", "V7")
    faces["F4"] = ("V3", "V5", "V8", "V7")
    faces["F5"] = ("V1", "V3", "V7", "V4")
    faces["F6"] = ("V2", "V5", "V8", "V6")
    return faces


class Cubo(Solido):
    """
    Cubo de lado igual a 1.5, com origem no centro do quadrado inferior do
    cubo e aresta do quadrado inferior paralela ao eixo x
    """

    def __init__(self, tamanho_aresta: float = 1.5, titulo: str = "Cubo", cor: str = "b"):
        super().__init__(constroi_vertices(tamanho_aresta), constroi_arestas(), constroi_faces(), titulo, cor)
