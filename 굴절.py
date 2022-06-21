import matplotlib.pyplot as plt
import numpy as np

def f(x):
 return 1/4*x**2

def f_d(x):
 return 1/2*x

def T(a):
  return np.tan(np.arctan(f_d(a))+np.arcsin((3*f_d(a))/(2*np.sqrt(f_d(a)+1))))

def find_x(a, t):
 if(a!=0):
  if(t<f(a)):
   return a
  else:
   return 1/T(a)*(t-f(a))+a
 else:
  return 0

x_lens_d, y_lens_d = list(np.arange(-5, 5.1, 0.1)), list(f(np.arange(-5, 5.1, 0.1)))
ray_x, ray_y = [], []

plt.plot(x_lens_d, y_lens_d, color='blue', linewidth='3')

for k in np.arange(-5, 5.5, 0.5):
  for i in np.arange(-2, 20, 0.01):
    ray_x.append(find_x(k, i))
    ray_y.append(i)
  plt.scatter(ray_x, ray_y, color='red', s=1)
  ray_x.clear()
  ray_y.clear()

plt.plot([0, 0],[-10,100], color='black')
plt.xlim([-6, 6])
plt.ylim([-2, 20])
plt.show()