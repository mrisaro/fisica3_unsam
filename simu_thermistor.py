import numpy as np
import matplotlib.pyplot as plt

# defino la resistencia como función de T
def Rt(T,param):
    R0 = param[0]
    B  = param[1]
    T0 = 298.15

    Rt = R0*np.exp(B*(1/T-1/T0))
    return Rt

# creo algunos termistores
T = np.linspace(0,55,500)+273.15
R0 = 220
B  = 3650
term_ntc = Rt(T,[R0,B])
term_ptc = Rt(T,[R0,-B])

fig = plt.figure(1,figsize=(9,6))
ax = fig.add_subplot(111)
ax.plot(T, term_ntc, linewidth=2)
ax.plot(T, term_ptc, linewidth=2)
ax.set_xlabel(r'Temperatura (K)')
ax.set_ylabel(r'Resistencia ($\Omega$)')
ax.set_ylim(0,700)
ax.grid(linestyle='--')
fig.tight_layout()
plt.show()
