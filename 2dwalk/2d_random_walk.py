
# coding: utf-8

# In[1]:


# get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
import matplotlib.animation
plt.rcParams["animation.html"] = "jshtml"
import numpy as np
# from matplotlib.lines import Line2D


# In[5]:


# Define parameters for the walk
dims = 2
step_n = 500
loop=step_n+1
step_set = [-1, 0, 1]
origin = np.zeros((1,dims))
# Simulate steps in 2D
step_shape = (step_n,dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin, steps]).cumsum(0)

x = np.arange(step_n+1)
x=x.tolist()
pathe=path.tolist()
start = path[:1]
stop = path[-1:]
# Plot the path
# fig = plt.figure()
# ax = fig.add_subplot(111)

fig, ax = plt.subplots()
l, = ax.plot([],[]) 

ax.plot(start[:,0], start[:,1],c='red', marker='+')
ax.plot(stop[:,0], stop[:,1],c='black', marker='o')
# ax.plot(path[:,0], path[:,1],c='blue',alpha=0.5,lw=0.25,ls='solid');

h = ax.axis([min(path[:,0])-5,max(path[:,0])+5,min(path[:,1])-5,max(path[:,1])+5])
# print(type(l))
def a(i):
    l.set_data(path[:i,0],path[:i,1])

plt.rcParams['figure.figsize'] = [10, 10]
ani = matplotlib.animation.FuncAnimation(fig, a, interval=10, frames=loop)
ani.event_source.stop()
ani.event_source.start()


ax.set_title('2D Random Walk')
plt.tight_layout(pad=0)
# plt.savefig('random_walk_2d.png',dpi=250);


plt.show()