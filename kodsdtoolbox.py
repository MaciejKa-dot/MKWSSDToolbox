import cantera as ct
from sdtoolbox.postshock import CJspeed
from sdtoolbox.postshock import PostShock_eq
from sdtoolbox.thermo import soundspeed_eq, soundspeed_fr
import numpy as np
import matplotlib.pyplot as plt

P0 = 253312.5 #lub 1266562.5/759937.5 zaleznie od przypadku
T0 = 1200 #lub 350/700 zaleznie od przypadku

npoints = 20

q1 = 'C3H8:1 O2:5'#lub 'H2:2 O2:1'/'CH4:1 O2:2' zaleznie od przypadku 


mech = 'gri30.xml'


#substance + oxygen
gas_initial2 = ct.Solution(mech)
gas_initial2.TPX = T0, P0, q1

#compute CJ speed for different pressures
speed2 = np.zeros(npoints)


P = np.linspace(0.1*ct.one_atm, ct.one_atm*3, npoints)


for i in range(npoints):
    [cj_speed,R2,plot_data] = CJspeed(P[i], T0, q1, mech, fullOutput=True)  
    speed2[i] = cj_speed

    
print('V(p) for H2-oxygen mixture')
fig, ax = plt.subplots()
ax.plot(P/100000, speed2)
ax.set(xlabel='Pressure [bar]', ylabel='Detonation speed [m/s]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()


#compute CJ speed for different temperatures
speed5 = np.zeros(npoints)


T = np.linspace(273, 2000, npoints)


for i in range(npoints):
    [cj_speed,R2,plot_data] = CJspeed(P0, T[i], q1, mech, fullOutput=True)  
    speed5[i] = cj_speed
    
print('V(T) for H2-oxygen mixture')
fig, ax = plt.subplots()
ax.plot(T, speed5)
ax.set(xlabel='Temperature [T]', ylabel='Detonation speed [m/s]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()