Florent VASSEUR--BERLIOUX
INF-FI3

<div align="center">
<img height="95" width="400" src="img/IUT_Velizy_Villacoublay_logo_2020_ecran.png" title="logo uvsq vélizy"/>

# Prog. Avancée - Compte rendu

</div>

Le document suivant est un résumé du cours de Programmation Avancée, illustrée par les exemples du TP.
Ce rapport expliquera aussi les choix effectuer dans les TP.

---

<br><br><br>

## Technique de Monte Carlo



<br>

## Assignement102

Ce code calcul une valeur appromimative de PI à partir de la technique de Monte Carlo.

<br>

### Dépendences :

Le code dépends de l'API conccurent et en utilise les concepts :
- Executors : La classe Executors permet l'impémentation d'un système distribué. Dans ce code, c'est la méthode Work-Stealing Pool de cette classe qui est utilisé. L'Executor a une collection de thread et une collection de tâches, il associe ces threads et tâches ensemble pour gérer l'exécution des tâches.
- AtomicInteger : La classe AtomicInteger permet la création d'un entier protéger des risques engendrés par la ressource critique. Cette classe permet d'éviter d'avoir à utilisé un zone `synchronized`.

<br>

**NOTE :** Utilisation d'Executor.
```java
new Tread(new RunnableTask()).start();
```
On substitue alors les threads par un Executor :
```java
Executor executor = myExecutor;
executor.execute(new RunnableTask1());
executor.execute(new RunnableTask2());
```
<br>

### Algorithme :

Assignement102 est un programme de paradigyme dit "d'itération parrallèle" ou encore de "parralélisme de boucles".
Il s'agit d'un algorithme parallèle calculant Pi à partir de la technique de Monte Carlo.



<br>

## Pi

Ce code calcul une valeur appromimative de PI à partir de la technique de Monte Carlo.

<br>

### Dépendences :

Le code dépends de l'API conccurent et en utilise les concepts :
- Executors : La classe Executors permet l'impémentation d'un système distribué. Dans ce code, c'est la méthode Work-Stealing Pool de cette classe qui est utilisé. L'Executor a une collection de thread et une collection de tâches, il associe ces threads et tâches ensemble pour gérer l'exécution des tâches.
- Future : La classe Future permet de représenter le résultat d'un calcul asynchrone. Cette classe est constituée des méthode isDone et get, permettant respectivement de vérifier si le calcul est fini, et de réccupérer le résultat du calcul.

<br>

### Algorithme :

Assignement102 est un programme de paradigyme dit "Master/Worker". Les tâches sont segmentées par le Master entre les différents Worker.
Il s'agit d'un algorithme parallèle calculant Pi à partir de la technique de Monte Carlo.


<br>

## Envoi de messages

Uns socket est un fichier contenant des informations. Il s'agit d'un paquet d'octets avec des informations sur la source et le destinataire d'une donnée.

On se base sur le code distributedMC_step1_javaSocket présent dans le fichier src2.
On exécute le code en attribuant des numéros de ports à chaque Worker, puis on execute le Master en lui indiquant les ports des Workers.

On peut exécuter ce code en ligne de dommande dans le terminal :

**D'abord on compile avec javac.**
```bash
javac WorkerSocket.java
```


```bash
javac MasterSocket.java
```

**Ensuite on exécute en plaçant les arguments dans l'appel.**

```bash
java WorkerSocket 25545
```

```bash
java MasterSocket
```

Le programme n'est pas complet, il faut donc lui ajouté la partie du calcul de MonteCarlo.
Dans le fichier WorkerSocket, on peut donc ajouter le code du programme Pi.java :

```java
long circleCount = 0;
Random prng = new Random();
for (int j = 0; j < parseInt(str); j++)
{
    double x = prng.nextDouble();
    double y = prng.nextDouble();
    if ((x * x + y * y) < 1)  ++circleCount;
}
pWrite.println(""+circleCount);
```

On utilise pWrite pour écrire le résultat calculé par le Worker dans la Socket.
Ainsi, le Master reçoit les informations et peut calculer le résultat final.
 

<br>

## Test des temps d'exécutions

