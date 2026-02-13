import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Volume Pro", page_icon="🏠", layout="centered")

# --- DESIGN PERSONNALISÉ (CSS) ---
st.markdown("""
    <style>
    /* Fond de la page */
    .stApp {
        background-color: #1E1E26;
    }
    
    /* Titre principal */
    h1 {
        color: #3498db;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-weight: bold;
    }

    /* Style des boîtes de saisie */
    .stNumberInput div div input {
        border-radius: 15px !important;
        border: 2px solid #3498db !important;
        background-color: #2c2c36 !important;
        color: white !important;
    }

    /* Bouton Calculer (Effet Pilule) */
    .stButton>button {
        width: 100%;
        border-radius: 30px;
        height: 55px;
        background-color: #3498db;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
        margin-top: 20px;
    }
    
    .stButton>button:hover {
        background-color: #2980b9;
        transform: scale(1.02);
    }

    /* Zone du résultat */
    .result-box {
        background-color: #2c2c36;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-top: 20px;
        border: 1px solid #58D68D;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENU DE L'APPLI ---
st.markdown("<h1>🏠 Calculateur de Volume</h1>", unsafe_allow_html=True)

# Utilisation de colonnes pour une meilleure disposition
col1, col2, col3 = st.columns(3)

with col1:
    L = st.number_input("Longueur (m)", min_value=0.0, format="%.2f")
with col2:
    l = st.number_input("Largeur (m)", min_value=0.0, format="%.2f")
with col3:
    h = st.number_input("Hauteur (m)", min_value=0.0, format="%.2f")

# Centrage du bouton
if st.button("CALCULER MAINTENANT"):
    if L > 0 and l > 0 and h > 0:
        volume = L * l * h
        st.markdown(f"""
            <div class="result-box">
                <p style="color: #bdc3c7; margin-bottom: 5px;">Résultat final</p>
                <h1 style="color: #58D68D; font-size: 50px; margin: 0;">{volume:.2f} m³</h1>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Veuillez remplir toutes les dimensions.")

# Espace en bas
st.write("")
st.write("")
