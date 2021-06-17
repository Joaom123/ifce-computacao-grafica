class Cubo:
    def __init__(self, tamanho_aresta: float = 1.5):
        self._vertices = dict()
        self._arestas = dict()
        self._faces = dict()

        self.set_vertices(tamanho_aresta)
        self.set_arestas({})
        self.set_faces({})

    @property
    def vertices(self):
        return self._vertices

    @property
    def arestas(self):
        return self._arestas

    @property
    def faces(self):
        return self._faces

    def set_vertices(self, tamanho_aresta: float):
        self._vertices["V1"] = (0, 0, 0)
        self._vertices["V2"] = (tamanho_aresta, 0, 0)
        self._vertices["V3"] = (0, tamanho_aresta, 0)
        self._vertices["V4"] = (0, 0, tamanho_aresta)
        self._vertices["V5"] = (tamanho_aresta, tamanho_aresta, 0)
        self._vertices["V6"] = (tamanho_aresta, 0, tamanho_aresta)
        self._vertices["V7"] = (0, tamanho_aresta, tamanho_aresta)
        self._vertices["V8"] = (tamanho_aresta, tamanho_aresta, tamanho_aresta)

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

    def set_faces(self, faces: dict):
        self._faces["F1"] = ("A1", "A1", "A1", "A1")
        self._faces["F2"] = ("A1", "A1", "A1", "A1")
        self._faces["F3"] = ("A1", "A1", "A1", "A1")
        self._faces["F4"] = ("A1", "A1", "A1", "A1")
        self._faces["F5"] = ("A1", "A1", "A1", "A1")
        self._faces["F6"] = ("A1", "A1", "A1", "A1")
