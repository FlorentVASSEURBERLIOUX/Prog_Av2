import pandas as pd
import matplotlib.pyplot as plt

file_path = 'U:/Prog. Av/Projet/Prog_Av2/tests/pi.txt'
df = pd.read_csv(file_path, sep=';', header=None, names=['Error', 'Npoint', 'Pi', 'Nlance', 'tempsMilis', 'Nproc'])


def faible_speedup():
    df_filtered = df[df['Npoint'] != "12000000"]
    df_filtered['tempsMilis'] = df_filtered['tempsMilis'].astype(int)
    df_filtered['Nproc'] = df_filtered['Nproc'].astype(int)

    df_mean = df_filtered.groupby('Nproc')['tempsMilis'].mean().reset_index()

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



def forte_speedup():
    df_filtered = df[df['Npoint'] == "12000000"]

    df_filtered['tempsMilis'] = df_filtered['tempsMilis'].astype(int)
    df_filtered['Nproc'] = df_filtered['Nproc'].astype(int)

    df_mean = df_filtered.groupby('Nproc')['tempsMilis'].mean().reset_index()

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


def forte():
    df_filtered = df[df['Npoint'] == "12000000"]

    df_filtered['tempsMilis'] = df_filtered['tempsMilis'].astype(int)
    df_filtered['Nproc'] = df_filtered['Nproc'].astype(int)

    df_mean = df_filtered.groupby('Nproc')['tempsMilis'].mean().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(df_mean['Nproc'], df_mean['tempsMilis'], marker='o', linestyle='-', color='b')

    plt.xlabel('Nombre de processus (Nproc)')
    plt.ylabel('Temps d\'exécution moyen (ms)')
    plt.title('Scalabilité forte : Impact du nombre de processus sur le temps d\'exécution')
    plt.grid(True)
    plt.show()

def faible():
    df_filtered = df[df['Npoint'] != "12000000"]

    df_filtered['tempsMilis'] = df_filtered['tempsMilis'].astype(int)
    df_filtered['Nproc'] = df_filtered['Nproc'].astype(int)

    df_mean = df_filtered.groupby('Nproc')['tempsMilis'].mean().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(df_mean['Nproc'], df_mean['tempsMilis'], marker='o', linestyle='-', color='b')

    plt.xlabel('Nombre de processus (Nproc)')
    plt.ylabel('Temps d\'exécution moyen (ms)')
    plt.title('Scalabilité forte : Impact du nombre de processus sur le temps d\'exécution')
    plt.grid(True)
    plt.show()


forte()