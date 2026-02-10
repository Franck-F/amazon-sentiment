import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
import random

# Configuration de la page
st.set_page_config(
    page_title="Amazon Sentiment Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS pour le Glassmorphism
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

    * {
        font-family: 'Outfit', sans-serif;
    }

    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: white;
    }

    /* Glassmorphism card */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 25px;
    }

    h1, h2, h3 {
        color: #6366f1 !important;
        font-weight: 600 !important;
    }

    .stMetric {
        background: rgba(255, 255, 255, 0.03);
        padding: 15px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    /* Animation pour le gradient */
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    """, unsafe_allow_html=True)

# Barre latérale
with st.sidebar:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.title("Configuration")
    model_version = st.selectbox("Version du Modèle", ["LSTM v1.0", "BERT v0.8 (Alpha)"])
    update_speed = st.slider("Vitesse de rafraîchissement (s)", 0.5, 5.0, 1.0)
    st.markdown("</div>", unsafe_allow_html=True)

# En-tête principal
st.markdown("<h1 style='text-align: center; font-size: 3rem;'>Amazon Sentiment Analysis</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: rgba(255,255,255,0.7);'>Monitorage en temps réel et analyse de polarité</p>", unsafe_allow_html=True)

# Layout principal
col1, col2, col3 = st.columns(3)

accuracy_metric = col1.metric("Précision (Live)", "0.00%", "0.00%")
loss_metric = col2.metric("Perte (Live)", "0.000", "0.000")
data_processed = col3.metric("Samples Traités", "0", "+0")

# Conteneurs pour les graphiques
chart_col1, chart_col2 = st.columns([2, 1])

with chart_col1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("Performance du modèle en temps réel")
    chart_placeholder = st.empty()
    st.markdown("</div>", unsafe_allow_html=True)

with chart_col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("Impact des Mots-Clés")
    impact_placeholder = st.empty()
    st.markdown("</div>", unsafe_allow_html=True)

# Simulation de données en temps réel
if 'acc_history' not in st.session_state:
    st.session_state.acc_history = []
    st.session_state.loss_history = []
    st.session_state.keywords_impact = {
        "excellent": 0, "parfait": 0, "déçu": 0, "médiocre": 0, "rapide": 0,
        "qualité": 0, "cher": 0, "recommande": 0, "panne": 0, "super": 0
    }

# Boucle de simulation
# Note: Dans un cas réel, on lirait les logs d'entraînement ou une API
for i in range(20):
    new_acc = min(0.95, 0.7 + i * 0.01 + random.uniform(-0.01, 0.01))
    new_loss = max(0.1, 0.5 - i * 0.02 + random.uniform(-0.02, 0.02))
    
    st.session_state.acc_history.append(new_acc)
    st.session_state.loss_history.append(new_loss)
    
    # Mise à jour aléatoire de l'impact des mots-clés
    for k in st.session_state.keywords_impact:
        st.session_state.keywords_impact[k] += random.uniform(-1, 1) if k in ["déçu", "médiocre", "panne", "cher"] else random.uniform(0, 2)

    # Mise à jour des métriques
    accuracy_metric.metric("Précision (Live)", f"{new_acc:.2%}", f"{(new_acc - st.session_state.acc_history[-2] if len(st.session_state.acc_history)>1 else 0):.2%}")
    loss_metric.metric("Perte (Live)", f"{new_loss:.4f}", f"{(new_loss - st.session_state.loss_history[-2] if len(st.session_state.loss_history)>1 else 0):.4f}", delta_color="inverse")
    data_processed.metric("Samples Traités", f"{1000 + i*500}", "+500")

    # Graphique de performance
    df_perf = pd.DataFrame({
        "Etape": range(len(st.session_state.acc_history)),
        "Précision": st.session_state.acc_history,
        "Perte": st.session_state.loss_history
    })
    
    fig_perf = go.Figure()
    fig_perf.add_trace(go.Scatter(x=df_perf["Etape"], y=df_perf["Précision"], name="Précision", line=dict(color='#6366f1', width=3)))
    fig_perf.add_trace(go.Scatter(x=df_perf["Etape"], y=df_perf["Perte"], name="Perte", line=dict(color='#f43f5e', width=3, dash='dot')))
    fig_perf.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    chart_placeholder.plotly_chart(fig_perf, use_container_width=True)

    # Graphique d'impact des mots-clés
    kw_data = pd.DataFrame({
        "Mot-Clé": list(st.session_state.keywords_impact.keys()),
        "Score d'Impact": list(st.session_state.keywords_impact.values())
    }).sort_values("Score d'Impact")
    
    fig_impact = px.bar(kw_data, y="Mot-Clé", x="Score d'Impact", orientation='h',
                        color="Score d'Impact", color_continuous_scale="RdYlGn")
    fig_impact.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        margin=dict(l=0, r=0, t=0, b=0),
        coloraxis_showscale=False,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
    impact_placeholder.plotly_chart(fig_impact, use_container_width=True)

    time.sleep(update_speed)

st.markdown("<p style='text-align: center; font-size: 0.8rem; color: rgba(255,255,255,0.3);'>Amazon Sentiment DeepLearn Project - Powered by Streamlit & UV</p>", unsafe_allow_html=True)
