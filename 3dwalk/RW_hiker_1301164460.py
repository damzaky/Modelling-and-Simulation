
# coding: utf-8

# In[1]:


# get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
import matplotlib.animation
plt.rcParams["animation.html"] = "jshtml"
import numpy as np
from matplotlib.lines import Line2D


# In[2]:


dims = 2
step_n = 100
loop=step_n

step_set=[0,1,2,3,4,5,6,7]

origin = [[0,100]]#np.zeros((1,dims))
# print(origin)
step_shape = step_n
steps = np.random.choice(a=step_set, size=step_shape,p=[0.2, 0.09, 0.01, 0.15,0.02, 0.02,0.17 ,0.34])#probability
def coor(ar):
    dic=[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]] #x,y: E, NE, N, NW, W, SW, S, SE
    nr = []
    for k in ar:
        nr.append(dic[k])
    return nr
stepss=coor(steps)


# In[3]:



path = np.concatenate([origin, stepss]).cumsum(0)

x = np.arange(step_n+1)
x=x.tolist()
pathe=path.tolist()
start = path[:1]
stop = path[-1:]

fig, ax = plt.subplots()
l, = ax.plot([],[]) #,c='blue',alpha=0.5,lw=0.25,ls='solid'

ax.plot(start[:,0], start[:,1],c='red', marker='+')

h = ax.axis([min(path[:,0])-5,max(path[:,0])+5,min(path[:,1])-5,max(path[:,1])+5])
def a(i):
    l.set_data(path[:i,0],path[:i,1])

plt.rcParams['figure.figsize'] = [10, 10]
ani = matplotlib.animation.FuncAnimation(fig, a, interval=40, frames=loop,repeat=False)
ani.event_source.stop()
ani.event_source.start()

ax.set_title('2D Random Walk')
plt.tight_layout(pad=0)


# In[5]:


plt.savefig('rw9.png',dpi=250);
plt.show()

