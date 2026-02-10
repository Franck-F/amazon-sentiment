# DeepLearn Amazon Sentiment Analysis

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Plotly](https://img.shields.io/badge/Visualisation-Plotly-orange.svg)](https://plotly.com/)
[![Deep Learning: TensorFlow](https://img.shields.io/badge/Deep%20Learning-TensorFlow-FF6F00.svg)](https://wwww.tensorflow.org/)

Ce projet vise à analyser les sentiments des commentaires Amazon à l'aide de techniques de Deep Learning.

## Structure du Projet

- `data/` : Contient le jeu de données généré (`amazon_reviews.csv`).
- `notebooks/` :
  - `01_eda.ipynb` : Analyse exploratoire des données avec Plotly.
  - `02_modeling.ipynb` : Construction et entraînement du modèle de sentiment (LSTM).
- `generate_data.py` : Script de génération des données synthétiques.

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/Franck-F/amazon-sentiment.git
   cd amazon-sentiment
   ```

2. Installez les dépendances :

   ```bash
   pip install pandas plotly numpy tensorflow scikit-learn
   ```

3. Générez les données :

   ```bash
   python generate_data.py
   ```

## Utilisation

Lancez les notebooks dans l'ordre pour explorer les données et entraîner le modèle. Les visualisations sont interactives grâce à Plotly.

## Résultats

Le modèle utilise une architecture LSTM pour capturer les nuances textuelles des avis Amazon et classer les sentiments en trois catégories : Positive, Neutre et Négative.
