import numpy as np
from scipy import linalg, signal
import matplotlib.pyplot as plt

'''
USAMOS SCIPY PARA ALGEBRA LINEAL
'''
A = np.array([
    [2, 1],
    [1, -1]
])
B = np.array([5, 1])

sol = linalg.solve(A, B) #Sistema de ecuaciones lineales
print("Solución del sistema:", sol)

'''
USAMOS SCIPY PARA SEÑALES
'''
t = np.linspace(0,1,500, endpoint=False)
signal_original = np.sin(2 * np.pi * 5 * t)

ruido = 0.3 * np.random.normal(size=t.shape)
signal_ruidosa = signal_original + ruido

b, a = signal.butter(3, 0.1) 
signal_filtrada = signal.filtfilt(b,a, signal_ruidosa)


plt.figure(figsize=(10,5))
plt.plot(t, signal_ruidosa, label="Señal con ruido")
plt.plot(t, signal_filtrada, label="Señal filtrada")
plt.plot(t, signal_original, label="Señal original")
plt.title("Proceso de señales con Scipy")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.legend()
plt.show()
