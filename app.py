import streamlit as st

# Configuration de la page (Design Sombre par défaut)
st.set_page_config(page_title="Calculateur Volume Pro", page_icon="🏠")

# CSS pour les boutons arrondis et le style
st.markdown("""
    <style>
    .stButton>button {
        border-radius: 25px;
        height: 3em;
        width: 100%;
        background-color: #3498db;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #2980b9;
        border: none;
    }
    div[data-baseweb="input"] {
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏠 Calculateur de Volume")

# Saisie des données
L = st.number_input("Longueur (m)", min_value=0.0, step=0.1)
l = st.number_input("Largeur (m)", min_value=0.0, step=0.1)
h = st.number_input("Hauteur (m)", min_value=0.0, step=0.1)

if st.button("CALCULER"):
    if L > 0 and l > 0 and h > 0:
        volume = L * l * h
        st.markdown(f"<h1 style='text-align: center; color: #58D68D;'>{volume:.2f} m³</h1>", unsafe_allow_html=True)
    else:
        st.error("Veuillez entrer des dimensions valides.")

st.info("Astuce : Sur mobile, ce site s'adapte automatiquement à votre écran !")
