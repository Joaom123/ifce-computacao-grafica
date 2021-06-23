from dataclasses import dataclass, field

import numpy as np


@dataclass
class Solido:
    vertices: dict = field(default_factory=dict)
    arestas: dict = field(default_factory=dict)
    titulo: str = ""
    cor: str = ""

    def __init__(self, vertices: dict, arestas: dict, titulo: str, cor: str):
        self.vertices = vertices
        self.arestas = arestas
        self.titulo = titulo
        self.cor = cor

    def array_de_vertices(self):
        return np.array(list(self.vertices.values()))

    def matriz_para_vertices(self, matriz: np.array) -> None:
        for i, vertice in enumerate(self.vertices):
            self.vertices[vertice] = matriz[i]

    def multiplicacao_por_matriz(self, matriz: np.array) -> None:
        l = []
        for i, vertice in enumerate(self.vertices):
            l.append([1.0])

        x = np.append(self.array_de_vertices(), l, axis=1)
        m = np.asmatrix(x)
        matriz_transposta = m.transpose()

        for i, vertice in enumerate(self.vertices):
            col = matriz_transposta[:, i]
            nova_col = matriz * col
            matriz_transposta[:, i] = nova_col

        self.matriz_para_vertices(np.array(matriz_transposta.transpose()))

    def adiciona_nos_eixos(self, eixo_x: float = 0, eixo_y: float = 0, eixo_z: float = 0) -> None:
        matriz_vertices = self.array_de_vertices()
        matriz_vertices[:, [0]] = matriz_vertices[:, [0]] + eixo_x
        matriz_vertices[:, [1]] = matriz_vertices[:, [1]] + eixo_y
        matriz_vertices[:, [2]] = matriz_vertices[:, [2]] + eixo_z
        self.matriz_para_vertices(matriz_vertices)
