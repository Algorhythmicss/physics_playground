import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def update(frame):
    ax.clear()
    R = np.sqrt( np.sin(X - frame/10) * np.cos(Y - frame/15))  #input function(can change), if confused then read from line 50.
    Z = np.sin(3*R - frame/4)    # evolving (radial ripples pattern) , you can look for other patterns starting from line 23 .
    ax.plot_surface(X, Y, Z)
    ax.set_zlim(-1, 1)

ani = FuncAnimation(fig, update, frames=50, interval=100)

plt.show()


#1.radial ripples (pond drop, perfectly symmetric)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(3*R - frame/4)

# 2.Traveling plane wave (clean directional motion, Feels like wind sweeping across a field.)
# Z = np.sin(2*X + 1.5*Y - frame/3)

# 3.Interference pattern (two sources colliding)
# R1 = np.sqrt((X-2)**2 + (Y-2)**2)
# R2 = np.sqrt((X+2)**2 + (Y+2)**2)
# Z = np.sin(3*R1 - frame/4) + np.sin(3*R2 - frame/4)

# 4. Breathing Gaussian hill (pulsating blob)
# Z = np.exp(-(X**2 + Y**2)) * np.sin(frame/5)

# 5. Swirl / vortex feel
# theta = np.arctan2(Y, X)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(4*theta + R - frame/4)

# 6. Checkerboard standing waves (lattice vibes,Nodes and antinodes dancing in place.)
# Z = np.sin(2*X) * np.sin(2*Y) * np.cos(frame/5)

# if this feels too much
# You are plotting:

# Z = f(X, Y, t)

# where t = frame.

# So anything you can write as a function of x and y in math, you can write with X and Y in NumPy(np).
#Math.                                      # Code
# sin x                                     np.sin(X)
# cos y                                     np.cos(Y)
# xy                                        X * Y
# x/y                                       X / Y
# |x|                                       np.abs(X)
# e^{-(x^2+y^2)}                            np.exp(-(X**2 + Y**2))

#coolfuntions.txt (as the name suggests) contains cool functions that open a doorway to real physics(not toy functions rather physically represent something)
