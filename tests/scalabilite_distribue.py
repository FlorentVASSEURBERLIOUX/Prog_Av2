import matplotlib.pyplot as plt
import numpy as np

# Données pour la scalabilité forte
processeurs_forte = np.array([1, 4, 8, 12, 16, 24, 32, 48])
temps_forte = np.array([5873, 1506, 756, 508, 385, 267, 206, 133])

# Calcul du speed-up pour la scalabilité forte
speedup_forte = temps_forte[0] / temps_forte
# Speedup idéal forte (égal au nombre de processeurs)
speedup_ideal_forte = processeurs_forte

# Données pour la scalabilité faible
processeurs_faible = np.array([1, 4, 8, 12, 16, 24, 32, 48])
temps_faible = np.array([129, 140, 143, 136, 134, 139, 140, 141])

# Calcul du speed-up pour la scalabilité faible
speedup_faible = temps_faible[0] / temps_faible
# Speedup idéal faible (constant à 1)
speedup_ideal_faible = np.ones_like(processeurs_faible)

# Création des graphiques
fig, axs = plt.subplots(2, 2, figsize=(15, 12))

# Graphique de la scalabilité forte
axs[0, 0].plot(processeurs_forte, temps_forte, marker='o', color='b', label="Temps d'exécution")
axs[0, 0].set_title("Scalabilité Forte")
axs[0, 0].set_xlabel("Nombre de processeurs")
axs[0, 0].set_ylabel("Temps d'exécution (s)")
axs[0, 0].grid(True)
axs[0, 0].legend()
axs[0, 0].set_xlim(0, max(processeurs_forte))
axs[0, 0].set_ylim(0, max(temps_forte))

# Graphique du speed-up pour la scalabilité forte
axs[0, 1].plot(processeurs_forte, speedup_forte, marker='o', color='g', label="Speed-up réel")
axs[0, 1].plot(processeurs_forte, speedup_ideal_forte, '--b', label="Speed-up idéal")
axs[0, 1].set_title("Speed-up - Scalabilité Forte")
axs[0, 1].set_xlabel("Nombre de processeurs")
axs[0, 1].set_ylabel("Speed-up")
axs[0, 1].grid(True)
axs[0, 1].legend()
axs[0, 1].set_xlim(0, max(processeurs_forte))
axs[0, 1].set_ylim(0, max(speedup_ideal_forte))

# Graphique de la scalabilité faible
axs[1, 0].plot(processeurs_faible, temps_faible, marker='o', color='r', label="Temps d'exécution")
axs[1, 0].set_title("Scalabilité Faible")
axs[1, 0].set_xlabel("Nombre de processeurs")
axs[1, 0].set_ylabel("Temps d'exécution (s)")
axs[1, 0].grid(True)
axs[1, 0].legend()
axs[1, 0].set_xlim(0, max(processeurs_faible))
axs[1, 0].set_ylim(0, max(temps_faible))

# Graphique du speed-up pour la scalabilité faible
axs[1, 1].plot(processeurs_faible, speedup_faible, marker='o', color='purple', label="Speed-up réel")
axs[1, 1].plot(processeurs_faible, speedup_ideal_faible, '--b', label="Speed-up idéal")
axs[1, 1].set_title("Speed-up - Scalabilité Faible")
axs[1, 1].set_xlabel("Nombre de processeurs")
axs[1, 1].set_ylabel("Speed-up")
axs[1, 1].grid(True)
axs[1, 1].legend()
axs[1, 1].set_xlim(0, max(processeurs_faible))
axs[1, 1].set_ylim(0, 2)  # Fixed y-axis scale from 0 to 2

plt.tight_layout()
plt.show()
