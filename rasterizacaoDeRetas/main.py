import math
import matplotlib.pyplot as plt
from typing import List, Tuple

"""
Definindo as resoluções padrões
"""
RESOLUCAO_40_30 = (40, 30)
RESOLUCAO_80_60 = (80, 60)
RESOLUCAO_QVGA = (320, 240)

"""
Definindo as retas padrões
"""
# Reta A
PONTO_ORIGEM_A = (0.2, 0.3)
PONTO_DESTINO_A = (0.9, 0.5)

# Reta B
PONTO_ORIGEM_B = (0.3, 0.2)
PONTO_DESTINO_B = (0.5, 0.9)

# Reta C
PONTO_ORIGEM_C = (0.3, 0.9)
PONTO_DESTINO_C = (0.2, 0.3)

# Reta D - Horizontal
PONTO_ORIGEM_D = (0.25, 0.25)
PONTO_DESTINO_D = (0.75, 0.25)

# Reta E - Vertical
PONTO_ORIGEM_E = (0.25, 0.25)
PONTO_DESTINO_E = (0.25, 0.75)

# Reta F - Quase Horizontal
PONTO_ORIGEM_F = (0.25, 0.25)
PONTO_DESTINO_F = (0.75, 0.24)

# Reta G - Quase Vertical
PONTO_ORIGEM_G = (0.25, 0.25)
PONTO_DESTINO_G = (0.24, 0.75)


def produz_fragmento(x: float, y: float) -> (float, float):
    """
    Dados um ponto (x, y), retorna o centro do pixel que tal ponto ocupa
    :param x: componente x do ponto
    :param y: componente y do ponto
    :return x_pixel, y_pixel: Posição do centro do pixel
    """
    x_pixel = math.floor(x) + 0.5
    y_pixel = math.floor(y) + 0.5
    
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

    # Transformar os pontos na coordenada normalizada na devida resolução
    x_origem = x_origem_normalizado * numero_de_colunas
    y_origem = y_origem_normalizado * numero_de_linhas

    x_destino = x_destino_normalizado * numero_de_colunas
    y_destino = y_destino_normalizado * numero_de_linhas

    # Calculo da variação no eixo x e y
    delta_x = x_destino - x_origem
    delta_y = y_destino - y_origem

    # Considerando a equação da reta como y = a*x + b, quando delta_x for 0, o coeficiente angular
    # torna-se indefinido
    coeficiente_angular = None
    coeficiente_linear = None

    if delta_x != 0:
        coeficiente_angular = delta_y / delta_x
        coeficiente_linear = y_destino - coeficiente_angular * x_destino

    # Guarda os pixels que devem ser preenchidos
    pixels = list()

    # x e y serão usados durante a iteração
    x = x_origem
    y = y_origem

    # Guarda o primeiro pixel da reta rasterizada
    pixels.append(produz_fragmento(x, y))

    # Caso a variação no eixo x seja maior do que a variação no eixo y,
    # o algoritmo irá iterar x até passar do x_destino, y é calculado pela equação da reta.
    # Caso contrário, a iteração ocorre no eixo y.
    if abs(delta_x) > abs(delta_y):
        # Caso a x_origem seja maior, vamos trocá-la pelo x_destino
        if x_origem > x_destino:
            x = x_destino
            x_origem, x_destino = x_destino, x_origem
        while x < x_destino:
            x = x + 1
            if x >= x_destino:
                return pixels
            y = coeficiente_angular * x + coeficiente_linear
            pixels.append(produz_fragmento(x, y))
    else:
        # Caso a y_origem seja maior, vamos trocá-la pelo y_destino
        if y_origem > y_destino:
            y = y_destino
            y_origem, y_destino = y_destino, y_origem
        while y < y_destino:
            y = y + 1
            if y >= y_destino:
                return pixels
            # x é atualizado apenas quando delta_x difere de 0
            if delta_x != 0:
                x = (y - coeficiente_linear) / coeficiente_angular
            pixels.append(produz_fragmento(x, y))
    return pixels


def produz_matriz(
        array_rasterizacao: List[Tuple[float, float]],
        resolucao: Tuple[int, int]) -> List[List[int]]:
    """
    Cria uma matriz preenchida de zeros e aonde coloca 1 onde há a reta rasterizada.
    :param array_rasterizacao: array com as marcações de pixel da rasterização
    :param resolucao: resolução utilizada na rasterização
    :return: produz uma matrix com as marcações da reta rasterizada, a matriz tem o tamanho da resolução
    """
    matriz = [[0 for coluna in range(resolucao[0])] for linha in range(resolucao[1])]

    # Devemos marcar na matriz os pontos existentes no array rasterização
    for pixel in array_rasterizacao:
        linha = math.floor(pixel[0])
        coluna = math.floor(pixel[1])
        matriz[coluna][linha] = 1
    return matriz


def cria_imagem(
        ponto_origem: Tuple[float, float],
        ponto_destino: Tuple[float, float],
        resolucao: Tuple[int, int],
        nome_da_imagem: str) -> None:
    """
    Plota e grava a matriz gerada.
    :param ponto_origem: Entre 0 e 1, representam o ponto de origem da reta
    :param ponto_destino: Entre 0 e 1, representam o ponto de destino da resta
    :param resolucao: Resolução utilizada
    :param nome_da_imagem: nome da imagem a ser gerada pelo matplotlib
    :return: None
    """
    reta_rasterizada = rasterizacao_reta(ponto_origem, ponto_destino, resolucao)
    matriz = produz_matriz(reta_rasterizada, resolucao)
    
    plt.figure()
    plt.title(nome_da_imagem)    
    img = plt.imshow(matriz, cmap='Greys', origin='lower')
    plt.savefig(nome_da_imagem)
    plt.show()


# Imagens geradas da rasterização da reta A
cria_imagem(PONTO_ORIGEM_A, PONTO_DESTINO_A, RESOLUCAO_40_30, "Reta A na resolução: 40x30")
cria_imagem(PONTO_ORIGEM_A, PONTO_DESTINO_A, RESOLUCAO_80_60, "Reta A na resolução: 80x60")
cria_imagem(PONTO_ORIGEM_A, PONTO_DESTINO_A, RESOLUCAO_QVGA, "Reta A na resolução: 320x240 (QVGA)")

# Imagens geradas da rasterização da reta B
cria_imagem(PONTO_ORIGEM_B, PONTO_DESTINO_B, RESOLUCAO_40_30, "Reta B na resolução: 40x30")
cria_imagem(PONTO_ORIGEM_B, PONTO_DESTINO_B, RESOLUCAO_80_60, "Reta B na resolução: 80x60")
cria_imagem(PONTO_ORIGEM_B, PONTO_DESTINO_B, RESOLUCAO_QVGA, "Reta B na resolução: 320x240 (QVGA)")

# Imagens geradas da rasterização da reta C
cria_imagem(PONTO_ORIGEM_C, PONTO_DESTINO_C, RESOLUCAO_40_30, "Reta C na resolução: 40x30")
cria_imagem(PONTO_ORIGEM_C, PONTO_DESTINO_C, RESOLUCAO_80_60, "Reta C na resolução: 80x60")
cria_imagem(PONTO_ORIGEM_C, PONTO_DESTINO_C, RESOLUCAO_QVGA, "Reta C na resolução: 320x240 (QVGA)")

# Gerando Reta D - Horizontal
cria_imagem(PONTO_ORIGEM_D, PONTO_DESTINO_D, RESOLUCAO_40_30, "Reta D na resolução: 40x30")
cria_imagem(PONTO_ORIGEM_D, PONTO_DESTINO_D, RESOLUCAO_80_60, "Reta D na resolução: 80x60")
cria_imagem(PONTO_ORIGEM_D, PONTO_DESTINO_D, RESOLUCAO_QVGA, "Reta D na resolução: 320x240 (QVGA)")

# Gerando Reta E - Vertical
cria_imagem(PONTO_ORIGEM_E, PONTO_DESTINO_E, RESOLUCAO_40_30, "Reta E na resolução: 40x30")
cria_imagem(PONTO_ORIGEM_E, PONTO_DESTINO_E, RESOLUCAO_80_60, "Reta E na resolução: 80x60")
cria_imagem(PONTO_ORIGEM_E, PONTO_DESTINO_E, RESOLUCAO_QVGA, "Reta E Na resolução: 320x240 (QVGA)")

# Gerando Reta F
cria_imagem(PONTO_ORIGEM_F, PONTO_DESTINO_F, RESOLUCAO_40_30, "Reta F na resolução: 40x30")
cria_imagem(PONTO_ORIGEM_F, PONTO_DESTINO_F, RESOLUCAO_80_60, "Reta F na resolução: 80x60")
cria_imagem(PONTO_ORIGEM_F, PONTO_DESTINO_F, RESOLUCAO_QVGA, "Reta F Na resolução: 320x240 (QVGA)")

# Gerando Reta G
cria_imagem(PONTO_ORIGEM_G, PONTO_DESTINO_G, RESOLUCAO_40_30, "Reta G na resolução: 40x30")
cria_imagem(PONTO_ORIGEM_G, PONTO_DESTINO_G, RESOLUCAO_80_60, "Reta G na resolução: 80x60")
cria_imagem(PONTO_ORIGEM_G, PONTO_DESTINO_G, RESOLUCAO_QVGA, "Reta G Na resolução: 320x240 (QVGA)")
