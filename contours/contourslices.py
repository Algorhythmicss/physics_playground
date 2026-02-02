import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)

Z = X**2 - Y**2  # the graph you want

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.3)

# Contour projection on bottom
ax.contour(X, Y, Z, zdir='z', offset=-30)

ax.set_zlim(-30, 30)

plt.show()

# So anything you can write as a function of x and y in math, you can write with X and Y in NumPy(np).
#Math.                                      # Code
# sin x                                     np.sin(X)
# cos y                                     np.cos(Y)
# xy                                        X * Y
# x/y                                       X / Y
# |x|                                       np.abs(X)
# e^{-(x^2+y^2)}                            np.exp(-(X**2 + Y**2))

#coolfuntions.txt (as the name suggests) contains cool functions that open a doorway to real physics(not toy functions rather physically represent something)
