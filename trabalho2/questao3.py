"""
3) Escolha um dos octantes sem nenhum sólido e escolha um ponto como origem
para o sistema de coordenadas da câmera.

a. Compute a base vetorial do novo sistema de coordenadas. Para isso,
tenha como base apenas um dos octantes que será considerado como o
volume de visão e use o ponto médio entre os centros de massa de cada
um dos sólidos na derivação de tal base vetorial.

b. Transforme os objetos do sistema de coordenadas do mundo para o sistema de coordenadas da câmera.

c. Apresente os diversos sólidos neste sistema de coordenadas em 3D.
"""
from typing import List

import numpy as np
from numpy import ndarray

from trabalho2.questao2 import cubo, piramideBaseQuadrada, paralelepipedo, troncoPiramide
from trabalho2.src.PlotaSolido import plota_solidos
from trabalho2.src.Solido import Solido


def centro_de_massa_dos_solidos(solidos: List[Solido]) -> ndarray:
    """
    :param solidos: lista de sólidos
    :return: posição do centro de massa dos sólidos da lista como [x, y, z]
    """
    centro_de_massa = np.array([0.0, 0.0, 0.0])  # x, y, z

    for solido in solidos:
        centro_de_massa += np.array(solido.centro_de_massa())
    centro_de_massa /= len(solidos)
    return centro_de_massa


# Sólidos da questão 2
solidos = list()
solidos.append(cubo)
solidos.append(piramideBaseQuadrada)
solidos.append(paralelepipedo)
solidos.append(troncoPiramide)

# ponto médio dos sólidos
cm_solidos = centro_de_massa_dos_solidos(solidos)

# Foi escolhido o octante V (+, +, -)
# Parâmetros Extrínsecos da Câmera
# Ponto de origem, em relação ao SCM, da câmera
origem_camera = np.array([5, 4, -1])
# n, v e u devem ser normalizados
n = (cm_solidos - origem_camera)
n_norm = np.sqrt(sum(n ** 2))

up = np.array([0, 0, 1])  # vetor up, que indica a direção a ser usada como direção vertical da imagem

v = up - (np.dot(up, n) / n_norm ** 2) * n

n = n / n_norm  # normalizando o vetor n
v = v / np.sqrt(sum(v ** 2))  # normalizando o vetor v
# print(np.dot(n, v))  # como v e n devem ser ortogonais, então o produto escalar deve ser próximos de 0

u = np.cross(v, n)  # como v e n estão normalizados, u também está normalizado

# A matriz de translação é obtida como a matriz que leva a posição da câmera p = (xc, yc, zc) para a origem
T = np.matrix([
    [1, 0, 0, -origem_camera[0]],
    [0, 1, 0, -origem_camera[1]],
    [0, 0, 1, -origem_camera[2]],
    [0, 0, 0, 1]
])

# Matriz de rotação do Sistema de Coordenadas do Mundo para o da Câmera
R = np.matrix([
    [u[0], u[1], u[2], 0],
    [v[0], v[1], v[2], 0],
    [n[0], n[1], n[2], 0],
    [0, 0, 0, 1]
])

V = R * T

# Debug - Distância entre o vértice V1 do cubo e a origem da câmera (eye)
primero_vertice_cubo = cubo.vertices["V1"]
print("Tamanho do vetor diferença entre o vértice V1 do cubo e a origem da câmera (eye): {}".format(
    np.linalg.norm(primero_vertice_cubo - origem_camera)))

# Multiplicação dos sólidos pela matriz V, agora todos os sólidos estão no SCC
cubo.multiplicacao_por_matriz(V)
piramideBaseQuadrada.multiplicacao_por_matriz(V)
paralelepipedo.multiplicacao_por_matriz(V)
troncoPiramide.multiplicacao_por_matriz(V)

plota_solidos(solidos, titulo="Sólidos no SCC", tem_volume_visao=True)

# Debug - Distância entre o vértice V1 do cubo e o origem das coordenadas do SCC (0, 0, 0)
primero_vertice_cubo = cubo.vertices["V1"]
print("Tamanho do vetor diferença entre o vértice V1 do cubo e a origem das coordenadas do SCC (0, 0, 0): {}".format(
    np.linalg.norm(primero_vertice_cubo)))

# Debug pra ver a posição dos vetores no espaço
# fig = plt.figure(constrained_layout=True)
# ax = fig.add_subplot(111, projection='3d')
#
# ax.plot([0, u[0]], [0, u[1]], [0, u[2]], color='b', linestyle='dashed')
# ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color='r', linestyle='dashed')
# ax.plot([0, n[0]], [0, n[1]], [0, n[2]], color='g', linestyle='dashed')
# ax.plot([0, up[0]], [0, up[1]], [0, up[2]], color='k', linestyle='dashed')
# ax.set_xlim(-1, 1)
# ax.set_ylim(-1, 1)
# ax.set_zlim(-1, 1)
#
# plt.show()

# Debug mostrando que a origem da câmera agora é [0, 0, 0]
# m_origem = np.matrix([10, 10, -10, 1])
# m_origem = m_origem.transpose()
#
# print(V*m_origem)
