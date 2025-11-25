import sympy as sp
import numpy as np
import math
import matplotlib.pyplot as plt

# Définir la variable symbolique t (temps en minutes)
t = sp.symbols('t')

# Demander combien de mesures de température ont été prises
n = int(input("Combien de fois avez-vous mesuré la température ? "))

# Listes pour stocker les instants (en minutes) et les températures mesurées
temps = []
temperature = []

# Saisie des données expérimentales
for i in range(n):
    ti = float(input(f"Entrez l'instant t{i} (en minutes) : "))
    Ti = float(input(f"Entrez la température T(t{i}) (en °C) : "))
    temps.append(ti)
    temperature.append(Ti)

# Fonction d'interpolation de Lagrange
def Lagrange(temps, temperature, t):
    n = len(temps)
    L = []  # Liste des polynômes de base L_i(t)

    for i in range(n):
        l = 1
        for j in range(n):
            if i != j:
                l *= (t - temps[j]) / (temps[i] - temps[j])
        L.append(sp.simplify(l))  # Simplifier chaque L_i(t)

    # Construction du polynôme interpolateur T(t)
    P = 0
    for i in range(n):
        P += L[i] * temperature[i]

    return sp.simplify(P), L

# Calcul du polynôme interpolateur
Tt, L = Lagrange(temps, temperature, t)

# Affichage des résultats
print("\nInstants mesurés t_i (en minutes) :", temps)
print("Températures mesurées T(t_i) (en °C) :", temperature)
print("\nPolynômes de base L_i(t) :")

for i, li in enumerate(L):
    print(f"L{i}(t) =", li)

print("\nPolynôme interpolateur T(t) =", Tt)

# Tracé graphique de T(t)
f_num = sp.lambdify(t, Tt, modules=['numpy'])
t_vals = np.linspace(min(temps), max(temps), 100)
T_vals = f_num(t_vals)

plt.plot(t_vals, T_vals, label='T(t) interpolé')
plt.scatter(temps, temperature, color='red', label='Mesures expérimentales')
plt.xlabel("Temps t (min)")
plt.ylabel("Température T(t) (°C)")
plt.title("Évolution de la température T(t) en fonction du temps (Heures)")
plt.grid(True)
plt.legend()
plt.show()
