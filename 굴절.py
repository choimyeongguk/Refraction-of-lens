import matplotlib.pyplot as plt
import numpy as np

def f(x):
 return 1/2*x**2

def f2(x):
 return -1/2*x**2+25

def f_d(x):
 return x

def f2_d(x):
 return -x

def find_x(a, t):
 if(a!=0):
  if(t<f(a)):
   return a
  else:
   return (1/np.tan(5/3*np.arctan(f_d(a))))*(t-f(a))+a
 else:
  return 0

x_lens_d, y_lens_d = list(np.arange(-5, 5.1, 0.1)), list(f(np.arange(-5, 5.1, 0.1)))
x_lens_u, y_lens_u = list(np.arange(-5, 5.1, 0.1)), list(f2(np.arange(-5, 5.1, 0.1)))
ray_x, ray_y = [], []

for i in np.arange(-5, 6):
 line = []
 for j in np.arange(-1, 25, 1):
  line.append(find_x(1.2, i))
 ray_x.append(line)
for i in np.arange(-1, 25, 1):
 ray_y.append(i)
 

plt.plot(x_lens_d, y_lens_d, color='blue', linewidth='3')
plt.plot(x_lens_u, y_lens_u, color='blue', linewidth='3')
line = []
for i in range(len(ray_x[0])):
 line.append(ray_x[0][i])
plt.plot(line, ray_y, color='red', linewidth='2')
# print(line)
# print(ray_y)

plt.show()