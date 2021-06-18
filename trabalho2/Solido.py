from dataclasses import dataclass, field
from typing import List
import numpy as np


@dataclass
class Solido:
    vertices: dict = field(default_factory=dict)
    arestas: dict = field(default_factory=dict)

    def __init__(self, vertices: dict, arestas: dict):
        self.vertices = vertices
        self.arestas = arestas

    def converte_vertices_para_matriz(self):
        return np.array(list(self.vertices.values()))

    def matriz_para_vertices(self, matriz: List[List]) -> None:
        for i, vertice in enumerate(self.vertices):
            self.vertices[vertice] = matriz[i]

    def adiciona_matriz(self, numero: float) -> None:
        matriz_vertices = self.converte_vertices_para_matriz()
        matriz_vertices = matriz_vertices + numero
        self.matriz_para_vertices(matriz_vertices)
