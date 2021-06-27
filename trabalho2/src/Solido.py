from dataclasses import dataclass, field
from typing import List

import numpy as np
from numpy import ndarray


@dataclass
class Solido:
    vertices: dict = field(default_factory=dict)
    arestas: dict = field(default_factory=dict)
    faces: dict = field(default_factory=dict)
    titulo: str = ""
    cor: str = ""

    def __init__(self, vertices: dict, arestas: dict, faces: dict, titulo: str, cor: str):
        self.vertices = vertices
        self.arestas = arestas
        self.titulo = titulo
        self.faces = faces
        self.cor = cor

    def array_de_vertices(self) -> ndarray:
        """
        :return: Array contendo cada vértice como [x, y, z]
        """
        return np.array(list(self.vertices.values()))

    def matriz_para_vertices(self, array_vertice: ndarray) -> None:
        """
        Recebe um array contendo vértices [x, y, z] e substitui os vértices do sólidos pelos do array.
        :param array_vertice: Array de vertices [x, y, z]
        :return: None
        """
        for i, vertice in enumerate(self.vertices):
            self.vertices[vertice] = array_vertice[i]

    def multiplicacao_por_matriz(self, matriz: np.matrix) -> None:
        """
        Para cada vértice V [x, y, z] do sólido, o colocamos em sua forma homogênea [x, y, z, 1]. Seja M uma matriz,
        multiplicamos cada vértice pela matriz M * V1, sendo V1 um vértice do sólido em sua forma homogênea.
        :param matriz: Matriz a ser multiplicada
        :return: None
        """
        uns = [[1.0]] * len(self.vertices)  # array de uns [1.0, 1.0, ...]
        x = np.append(self.array_de_vertices(), uns, axis=1)
        matriz_vertices_homogenea = np.asmatrix(x)
        matriz_transposta_vertices = matriz_vertices_homogenea.transpose()

        # Multiplicação da matriz pra cada vértice
        for i, vertice in enumerate(self.vertices):
            col = matriz_transposta_vertices[:, i]
            nova_col = matriz * col
            matriz_transposta_vertices[:, i] = nova_col

        matriz_transposta_vertices = np.delete(matriz_transposta_vertices, -1, 0)  # Remove a linha de uns
        self.matriz_para_vertices(np.array(matriz_transposta_vertices.transpose()))

    def adiciona_nos_eixos(self, eixo_x: float = 0, eixo_y: float = 0, eixo_z: float = 0) -> None:
        """
        Equivalente de utilizar uma matriz de translação. Recebe-se o valor dos eixos x, y e z e adiciona-os
        nos seus respectivos eixos.
        :param eixo_x: Valor a adicionar no eixo x
        :param eixo_y: Valor a adicionar no eixo y
        :param eixo_z: Valor a adicionar no eixo z
        :return: None
        """
        matriz_vertices = self.array_de_vertices()
        matriz_vertices[:, [0]] = matriz_vertices[:, [0]] + eixo_x
        matriz_vertices[:, [1]] = matriz_vertices[:, [1]] + eixo_y
        matriz_vertices[:, [2]] = matriz_vertices[:, [2]] + eixo_z
        self.matriz_para_vertices(matriz_vertices)

    def centro_de_massa(self) -> List:
        """
        Retorna o ponto do centro de massa do sólido. Utilizamos a média do pontos no eixo x, y e z. Isso é válido,
        pois consideramos o sólido homogêneo.
        :return: [cm_x, cm_y, cm_z] que são as coordenadas do centro de massa
        """
        matriz_vertices = self.array_de_vertices()
        media_x = np.median(matriz_vertices[:, [0]])
        media_y = np.median(matriz_vertices[:, [1]])
        media_z = np.median(matriz_vertices[:, [2]])

        return [media_x, media_y, media_z]

    def vertice_faces(self) -> ndarray:
        vertices_faces = []
        for face, vertices_da_face in self.faces.items():
            vertices = []
            for vertice in vertices_da_face:
                vertices.append(self.vertices[vertice])
            vertices_faces.append(vertices)
        return np.array(vertices_faces)
