import pandas as pd
import matplotlib.pyplot as plt

file_path = 'U:/Prog. Av/Projet/Prog_Av2/tests/pi.txt'
df = pd.read_csv(file_path, sep=';', header=None, names=['Error', 'Npoint', 'Pi', 'Nlance', 'tempsMilis', 'Nproc'])

"""
df_filtered = df[df['Npoint'] == "12000000"]

print(df_filtered)
print(df['Npoint'].unique())

df_filtered['tempsMilis'] = df_filtered['tempsMilis'].astype(int)
df_filtered['Nproc'] = df_filtered['Nproc'].astype(int)


df_mean = df_filtered.groupby('Nproc')['tempsMilis'].mean().reset_index()
"""

"""
plt.figure(figsize=(10, 6))
plt.plot(df_mean['Nproc'], df_mean['tempsMilis'], marker='o', linestyle='-', color='b')

plt.xlabel('Nombre de processus (Nproc)')
plt.ylabel('Temps d\'exécution moyen (ms)')
plt.title('Scalabilité forte : Impact du nombre de processus sur le temps d\'exécution')
plt.grid(True)
plt.show()
"""

"""
sequential_time = df_mean['tempsMilis'].iloc[0]
df_mean['speedup'] = sequential_time / df_mean['tempsMilis']

plt.figure(figsize=(10, 6))
plt.plot(df_mean['Nproc'], df_mean['speedup'], marker='o', linestyle='-', color='r')


plt.plot([1, 12], [1, 12], '--b', label='Speedup idéal')
plt.legend()


plt.xlabel('Nombre de processus (Nproc)')
plt.ylabel('Speed-up')
plt.title('Speed-up en fonction du nombre de processus')
plt.grid(True)
plt.show()
"""

"""
df_fixed_proc = df[df['Nproc'] == "8"]

df_fixed_proc['tempsMilis'] = pd.to_numeric(df_fixed_proc['tempsMilis'])
df_fixed_proc['Npoint'] = pd.to_numeric(df_fixed_proc['Npoint'])

df_mean_points = df_fixed_proc.groupby('Npoint')['tempsMilis'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(df_mean_points['Npoint'], df_mean_points['tempsMilis'], marker='o', linestyle='-', color='b')

plt.xlabel('Nombre de points')
plt.ylabel('Temps d\'exécution moyen (ms)')
plt.title('Temps d\'exécution en fonction du nombre de points (Nproc = 8)')
plt.grid(True)
plt.show()
"""


df_fixed_proc = df[df['Nproc'] == "8"]

df_fixed_proc['tempsMilis'] = pd.to_numeric(df_fixed_proc['tempsMilis'])
df_fixed_proc['Npoint'] = pd.to_numeric(df_fixed_proc['Npoint'])

df_mean_points = df_fixed_proc.groupby('Npoint')['tempsMilis'].mean().reset_index()

sequential_time = df_mean_points['tempsMilis'].iloc[0]
df_mean_points['speedup'] = sequential_time / df_mean_points['tempsMilis']

plt.figure(figsize=(10, 6))
plt.plot(df_mean_points['Npoint'], df_mean_points['speedup'], marker='o', linestyle='-', color='r')


plt.plot([1, 12], [1, 12], '--b', label='Speedup idéal')
plt.legend()

plt.xlabel('Nombre de points')
plt.ylabel('Temps d\'exécution moyen (ms)')
plt.title('Temps d\'exécution en fonction du nombre de points (Nproc = 8)')
plt.grid(True)
plt.show()
