import matplotlib.pyplot as plt
import matplotlib.animation
plt.rcParams["animation.html"] = "jshtml"
import numpy as np

# done by
# Damar Zaky 1301164460
# Ki Ageng Satria Pamungkas 1301164422
# Eldio Ruben M. L. 1301164576

v0 = 50
g = 9.8
w = -13
i = 30

fig, ax = plt.subplots()
l, = ax.plot([],[])

xmax = 0
ymax = 0
xmin = 0
ymin = 0
loop = 0
mul = 0.1
ti=0

x1 = []
y1 = []

def toDeg(x):
    return x*np.pi/180

while True:
    t=ti
    x = v0*np.cos(np.deg2rad(i))*t+(0.5*w*(t**2))
    y = ((v0*t)*np.sin(np.deg2rad(i)))-((0.5*g)*(t**2))
    if x>xmax:
        xmax=x
    if y>ymax:
        ymax=y
    if x<xmin:
        xmin=x
    if y<ymin:
        ymin=y
    x1.append(x)
    y1.append(y)
    ti+=mul
    if y>=0:
        loop+=1
    else:
        break   

h = ax.axis([xmin-2,xmax+2,ymin-2,ymax+2])

def animate(i):
    l.set_data(x1[:i], y1[:i])

ani = matplotlib.animation.FuncAnimation(fig, animate, interval=1, frames=loop)
plt.show()