
# coding: utf-8

# In[7]:


from matplotlib import pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'notebook')
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation


# get_ipython().run_line_magic('matplotlib', 'notebook')
# import matplotlib.pyplot as plt
# import matplotlib.animation
plt.rcParams["animation.html"] = "jshtml"
# import numpy as np
# from matplotlib.lines import Line2D

dims = 3
step_n = 100
loop=step_n+2

step_set=list(range(26))

origin = [[0,0,100]]
# print(origin)
step_shape = step_n
steps = np.random.choice(a=step_set, size=step_shape)#,p=[0.2, 0.09, 0.01, 0.15,0.02, 0.02,0.17 ,0.34])#probability

print(steps)

def coor(ar):
#     dic=[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]] #x,y: E, NE, N, NW, W, SW, S, SE
    dic=[[1,1,1],[1,1,0],[1,1,-1],[1,0,1],[1,0,0],[1,0,-1],[1,-1,1],
    [1,-1,0],[1,-1,-1],[0,1,1],[0,1,0],[0,1,-1],[0,0,1],[0,0,-1],
    [0,-1,1],[0,-1,0],[0,-1,-1],[-1,1,1],[-1,1,0],[-1,1,-1],
    [-1,0,1],[-1,0,0],[-1,0,-1],[-1,-1,1],[-1,-1,0],[-1,-1,-1]]
    nr = []
    for k in ar:
        nr.append(dic[k])
    return nr
stepss=coor(steps)
print(stepss)


path = np.concatenate([origin, stepss]).cumsum(0)

# print(path)

x = np.arange(step_n+1)
x=x.tolist()
pathe=path.tolist()
start = path[:1]
stop = path[-1:]

# print(path)
# print(stop)




fig = plt.figure()
ax = p3.Axes3D(fig)


ax.grid(False)
ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# ax.scatter3D(path[:,0], path[:,1], path[:,2], 
#              c='blue', alpha=0.25,s=1)
# ax.plot3D(path[:,0], path[:,1], path[:,2], 
#           c='blue', alpha=0.5, lw=0.5)
ax.plot3D(start[:,0], start[:,1], start[:,2], 
          c='red', marker='+')
ax.plot3D(stop[:,0], stop[:,1], stop[:,2], 
          c='black', marker='o')

l, = ax.plot([],[],[]) #,c='blue',alpha=0.5,lw=0.25,ls='solid'



# h = ax.axis([min(path[:,0])-5,max(path[:,0])+5,min(path[:,1])-5,max(path[:,1])+5,min(path[:,2])-5,max(path[:,2])+5])
ax.set_xlim3d(min(path[:,0])-5,max(path[:,0])+5)
ax.set_ylim3d(min(path[:,1])-5,max(path[:,1])+5)
ax.set_zlim3d(min(path[:,2])-5,max(path[:,2])+5)

def az(i,path,l):
    l.set_data(path[:i,0],path[:i,1])
    l.set_3d_properties(path[:i,2])



N=100


ani = animation.FuncAnimation(fig, az, fargs=(path, l), interval=10000/N, frames=loop, blit=False,repeat=False)
ani.event_source.stop()
ani.event_source.start()
#ani.save('matplot003.gif', writer='imagemagick')

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save('im.mp4', writer=writer)
plt.show()

