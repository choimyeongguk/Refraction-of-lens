import matplotlib.pyplot as plt
import numpy as np

contact = 0

def f(x):
 return 1/10*x**2

def f2(x):
  return -1/10*x**2+5

def f_d(x):
 return 1/5*x

def f2_d(x):
  return -1/5*x

def T(a):
  if(f_d(a)<0):
    return np.tan(np.pi/2-np.arctan(-f_d(a))+np.arcsin(2/3*np.sin(np.arctan(-f_d(a)))))
  else:
    return np.tan(np.pi/2+np.arctan(f_d(a))-np.arcsin(2/3*np.sin(np.arctan(f_d(a)))))

def T2(a):
  alpha = -5*T(a)+np.sqrt(25*T(a)**2+10*T(a)*a-10*f(a)+50)
  beta = -5*T(a)-np.sqrt(25*T(a)**2+10*T(a)*a-10*f(a)+50)
  contact = alpha if f(alpha)>f(beta) else beta
  if(f2_d(a)>=0):
    return np.arctan(-1/f2_d(contact))-np.arcsin(3/2*np.sin(np.arctan(-1/f2_d(a))-np.arctan(T(a))))
  else:
    return np.tan(np.arcsin(3/2*np.sin(np.arctan(T(a))-np.arctan(-1/f2_d(a))))+np.arctan(-1/f2_d(a)))

def find_x(a, t):
  if(t<f(a)):
   return a
  elif(f(a)<=t<f2(a)):
   return 1/T(a)*(t-f(a))+a
  else:
    return 1/T2(a)*(t-f2(contact))+contact

x_lens_d, y_lens_d = list(np.arange(-5, 5.1, 0.1)), list(f(np.arange(-5, 5.1, 0.1)))
x_lens_u, y_lens_u = list(np.arange(-5, 5.1, 0.1)), list(f2(np.arange(-5, 5.1, 0.1)))
ray_x, ray_y = [], []

plt.plot(x_lens_d, y_lens_d, color='skyblue', linewidth='3')
plt.plot(x_lens_u, y_lens_u, color='skyblue', linewidth='3')

for i in np.arange(-3, 3.5, 0.5):
  for j in np.arange(-2, 30, 0.001):
    ray_x.append(find_x(i, j))
    ray_y.append(j)
  plt.scatter(ray_x, ray_y, color='red', s=0.1)
  ray_x.clear()
  ray_y.clear()

plt.xlim([-5.5, 5.5])
plt.ylim([-2, 25])
plt.show()