import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def fun(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

def nlin_model1(y, t, b, c):
    omega, theta = y
    dydt =  omega     
    return dydt
    
def nlin_model2(y, t, b, c):
    omega, theta = y
    dydt = -b*omega - c*np.sin(theta)    
    return dydt
   
def func_agg( f_list ):
    dydt = [ 0 , 0 ]
    def wrapper( y , t , b , c ):
        for i, fun in enumerate(f_list):
            dydt[i] = fun( y , t , b , c )
        return dydt
    return wrapper


f_list = [ nlin_model1, nlin_model2 ]
fun2 = func_agg( f_list )
b = 0.25
c = 5.0
y0 = [np.pi - 0.1, 0.0]
t = np.linspace(0, 10, 101)
sol = odeint(fun, y0, t, args=(b, c))
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')


sol2 = odeint(fun2, y0, t, args=(b, c))
plt.plot(t, sol[:, 0], 'k--', label='theta(t)2')
plt.plot(t, sol[:, 1], 'y--', label='omega(t)2')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
a=1