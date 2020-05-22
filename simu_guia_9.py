import numpy as np
import matplotlib.pyplot as plt

# Defino funciones
def B(r,a,b,I):
    mu0 = 12.57e-7
    I   = 100
    if r<b:
        campo = 0
    elif ((r<a) & (r>b)):
        campo = (mu0*I/2/np.pi/(a**2-b**2))*(r**2-b**2)/r
    else:
        campo = mu0*I/2/np.pi/r

    return campo

def B1(r,a,b,c,I):
    mu0 = 12.57e-7
    I   = 100
    if r<=a:
        campo = r*mu0*I/2/np.pi/a**2
    elif ((r<b) & (r>a)):
        campo = mu0*I/2/np.pi/r
    elif ((r<c) & (r>b)):
        campo = mu0*I/2/np.pi/r - mu0*I*(r**2-b**2)/(c**2-b**2)/(2*np.pi*r)
    else:
        campo = 0
    return campo

# Paso a graficar los campos
N = 500
r = np.linspace(0,20,N)
r1 = np.linspace(0,10,N)
a = 6
b = 2
I = 100

Bcampo = np.zeros((N,1))
B1campo = np.zeros((N,1))
for jj in range(N):
    Bcampo[jj] = B(r[jj],a,b,I)
    B1campo[jj] = B1(r1[jj],1,3,6,I)

fig = plt.figure(1,figsize=(9,6))
ax = fig.add_subplot(111)
ax.plot(r, Bcampo*1e4, linewidth=2)
ax.set_xlabel(r'Distancia (m)', fontsize=14)
ax.set_ylabel(r'Campo (G)', fontsize=14)
ax.grid(linestyle='--')
fig.tight_layout()
plt.savefig('figuras_problemas/campo_magnetico.png')

fig = plt.figure(2,figsize=(9,6))
ax = fig.add_subplot(111)
ax.plot(r1, B1campo*1e4, linewidth=2)
ax.set_xlabel(r'Distancia (#a)', fontsize=14)
ax.set_ylabel(r'Campo (u.a.)', fontsize=14)
ax.grid(linestyle='--')
fig.tight_layout()
plt.savefig('figuras_problemas/campo_magnetico_prob15.png')
