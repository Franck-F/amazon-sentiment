# DeepLearn Amazon Sentiment Analysis

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Package Manager: UV](https://img.shields.io/badge/package%20manager-uv-6112a3.svg)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Plotly](https://img.shields.io/badge/Visualisation-Plotly-orange.svg)](https://plotly.com/)
[![Deep Learning: TensorFlow](https://img.shields.io/badge/Deep%20Learning-TensorFlow-FF6F00.svg)](https://wwww.tensorflow.org/)
[![Scikit-learn](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-F7931E.svg)](https://scikit-learn.org/)

Ce projet est une solution complète d'analyse de sentiment pour les avis Amazon, allant de la génération de données synthétiques représentatives à la modélisation par Deep Learning (LSTM), avec des visualisations interactives.

## Fonctionnalités

- **EDA Interactive** : Analyse exploratoire approfondie avec des graphiques **Plotly** (distribution des notes, sentiments par produit).
- **Modélisation Avancée** : Architecture de réseau de neurones récurrents (**LSTM**) pour la classification de texte.
- **Gestion Moderne** : Utilisation de **uv** pour une gestion des dépendances ultra-rapide et reproductible.

## Structure du Projet

- `data/` : Contient `amazon_reviews.csv` (10k reviews).
- `notebooks/` :
  - `01_eda.ipynb` : Analyse visuelle et statistique des données.
  - `02_modeling.ipynb` : Prétraitement, architecture LSTM et évaluation.
- `generate_data.py` : Script Python pour régénérer le dataset.
- `pyproject.toml` & `uv.lock` : Fichiers de configuration de l'environnement.

## Installation

Le projet utilise [uv](https://github.com/astral-sh/uv) pour la gestion des packages.

1. **Cloner le projet** :

   ```bash
   git clone https://github.com/Franck-F/amazon-sentiment.git
   cd amazon-sentiment
   ```

2. **Synchroniser l'environnement** :

   ```bash
   uv sync
   ```

## Utilisation

Pour lancer les notebooks dans un environnement isolé :

```bash
uv run jupyter notebook
```

Ouvrez ensuite `notebooks/01_eda.ipynb` pour l'analyse ou `notebooks/02_modeling.ipynb` pour l'entraînement.

## Résultats

Les visualisations Plotly permettent de suivre en temps réel :

- La précision (Accuracy) et la perte (Loss) durant l'entraînement.
- La répartition des sentiments pour chaque catégorie de produits.
- L'impact des mots-clés sur la classification.
