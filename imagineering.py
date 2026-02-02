import numpy as np
import matplotlib.pyplot as plt

# Create x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Create grid
X, Y = np.meshgrid(x, y)

# Define surface (write your equation here)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z)

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

