import matplotlib.pyplot as plt
import numpy as np

global contact

def f(x):
 return -1/10*x**2
def f_d(x):
 return -1/5*x

def g(x):
 return +1/10*x**2+5
def g_d(x):
 return +1/5*x

def M1(x):
 return np.tan(np.pi/2-np.arctan(-f_d(x))+np.arcsin(2/3*np.sin(np.arctan(-f_d(x)))))
def M2(x):
 return np.tan(np.arctan(-1/g_d(contact))+np.arcsin(3/2*np.sin(np.arctan(-1/g_d(contact))-np.arctan(M1(x)))))

def find_x(x, y):
 if(y<=f(x) or x<-5 or x>5):
  return x
 elif(f(x)<y<=g(contact)):
  return 1/M1(x)*(y-f(x))+x
 else:
  return 1/M2(x)*(y-g(contact))+contact

lens_d = [list(np.linspace(-5, 5, 100)), list(f(np.linspace(-5, 5, 100)))]
lens_u = [list(np.linspace(-5, 5, 100)), list(g(np.linspace(-5, 5, 100)))]
ray_x, ray_y = [], []

plt.figure(figsize=(6, 6))
plt.axis([-5.5, 5.5, -3, 20])
plt.xticks(range(0), range(0))
plt.yticks(range(0), range(0))
plt.title("concave lens")
plt.plot(lens_d[0], lens_d[1], color='skyblue', linewidth='3', zorder=1)
plt.plot(lens_u[0], lens_u[1], color='skyblue', linewidth='3', zorder=1)

for x in np.linspace(-3, 3, 50):
 alpha = 5*M1(x)+np.sqrt(25*M1(x)**2-10*M1(x)*x+10*f(x)-50)
 beta = 5*M1(x)-np.sqrt(25*M1(x)**2-10*M1(x)*x+10*f(x)-50)
 contact = beta if g(alpha)>g(beta) else alpha
 for y in np.arange(-3, 20, 0.1):
  ray_x.append(find_x(x, y))
  ray_y.append(y)
 plt.plot(ray_x, ray_y, color='red', linewidth='0.5', zorder=0)
 ray_x.clear()
 ray_y.clear()


plt.show()