# Pièges ! (Stay Alive!)

Projet de jeu de stratégie multi-joueur « Pièges ! » (Stay Alive!)  
Développé en Python dans le cadre du TP/DM sur les interfaces texte et graphique.


## Gameplay

![Placement des billes par les deux joueurs](docs/screenshots/marble-placement.png)

![Manipulation des tirettes pendant une partie](docs/screenshots/sliding-bars.png)

Captures de la fenêtre du jeu après placement des billes et manipulation des tirettes par les commandes de l’interface.

##  Objectif

- **V1 (Terminal)** : version solo, calcul de coups pour éliminer toutes les billes.
- **V2 (Graphique)** : version multi-joueur complète, interface graphique via le module FLTK.

##  Structure du dépôt

```
.
├── game.py                 # Moteur du jeu (structures et logique)
├── piege.py                # Interface graphique et boucle principale (FLTK)
├── fltk.py                 # Wrapper FLTK pour dessin et gestion d’événements
├── rapport Vincent Plessy Pieges!.pdf    # Rapport de projet détaillé
└── Sujet.pdf               # Énoncé du projet
```

## ⚙ Prérequis

- Python 3.8+
- tkinter (généralement fourni avec Python)
- PIL/Pillow (pour gestion avancée des images)

```bash
pip install pillow
```

##  Installation & Lancement

1. **Cloner** ou **télécharger** ce dépôt.
2. Installer les dépendances :

   ```bash
   pip install pillow
   ```

3. Lancer l’interface graphique :

   ```bash
   python3 piege.py
   ```

   Les joueurs placent d’abord leurs billes. Pendant la phase des tirettes, le clic gauche tire et le clic droit pousse. Le dernier joueur à conserver une bille gagne.

`game.py` contient les structures et règles utilisées par l’interface ; son exécution seule ne lance pas une partie interactive.

##  Documentation & Rapport

Consultez **`rapport Vincent Plessy Pieges!.pdf`** pour :
- Règles détaillées
- Architecture du code
- Tests et résultats
- Améliorations possibles

## 🛠 Développement

- Le module **`fltk.py`** gère la création de la fenêtre, le dessin des formes et la gestion des événements (clics, touches).
- **`game.py`** définit :
  - `Plateau` : position des billes et des tirettes
  - `Tirette` : déplacement et gestion des trous
  - `Joueur`   : placement et gestion des billes
- **`piege.py`** orchestre le jeu (placement/phase tirettes) et crée l’interface utilisateur.

##  Contribution

Les modifications sont bienvenues !  
Forkez le dépôt, apportez vos améliorations et proposez une Pull Request.

##  Licence

Le dépôt ne contient pas de fichier de licence explicite.

---

**Auteur** : Vincent Plessy  
Étudiant L2 Informatique – Année 2024–2025
