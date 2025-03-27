import numpy as np
import matplotlib.pyplot as plt

n_pasos = 100  # Numero de pasos

# Se generan pasos random: +1 o -1
pasos = np.random.choice([-1, 1], size=n_pasos)

# Calcular posiciones
posiciones = np.cumsum(pasos)

# Graficar el camino aleatorio
plt.figure(figsize=(10, 6))
plt.plot(posiciones, marker='o', linestyle='-', markersize=4)
plt.title("Camino Aleatorio 1D")
plt.xlabel("Pasos")
plt.ylabel("Posición")
plt.grid(True)
plt.show()
