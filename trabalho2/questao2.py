"""
2) Componha uma cena contendo os diversos sólidos modelados anteriormente
em um sistema de coordenadas do mundo, de tal maneira a não haver
sobreposição ou intersecção entre tais objetos.

a. O cubo e a pirâmide devem estar localizados em apenas um octante do
espaço, bem como o paralelepípedo e o tronco devem estar em apenas
um octante. Além disso, pelo menos dois octantes adjacentes devem
possuir sólidos.

b. O maior valor possível para cada uma das componentes de um vértice é 6.
Se necessário aplique transformações de escala para que os sólidos
sejam localizados respeitando tais limites.

c. Apresente os diversos sólidos neste sistema de coordenadas em 3D.
"""
from trabalho2.Cubo import Cubo
from trabalho2.Paralelepipedo import Paralelepipedo
from trabalho2.PiramideBaseQuadrada import PiramideBaseQuadrada
from trabalho2.PlotaSolido import plota_solidos
from trabalho2.TroncoPiramide import TroncoPiramide


cubo = Cubo()
cubo.adiciona_nos_eixos(10, 10, 10)

piramideBaseQuadrada = PiramideBaseQuadrada()
piramideBaseQuadrada.adiciona_nos_eixos(-10, 10, 0)

paralelepipedo = Paralelepipedo()
paralelepipedo.adiciona_nos_eixos(10, -10, 10)


troncoPiramide = TroncoPiramide()
troncoPiramide.adiciona_nos_eixos(-10, -10, -10)

solidos = list()
solidos.append(cubo)
solidos.append(paralelepipedo)
solidos.append(piramideBaseQuadrada)
solidos.append(troncoPiramide)

plota_solidos(solidos, titulo="cena3D")
