import matplotlib.pyplot as plt
import numpy as np

global contact

## negative meniscus lens function ##

def f1(x):
 return -1/10*x**2
def f1_d(x):
 return -1/5*x

def g1(x):
 return -1/1000000*x**2+5
def g1_d(x):
 return -1/500000*x

def Mn1(x):
 return np.tan(np.pi/2-np.arctan(-f1_d(x))+np.arcsin(2/3*np.sin(np.arctan(-f1_d(x)))))
def Mn2(x):
 return np.tan(np.arctan(-1/g1_d(contact))+np.arcsin(3/2*np.sin(np.arctan(-1/g1_d(contact))-np.arctan(Mn1(x)))))

def find_xn(x, y):
 if(y<=f1(x) or x<-5 or x>5):
  return x
 elif(f1(x)<y<=g1(contact)):
  return 1/Mn1(x)*(y-f1(x))+x
 else:
  return 1/Mn2(x)*(y-g1(contact))+contact


## positive meniscus lens function ##

def f2(x):
 return 1/10*x**2
def f2_d(x):
 return 1/5*x

def g2(x):
 return +1/1000000*x**2+5
def g2_d(x):
 return +1/500000*x

def Mp1(x):
 return np.tan(np.pi/2-np.arctan(-f2_d(x))+np.arcsin(2/3*np.sin(np.arctan(-f2_d(x)))))
def Mp2(x):
 return np.tan(np.arctan(-1/g2_d(contact))+np.arcsin(3/2*np.sin(np.arctan(-1/g2_d(contact))-np.arctan(Mp1(x)))))

def find_xp(x, y):
 if(y<=f2(x) or x<-5 or x>5):
  return x
 elif(f2(x)<y<=g2(contact)):
  return 1/Mp1(x)*(y-f2(x))+x
 else:
  return 1/Mp2(x)*(y-g2(contact))+contact


ray_x, ray_y = [], []
plt.figure(figsize=(12, 6))

## negative lens drawing ##

plt.subplot(121)
lens_d = [list(np.linspace(-5, 5, 100)), list(f1(np.linspace(-5, 5, 100)))]
lens_u = [list(np.linspace(-5, 5, 100)), list(g1(np.linspace(-5, 5, 100)))]
plt.axis([-5.5, 5.5, -3, 20])
plt.xticks(range(0), range(0))
plt.yticks(range(0), range(0))
plt.title("negative meniscus lens")
plt.plot(lens_d[0], lens_d[1], color='skyblue', linewidth='3', zorder=0)
plt.plot(lens_u[0], lens_u[1], color='skyblue', linewidth='3', zorder=0)

for x in np.linspace(-3, 3, 50):
 alpha = -5*Mn1(x)+np.sqrt(25*Mn1(x)**2+10*Mn1(x)*x-10*f1(x)+50)
 beta = -5*Mn1(x)-np.sqrt(25*Mn1(x)**2+10*Mn1(x)*x-10*f1(x)+50)
 contact = alpha if g1(alpha)>g1(beta) else beta
 for y in np.arange(-3, 20, 0.1):
  ray_x.append(find_xn(x, y))
  ray_y.append(y)
 plt.plot(ray_x, ray_y, color='red', linewidth='0.5', zorder=1)
 ray_x.clear()
 ray_y.clear()


## positive lens drawing ##

plt.subplot(122)
lens_d = [list(np.linspace(-5, 5, 100)), list(f2(np.linspace(-5, 5, 100)))]
lens_u = [list(np.linspace(-5, 5, 100)), list(g2(np.linspace(-5, 5, 100)))]
plt.axis([-5.5, 5.5, -3, 20])
plt.xticks(range(0), range(0))
plt.yticks(range(0), range(0))
plt.title("positive meniscus lens")
plt.plot(lens_d[0], lens_d[1], color='skyblue', linewidth='3', zorder=0)
plt.plot(lens_u[0], lens_u[1], color='skyblue', linewidth='3', zorder=0)

for x in np.linspace(-3, 3, 50):
 alpha = 5*Mp1(x)+np.sqrt(25*Mp1(x)**2-10*Mp1(x)*x+10*f2(x)-50)
 beta = 5*Mp1(x)-np.sqrt(25*Mp1(x)**2-10*Mp1(x)*x+10*f2(x)-50)
 contact = beta if g2(alpha)>g2(beta) else alpha
 for y in np.arange(-3, 20, 0.1):
  ray_x.append(find_xp(x, y))
  ray_y.append(y)
 plt.plot(ray_x, ray_y, color='red', linewidth='0.5', zorder=1)
 ray_x.clear()
 ray_y.clear()

plt.show()