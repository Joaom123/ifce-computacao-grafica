import math
import matplotlib.pyplot as plt
from typing import List, Tuple

"""
Definindo as resoluções padrões
"""
RESOLUCAO_TESTE = (9, 9)
RESOLUCAO_25_25 = (25, 25)
RESOLUCAO_50_50 = (50, 50)
RESOLUCAO_150_150 = (150, 150)

# Reta A
PONTO_ORIGEM_A = (0, 0)
PONTO_DESTINO_A = (1, 1)
# Reta B
PONTO_ORIGEM_B = (0.25, 0.25)
PONTO_DESTINO_B = (0.75, 0.75)
# Reta C
PONTO_ORIGEM_C = (0.3, 0.4)
PONTO_DESTINO_C = (0.2, 0.3)


def produz_fragmento(x: float, y: float) -> (float, float):
    """
    Dados um ponto (x, y), retorna o centro do pixel que tal ponto ocupa
    :param x: componente x do ponto
    :param y: componente y do ponto
    :return x_pixel, y_pixel: Posição do centro do pixel
    """
    x_chao = math.floor(x)
    y_chao = math.floor(y)
    x_pixel = x_chao + 0.5
    y_pixel = y_chao + 0.5
    return x_pixel, y_pixel


def rasterizacao_reta(
        ponto_origem: Tuple[float, float],
        ponto_destino: Tuple[float, float],
        resolucao: (int, int)) -> List[Tuple[float, float]]:
    """
    Algoritmo de rasterização de retas
    :param ponto_origem: Entre 0 e 1, representam o ponto de origem da reta
    :param ponto_destino: Entre 0 e 1, representam o ponto de destino da resta
    :param resolucao: Resolucao utilizada
    :return: array com a rasterização entre os pontos
    """
    numero_de_colunas = resolucao[0]
    numero_de_linhas = resolucao[1]

    x_origem_normalizado = ponto_origem[0]
    y_origem_normalizado = ponto_origem[1]

    x_destino_normalizado = ponto_destino[0]
    y_destino_normalizado = ponto_destino[1]

    x_origem = x_origem_normalizado * numero_de_colunas
    y_origem = y_origem_normalizado * numero_de_linhas

    x_destino = x_destino_normalizado * numero_de_colunas
    y_destino = y_destino_normalizado * numero_de_linhas

    delta_x = x_destino - x_origem
    delta_y = y_destino - y_origem

    coeficiente_angular = 0 if delta_x == 0 else delta_y / delta_x
    coeficiente_linear = y_destino - coeficiente_angular * x_destino

    lista_dos_pixels = list()

    x = x_origem
    y = y_origem

    lista_dos_pixels.append(produz_fragmento(x, y))

    if abs(delta_x) > abs(delta_y):
        while x < x_destino:
            x = x + 1
            if x >= x_destino:
                return lista_dos_pixels
            y = coeficiente_angular * x + coeficiente_linear
            lista_dos_pixels.append(produz_fragmento(x, y))
    else:
        while y < y_destino:
            y = y + 1
            if y >= y_destino:
                return lista_dos_pixels
            x = x if coeficiente_angular == 0 else (y - coeficiente_linear) / coeficiente_angular
            lista_dos_pixels.append(produz_fragmento(x, y))
    return lista_dos_pixels


def produz_matriz(array_rasterizacao: List[Tuple[float, float]], resolucao: Tuple[int, int]) -> List[List[int]]:
    """

    :param array_rasterizacao: array com as marcações de pixel da rasterização
    :param resolucao: resolução utilizada na rasterização
    :return: produz uma matrix com as marcações da resterização, a matriz tem o tamanho da resolução
    """
    matriz = [[0 for _ in range(resolucao[0])] for _ in range(resolucao[1])]

    for pixel in array_rasterizacao:
        coluna = math.floor(pixel[1])
        linha = math.floor(pixel[0])
        matriz[coluna][linha] = 1
    return matriz


def cria_imagem(ponto_origem, ponto_destino, resolucao, nome_da_imagem) -> None:
    """

    :param nome_da_imagem: nome da imagem a ser gerada pelo matplotlib
    :param ponto_origem:
    :param ponto_destino:
    :param resolucao:
    :return:
    """
    plt.figure()
    linha_reso_1 = rasterizacao_reta(ponto_origem, ponto_destino, resolucao)
    matriz = produz_matriz(linha_reso_1, resolucao)
    img = plt.imshow(matriz, cmap='Greys', origin='lower')
    plt.savefig(nome_da_imagem)
    plt.show()


# Imagens geradas da rasterização da reta A
cria_imagem(PONTO_ORIGEM_A, PONTO_DESTINO_A, RESOLUCAO_25_25, "Ponto A na resolução: 25x25")
cria_imagem(PONTO_ORIGEM_A, PONTO_DESTINO_A, RESOLUCAO_50_50, "Ponto A na resolução: 50x50")
cria_imagem(PONTO_ORIGEM_A, PONTO_DESTINO_A, RESOLUCAO_150_150, "Ponto A na resolução: 150x150")

# Imagens geradas da rasterização da reta A
cria_imagem(PONTO_ORIGEM_B, PONTO_DESTINO_B, RESOLUCAO_25_25, "Ponto B na resolução: 25x25")
cria_imagem(PONTO_ORIGEM_B, PONTO_DESTINO_B, RESOLUCAO_50_50, "Ponto B na resolução: 50x50")
cria_imagem(PONTO_ORIGEM_B, PONTO_DESTINO_B, RESOLUCAO_150_150, "Ponto B na resolução: 150x150")

# Imagens geradas da rasterização da reta A
cria_imagem(PONTO_ORIGEM_C, PONTO_DESTINO_C, RESOLUCAO_25_25, "Ponto C na resolução: 25x25")
cria_imagem(PONTO_ORIGEM_C, PONTO_DESTINO_C, RESOLUCAO_50_50, "Ponto C na resolução: 50x50")
cria_imagem(PONTO_ORIGEM_C, PONTO_DESTINO_C, RESOLUCAO_150_150, "Ponto C na resolução: 150x150")

# Gerando reta vertical e horizontal
cria_imagem((0.25, 0.25), (0.25, 0.5), RESOLUCAO_50_50, "Reta vertical")
cria_imagem((0.25, 0.25), (0.5, 0.25), RESOLUCAO_50_50, "Reta horizontal")
