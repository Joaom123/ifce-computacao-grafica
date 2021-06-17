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
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

plt.show()
