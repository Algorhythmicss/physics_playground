import numpy as np
import matplotlib.pyplot as plt

# Create grid
x, y, z = np.meshgrid(
    np.linspace(-2, 2, 6),
    np.linspace(-2, 2, 6),
    np.linspace(-2, 2, 6)
)

# Define vector field F = (Fx, Fy, Fz)[fun part!!]
Fx = -y
Fy = x
Fz = np.zeros_like(z)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.quiver(x, y, z, Fx, Fy, Fz, length=0.4)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

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

