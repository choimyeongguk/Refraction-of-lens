import matplotlib.pyplot as plt
import numpy as np

def f(x):
 return 1/10*x**2

def g(x):
  return -1/10*x**2+5

def f_d(x):
 return 1/5*x

def g_d(x):
  return -1/5*x

def T1(x):
  if(x<0):
    return np.tan(np.pi/2-np.arctan(-f_d(x))+np.arcsin(2/3*np.sin(np.arctan(-f_d(x)))))
  else:
    return np.tan(np.pi/2+np.arctan(f_d(x))-np.arcsin(2/3*np.sin(np.arctan(f_d(x)))))

def T2(x):
  if(contact<0):
    return np.tan(np.arctan(-1/g_d(contact))-np.arcsin(3/2*np.sin(np.arctan(-1/g_d(contact))-np.arctan(T1(x)))))
  else:
    return np.tan(np.arctan(-1/g_d(contact))+np.arcsin(3/2*np.sin(-np.arctan(-1/g_d(contact))+np.arctan(T1(x)))))

def find_x(a, t):
  if(t<=f(a)):
   return a
  elif(f(a)<t<=f2(a)):
   return 1/T(a)*(t-f(a))+a
  else:
    return 1/T2(a)*(t-f2(contact))+contact

x_lens_d, y_lens_d = list(np.arange(-5, 5.1, 0.1)), list(f(np.arange(-5, 5.1, 0.1)))
x_lens_u, y_lens_u = list(np.arange(-5, 5.1, 0.1)), list(f2(np.arange(-5, 5.1, 0.1)))
ray_x, ray_y = [], []

plt.figure(figsize=(7, 5))
plt.xlim([-5.5, 5.5])
plt.ylim([-2, 20])
plt.plot(x_lens_d, y_lens_d, color='skyblue', linewidth='8', zorder=1)
plt.plot(x_lens_u, y_lens_u, color='skyblue', linewidth='8', zorder=1)

for i in np.linspace(-3, 3, 25):
  alpha = -5*T(i)+np.sqrt(25*T(i)**2+10*T(i)*i-10*f(i)+50)
  beta = -5*T(i)-np.sqrt(25*T(i)**2+10*T(i)*i-10*f(i)+50)
  contact = alpha if f2(alpha)>=f2(beta) else beta
  for j in np.arange(-2, 20, 0.01):
    ray_x.append(find_x(i, j))
    ray_y.append(j)
  plt.plot(ray_x, ray_y, color='red', linewidth='1', zorder=0)
  ray_x.clear()
  ray_y.clear()
  print("%lf"%contact)

plt.show()