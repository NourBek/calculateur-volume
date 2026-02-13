import streamlit as st

# Configuration
st.set_page_config(page_title="Volume Pro", page_icon="🏠", layout="centered")

# --- DESIGN ULTRA-PREMIUM (CSS) ---
st.markdown("""
    <style>
    /* Fond dégradé élégant */
    .stApp {
        background: linear-gradient(135deg, #1e1e26 0%, #111115 100%);
    }
    
    /* Carte principale pour les champs */
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }

    /* Style des textes */
    h1 {
        background: linear-gradient(90deg, #3498db, #58D68D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 32px !important;
        padding-bottom: 20px;
    }

    /* Bouton "Néon" arrondi */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 60px;
        background: linear-gradient(90deg, #3498db, #2980b9);
        color: white;
        font-size: 20px !important;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(52, 152, 219, 0.4);
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        box-shadow: 0 6px 20px rgba(52, 152, 219, 0.6);
        transform: translateY(-2px);
    }

    /* Boîte de résultat stylisée */
    .result-container {
        background: rgba(88, 214, 141, 0.1);
        border: 2px solid #58D68D;
        border-radius: 30px;
        padding: 40px;
        text-align: center;
        animation: fadeIn 0.5s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

# --- INTERFACE ---
st.markdown("<h1>🏠 Volume Master Pro</h1>", unsafe_allow_html=True)

# Début de la carte de saisie
st.markdown('<div class="main-card">', unsafe_allow_html=True)

L = st.number_input("📏 Longueur (m)", min_value=0.0, format="%.2f", key="L")
l = st.number_input("↔️ Largeur (m)", min_value=0.0, format="%.2f", key="l")
h = st.number_input("⬆️ Hauteur (m)", min_value=0.0, format="%.2f", key="h")

st.markdown('</div>', unsafe_allow_html=True)

# Bouton de calcul
if st.button("CALCULER LE VOLUME"):
    if L > 0 and l > 0 and h > 0:
        volume = L * l * h
        st.markdown(f"""
            <div class="result-container">
                <p style="color: #58D68D; font-size: 18px; font-weight: bold; text-transform: uppercase;">Volume Total</p>
                <h1 style="background: none; -webkit-text-fill-color: #58D68D; font-size: 65px !important; margin: 0;">{volume:.2f} m³</h1>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Veuillez saisir toutes les mesures.")

# Bas de page
st.markdown("<p style='text-align: center; color: #555; margin-top: 50px;'>Propulsé par Python & Streamlit</p>", unsafe_allow_html=True)
