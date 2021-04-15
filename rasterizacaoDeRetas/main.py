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

"""
Definindo as retas padrões
"""
# Reta A
PONTO_ORIGEM_A = (0, 0)
PONTO_DESTINO_A = (1, 1)

# Reta B
PONTO_ORIGEM_B = (0.2, 0.4)
PONTO_DESTINO_B = (0.6, 0.7)

# Reta C
PONTO_ORIGEM_C = (0.3, 0.9)
PONTO_DESTINO_C = (0.2, 0.3)


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

    # Transformar os pontos da coordenada normalizada na devida resolução
    x_origem = x_origem_normalizado * numero_de_colunas
    y_origem = y_origem_normalizado * numero_de_linhas

    x_destino = x_destino_normalizado * numero_de_colunas
    y_destino = y_destino_normalizado * numero_de_linhas

    # calculo da variação no eixo x e y
    delta_x = x_destino - x_origem
    delta_y = y_destino - y_origem

    # Considerando a equação da reta como y = a*x + b
    coeficiente_angular = 0 if delta_x == 0 else delta_y / delta_x
    coeficiente_linear = y_destino - coeficiente_angular * x_destino

    # Guarda os pixels que devem ser preenchidos
    pixels = list()

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
            x = x if coeficiente_angular == 0 else (y - coeficiente_linear) / coeficiente_angular
            pixels.append(produz_fragmento(x, y))
    return pixels


def produz_matriz(
        array_rasterizacao: List[Tuple[float, float]],
        resolucao: Tuple[int, int]) -> List[List[int]]:
    """
    Cria uma matriz preenchida de zeros e aonde coloca 1 onde há a reta rasterizada.
    :param array_rasterizacao: array com as marcações de pixel da rasterização
    :param resolucao: resolução utilizada na rasterização
    :return: produz uma matrix com as marcações da resterização, a matriz tem o tamanho da resolução
    """
    matriz = [[0 for coluna in range(resolucao[0])] for linha in range(resolucao[1])]

    for pixel in array_rasterizacao:
        coluna = math.floor(pixel[1])
        linha = math.floor(pixel[0])
        matriz[coluna][linha] = 1
    return matriz


def cria_imagem(
        ponto_origem: Tuple[float, float],
        ponto_destino: Tuple[float, float],
        resolucao: Tuple[int, int],
        nome_da_imagem: str) -> None:
    """
    Plota e salva a matriz gerada.
    :param nome_da_imagem: nome da imagem a ser gerada pelo matplotlib
    :param ponto_origem: Entre 0 e 1, representam o ponto de origem da reta
    :param ponto_destino: Entre 0 e 1, representam o ponto de destino da resta
    :param resolucao: Resolucao utilizada
    :return: None
    """
    reta_rasterizada = rasterizacao_reta(ponto_origem, ponto_destino, resolucao)
    matriz = produz_matriz(reta_rasterizada, resolucao)
    
    plt.figure()
    plt.title(nome_da_imagem)    
    img = plt.imshow(matriz, cmap='Greys', origin='lower')
    plt.savefig("rasterizacaoDeRetas/" + nome_da_imagem)
    plt.show()


# Imagens geradas da rasterização da reta A
cria_imagem(PONTO_ORIGEM_A, PONTO_DESTINO_A, RESOLUCAO_25_25, "Reta A na resolução: 25x25")
cria_imagem(PONTO_ORIGEM_A, PONTO_DESTINO_A, RESOLUCAO_50_50, "Reta A na resolução: 50x50")
cria_imagem(PONTO_ORIGEM_A, PONTO_DESTINO_A, RESOLUCAO_150_150, "Reta A na resolução: 150x150")

# Imagens geradas da rasterização da reta A
cria_imagem(PONTO_ORIGEM_B, PONTO_DESTINO_B, RESOLUCAO_25_25, "Reta B na resolução: 25x25")
cria_imagem(PONTO_ORIGEM_B, PONTO_DESTINO_B, RESOLUCAO_50_50, "Reta B na resolução: 50x50")
cria_imagem(PONTO_ORIGEM_B, PONTO_DESTINO_B, RESOLUCAO_150_150, "Reta B na resolução: 150x150")

# Imagens geradas da rasterização da reta A
cria_imagem(PONTO_ORIGEM_C, PONTO_DESTINO_C, RESOLUCAO_25_25, "Reta C na resolução: 25x25")
cria_imagem(PONTO_ORIGEM_C, PONTO_DESTINO_C, RESOLUCAO_50_50, "Reta C na resolução: 50x50")
cria_imagem(PONTO_ORIGEM_C, PONTO_DESTINO_C, RESOLUCAO_150_150, "Reta C na resolução: 150x150")

# Gerando reta vertical e horizontal
cria_imagem((0.25, 0.25), (0.25, 0.5), RESOLUCAO_50_50, "Reta vertical")
cria_imagem((0.25, 0.25), (0.5, 0.25), RESOLUCAO_50_50, "Reta horizontal")
