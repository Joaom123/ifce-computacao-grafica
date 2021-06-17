class Paralelepipedo:
    """
    Paralelepípedo com lados iguais a 1.5 em x, 5.0 em y e 2.5 em z, com origem em
    um dos vértices pertencentes ao retângulo inferior e aresta paralela ao eixo y;
    """
    def __init__(self):
        self._vertices = dict()
        self._arestas = dict()

        self.set_vertices()
        self.set_arestas({})

    @property
    def vertices(self):
        return self._vertices

    @property
    def arestas(self):
        return self._arestas

    def set_vertices(self):
        self._vertices["V1"] = (0, 0, 0)
        self._vertices["V2"] = (1.5, 0, 0)
        self._vertices["V3"] = (0, 5.0, 0)
        self._vertices["V4"] = (0, 0, 2.5)
        self._vertices["V5"] = (1.5, 5.0, 0)
        self._vertices["V6"] = (1.5, 0, 2.5)
        self._vertices["V7"] = (0, 5.0, 2.5)
        self._vertices["V8"] = (1.5, 5.0, 2.5)

    def set_arestas(self, arestas: dict):
        self._arestas["A1"] = ("V1", "V2")
        self._arestas["A2"] = ("V1", "V3")
        self._arestas["A3"] = ("V1", "V4")
        self._arestas["A4"] = ("V2", "V5")
        self._arestas["A5"] = ("V2", "V6")
        self._arestas["A6"] = ("V3", "V5")
        self._arestas["A7"] = ("V3", "V7")
        self._arestas["A8"] = ("V4", "V6")
        self._arestas["A9"] = ("V4", "V7")
        self._arestas["A10"] = ("V5", "V8")
        self._arestas["A11"] = ("V6", "V8")
        self._arestas["A12"] = ("V7", "V8")
