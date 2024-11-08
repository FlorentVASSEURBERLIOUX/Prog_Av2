## Assignement102

Ce code calcul une valeur appromimative de PI à partir de la technique de Monte Carlo.

### Dépendences :

Le code dépends de l'API conccurent et en utilise les concepts :
- Executors : La classe Executors permet l'impémentation d'un système distribué de Master/Worker. Dans ce code, c'est la méthode Work-Stealing Pool de cette classe qui est utilisé.
- AtomicInteger : La classe AtomicInteger permet la création d'un entier protéger des risques engendrés par la ressource critique.
