# 🪨📄✂️ Rock-Paper-Scissors — Mini Python Game

Un petit jeu Pierre-Feuille-Ciseaux développé en Python pour t’entraîner à la logique, aux fonctions et à la structure d’un mini-projet.
Le joueur affronte l’ordinateur, et peut rejouer autant de fois qu’il le souhaite !

## 🎯 Objectifs du projet

- Apprendre à structurer un mini-projet Python (main.py, game.py, utils.py)
- Gérer les entrées utilisateur
- Générer un choix aléatoire pour l'ordinateur
- Déterminer un gagnant selon les règles du jeu
- Implémenter une boucle permettant de rejouer automatiquement

## 🕹️ Comment jouer ?

#### Lance le script principal :

```bash
python main.py
```

#### Choisis ton coup :

```bash
Enter your move (rock, paper, scissors):
```

#### L’ordinateur joue à son tour et le résultat s’affiche :

```bash
Computer chose: paper
You win!
```

#### Le jeu te demande :

```bash
Do you want to play again? (y/n):
```

👉 Tape y pour rejouer
👉 Tape n pour quitter

## 📂 Structure du projet
.
├── main.py        # Point d'entrée du jeu
├── game.py        # Logique du jeu
└── utils.py       # Fonctions utilitaires


**main.py** → gère la boucle principale et relance le jeu

**game.py** → contient la logique : entrée user, coup ordi, gagnant

**utils.py** → vérifications et gestion du “play again”

## 🧑‍💻 Technologies

Python 3