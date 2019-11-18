
# coding: utf-8

# In[21]:


# get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
import matplotlib.animation
plt.rcParams["animation.html"] = "jshtml"
import numpy as np


# In[22]:


dims = 1
step_n = 500
loop = 500+1
step_set = [-1, 0, 1]
origin = np.zeros((1,dims))

x = np.arange(step_n+1)
x=x.tolist()

step_shape = (step_n,dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin, steps]).cumsum(0)

fig, ax = plt.subplots()
l, = ax.plot([],[])

pathe = path.tolist()

h = ax.axis([-10,step_n,min(path),max(path)])

def a(i):
    l.set_data(x[:i],pathe[:i])
# ax.plot(path,c='blue',alpha=0.5,lw=0.5,ls='solid',);
plt.rcParams['figure.figsize'] = [10, 10]
ani = matplotlib.animation.FuncAnimation(fig, a, interval=1, frames=loop)
ani.event_source.stop()
ani.event_source.start()


ax.set_title('1D Random Walk')
plt.tight_layout(pad=0)
# plt.savefig('random_walk_1d.png',dpi=250);
plt.show()