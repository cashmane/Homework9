import numpy as np
import matplotlib.pyplot as plt

m = 0.145 #kg, mass of baseball
g = np.array([0, -9.8]) #m/s^2, accel of grav at surface
rho = 1.225 #kg/m^3, density of air at STP
Cd = 0.47 #[unitless], drag coefficient of sphere
A = 0.00414 #m^2, cross-sectional area of baseball

def analytic_projectile_nodrag(t,
                               initial_position=None,
                               initial_velocity=None):
    #trick to apply to x and y component simultaneously
    times = t[:,np.newaxis]
    return initial_position +\
           initial_velocity*times + \
           g*0.5*times**2

def fg():
    return m*g

def fdrag(speed):
    return 0.5*rho*speed**2*Cd*A

def rk4(firstVector, secondVector, times, timestep):
    vals = []
    for i in range(len(times)):
        vals.append(firstVector)
        k1 = timestep*secondVector
        k2 = timestep*(secondVector+0.5*k1)
        k3 = timestep*(secondVector+0.5*k2)
        k4 = timestep*(secondVector+k3)
        firstVector = firstVector + ((k1+2*k2+2*k3+k4)/6)  
    return vals

if __name__ == "__main__":
    print("test")
    
    times = np.arange(0, 10, 0.01)
    angle = 45*np.pi/180 #degrees
    speed = 10 #m/s
    x0 = np.array([0,0])
    v0 = speed*np.array([np.cos(angle), np.sin(angle)])
    firstVector = np.array([0, 0, speed*np.cos(angle), speed*np.sin(angle)])
    secondVector = np.array([speed*np.cos(angle), speed*np.sin(angle),
                            0, -9.8])
    positions = analytic_projectile_nodrag(times,
                                           initial_position=x0,
                                           initial_velocity=v0)
    rk4pos = list(rk4(firstVector, secondVector, times, 0.01))
    rk4positions = []
    for pos in rk4pos:
       #pos = list(pos)
       rk4positions.append(pos[1])
        
    print('RK4', rk4positions)
    plt.plot(times, positions, label='analytic')
    plt.plot(times, rk4positions, label='rk4')
    plt.legend()
    plt.show()
