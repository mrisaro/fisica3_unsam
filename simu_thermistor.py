import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# defino la resistencia como función de T
def Rt(T,param):
    R0 = param[0]
    B  = param[1]
    T0 = 298.15

    Rt = R0*np.exp(B*(1/T-1/T0))
    return Rt

def Vt(T,rt,param):
    V0 = param[0]
    Rf = param[1]
    R0 = param[2]

    vt = V0*(rt/(Rf+R0+rt))
    return vt

def func(x, A, B):
    return A*np.exp(B/x)

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
plt.savefig('figuras_tps/termistor_temperatura.png')

N = 100
T = np.linspace(0,100,N)+273.15
R0 = 220
B  = 3650
rt = Rt(T,[R0,B])
vt_ntc = Vt(T,rt,[5,2,50])*np.random.normal(1,0.01,N)

fig = plt.figure(2,figsize=(9,6))
ax = fig.add_subplot(111)
ax.plot(T, vt_ntc, 'o')
ax.set_xlabel(r'Temperatura (K)',fontsize = 14)
ax.set_ylabel(r'V$_{term}$ (V)',fontsize = 14)
ax.grid(linestyle='--')
fig.tight_layout()
plt.savefig('figuras_tps/v_term_temperatura.png')

Rt_exp = vt_ntc*(2+50)/(5-vt_ntc)
popt, pcov = curve_fit(func, T, Rt_exp, p0=(100, 3000))

fig = plt.figure(3,figsize=(9,6))
ax = fig.add_subplot(111)
ax.plot(T, Rt_exp, 'o', label='Datos experimentales')
ax.plot(T, func(T,popt[0],popt[1]), '--', label='fit')
ax.plot(T, rt, '-', label='Curva teórica')
ax.set_xlabel(r'Temperatura (K)', fontsize = 14)
ax.set_ylabel(r'Resistencia ($\Omega$)', fontsize = 14)
ax.legend(fontsize=14)
ax.grid(linestyle='--')
fig.tight_layout()
plt.savefig('figuras_tps/R_term_temperatura.png')

data = np.array([T-273.15, vt_ntc, rt])
file_name = 'data_f3.txt'
np.savetxt(file_name, data.T, header="Temp(C),Vt(V),Rteo(Ohm)", fmt='%1.3f',
					delimiter=',', comments='')
