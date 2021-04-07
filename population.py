import numpy as np
import matplotlib.pyplot as plt

def analytic_solution(t, K=1, P0=1, r=0.01):
    """K = maximum carrying capacity of ecosystem
       P0 = initial population at time t=0
       r = population growth rate (eg, 1% = 0.01
       t = time """
    #Fill this in
    return (K*P0*np.exp(r*t))/(K+P0*(np.exp(r*t)-1))

def dP_dt(P, K=1, r=0.01):
    #Fill this in, including comments
    return r*P*(1-(P/K))


def forward_euler(timestep = None,
                  max_time = None,
                  initial_time = None,
                  initial_val = None,
                  deriv = None, #pass dP_dt
                  deriv_params = None):
    #fill this in, including comments
    #return times, vals
    times = []
    vals = []
    while initial_time + timestep < max_time:
        times.append(initial_time + 1800)
        vals.append(initial_val)
        initial_val = initial_val + timestep*deriv(initial_val,
                                                   deriv_params['K'],
                                                   deriv_params['r'])
        initial_time += timestep
    return times, vals

def rk4(timestep = None,
        max_time = None,
        initial_time = None,
        initial_val = None,
        deriv = None,
        deriv_params = None):
    #fill this in, including comments
    #return times, vals
    times = []
    vals = []
    while initial_time + timestep < max_time:
        times.append(initial_time+1800)
        vals.append(initial_val)
        k1 = timestep*deriv(initial_val, deriv_params['K'],
                            deriv_params['r'])
        k2 = timestep*deriv(initial_val+0.5*k1, deriv_params['K'],
                            deriv_params['r'])
        k3 = timestep*deriv(initial_val+0.5*k2, deriv_params['K'],
                            deriv_params['r'])
        k4 = timestep*deriv(initial_val+k3, deriv_params['K'],
                            deriv_params['r'])
        initial_val = initial_val + ((k1+2*k2+2*k3+k4)/6)
        initial_time += timestep       
    return times, vals

if __name__ == "__main__":
    K = 10 #10 billion
    P0 = 1 #billion, population at year 1800
    r = 0.014 #1.4% growth rate
    start_year = 1800
    max_year = 2300
    max_time = max_year - start_year
    years_since_start = np.arange(0, max_time)

    analytic_sol = analytic_solution(years_since_start, K=K, P0=P0, r=r)
    timestep=25
    eulerTimes, eulerVals = forward_euler(initial_val=P0, initial_time=0,
                             timestep=timestep,
                             max_time=max_time, deriv=dP_dt,
                             deriv_params={'K':K, 'r':r})
    rk4Times, rk4Vals = rk4(initial_val=P0, initial_time=0,
                             timestep=timestep,
                             max_time=max_time, deriv=dP_dt,
                             deriv_params={'K':K, 'r':r})
    
    plt.scatter(eulerTimes, eulerVals, label="Forward Euler", marker='.',
                color='magenta')
    plt.scatter(rk4Times, rk4Vals, label='RK4', marker='.', color='green')
    years_since_start += 1800
    plt.plot(years_since_start, analytic_sol, label='Analytic Solution')
    plt.title('Population over Time')
    plt.xlabel('Years')
    plt.ylabel('Population in Billions')
    plt.legend()
    plt.show()
