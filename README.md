# DeepLearn Amazon Sentiment Analysis

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Package Manager: UV](https://img.shields.io/badge/package%20manager-uv-6112a3.svg)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Plotly](https://img.shields.io/badge/Visualisation-Plotly-orange.svg)](https://plotly.com/)
[![Deep Learning: TensorFlow](https://img.shields.io/badge/Deep%20Learning-TensorFlow-FF6F00.svg)](https://wwww.tensorflow.org/)
[![Scikit-learn](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-F7931E.svg)](https://scikit-learn.org/)

Ce projet est une solution complète d'analyse de sentiment pour les avis Amazon, intégrant un dashboard ultra-moderne.

## Fonctionnalités

- **Dashboard Streamlit** : Interface avec **glassmorphism** pour le monitorage en temps réel de la précision et de l'impact des mots-clés.
- **Génération de Données** : Dataset de 10 000 avis avec répartition réaliste des sentiments.
- **EDA Interactive** : Analyse exploratoire approfondie avec des graphiques **Plotly**.
- **Modélisation Avancée** : Architecture **LSTM** pour la classification de texte.
- **Gestion Moderne** : Utilisation de **uv** pour une performance optimale.

## Structure du Projet

- `data/` : Contient `amazon_reviews.csv`.
- `notebooks/` :
  - `01_eda.ipynb` : Analyse visuelle et statistique.
  - `02_modeling.ipynb` : Architecture LSTM et évaluation.
- `dashboard.py` : Dashboard Streamlit moderne.
- `generate_data.py` : Script de génération des données.

## Installation

Le projet utilise [uv](https://github.com/astral-sh/uv).

1. **Cloner le projet** :

   ```bash
   git clone https://github.com/Franck-F/amazon-sentiment.git
   cd amazon-sentiment
   ```

2. **Synchroniser l'environnement** :

   ```bash
   uv sync
   ```

3. **Générer les données** :

   ```bash
   uv run generate_data.py
   ```

## Utilisation

### Dashboard Temps Réel

```bash
uv run streamlit run dashboard.py
```

### Notebooks

```bash
uv run jupyter notebook
```

Ouvrez `notebooks/01_eda.ipynb` ou `notebooks/02_modeling.ipynb`.

## Résultats

- Précision et perte en direct sur le dashboard.
- Impact des mots-clés sur la polarité des sentiments.
- Graphiques interactifs pour l'exploration des données.

---
Développé pour l'analyse de données Deep Learning.
