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
from trabalho2.src.Cubo import Cubo
from trabalho2.src.Paralelepipedo import Paralelepipedo
from trabalho2.src.PiramideBaseQuadrada import PiramideBaseQuadrada
from trabalho2.src.PlotaSolido import plota_solidos
from trabalho2.src.TroncoPiramide import TroncoPiramide

cubo = Cubo()
cubo.adiciona_nos_eixos(1, 1, 1)  # Octante I (+, +, +)

piramideBaseQuadrada = PiramideBaseQuadrada()
piramideBaseQuadrada.adiciona_nos_eixos(3.5, 2, 1)  # Octante I (+, +, +)

paralelepipedo = Paralelepipedo()
paralelepipedo.adiciona_nos_eixos(-2, 0.5, 1)  # Octante II (-, +, +)

troncoPiramide = TroncoPiramide()
troncoPiramide.adiciona_nos_eixos(-4, 2, 1)  # Octante II (-, +, +)

solidos = list()
solidos.append(cubo)
solidos.append(piramideBaseQuadrada)
solidos.append(paralelepipedo)
solidos.append(troncoPiramide)

plota_solidos(solidos, titulo="Sólidos no SCM com volume", com_volume=True)
