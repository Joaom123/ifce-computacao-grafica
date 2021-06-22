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
import numpy as np

# Foi escolhido o octante V (+, +, -)
from trabalho2.questao2 import cubo, piramideBaseQuadrada, paralelepipedo, troncoPiramide
from trabalho2.src.PlotaSolido import plota_solidos

origem_camera = [3, 3, -2]

u = [1, 0, 0]
v = [1, 1, 0]
n = [0, 1, 1]

T = [
    [1, 0, 0, -origem_camera[0]],
    [0, 1, 0, -origem_camera[1]],
    [0, 0, 1, -origem_camera[2]],
    [0, 0, 0, 1]
]

R = [
    [u[0], u[1], u[2], 0],
    [v[0], v[1], v[2], 0],
    [n[0], n[1], n[2], 0],
    [0, 0, 0, 1]
]

V = np.matrix(T) * np.matrix(R)

cubo.multiplicacao_por_matriz(V)
piramideBaseQuadrada.multiplicacao_por_matriz(V)
paralelepipedo.multiplicacao_por_matriz(V)
troncoPiramide.multiplicacao_por_matriz(V)

solidos = list()
solidos.append(cubo)
solidos.append(piramideBaseQuadrada)
solidos.append(paralelepipedo)
solidos.append(troncoPiramide)

plota_solidos(solidos, titulo="visaoCamera")
