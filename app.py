import streamlit as st
import urllib.parse

# Configuration
st.set_page_config(page_title="Volume Master", page_icon="🏠")

# Initialisation de l'historique (mémoire de l'appli)
if "historique" not in st.session_state:
    st.session_state.historique = []

# --- DESIGN CSS ---
st.markdown("""
    <style>
    .stApp { background: #121212; }
    h1 { background: linear-gradient(90deg, #00C9FF, #92FE9D); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; }
    .whatsapp-btn {
        display: inline-block; background-color: #25D366; color: white !important;
        padding: 15px; border-radius: 50px; text-decoration: none;
        font-weight: bold; text-align: center; width: 100%; margin-top: 10px;
    }
    .histo-card {
        background: rgba(255, 255, 255, 0.05); padding: 10px;
        border-radius: 10px; margin-top: 5px; border-left: 5px solid #3498db;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🏠 Volume Master Pro</h1>", unsafe_allow_html=True)

# Saisie
L = st.number_input("📏 Longueur (m)", min_value=0.0, format="%.2f")
l = st.number_input("↔️ Largeur (m)", min_value=0.0, format="%.2f")
h = st.number_input("⬆️ Hauteur (m)", min_value=0.0, format="%.2f")

if st.button("🚀 CALCULER LE VOLUME"):
    if L > 0 and l > 0 and h > 0:
        volume = L * l * h
        
        # --- ANIMATION ---
        st.balloons() 
        
        # Ajouter à l'historique (on garde les 5 derniers)
        st.session_state.historique.insert(0, f"{L}x{l}x{h} = {volume:.2f} m³")
        st.session_state.historique = st.session_state.historique[:5]
        
        # Affichage résultat
        st.markdown(f"""
            <div style="background: rgba(146, 254, 157, 0.1); border: 2px solid #92FE9D; border-radius: 20px; padding: 20px; text-align: center;">
                <h1 style="background: none; -webkit-text-fill-color: #92FE9D; font-size: 50px !important;">{volume:.2f} m³</h1>
            </div>
            """, unsafe_allow_html=True)
        
        # Partage WhatsApp
        msg = urllib.parse.quote(f"Volume calculé : {volume:.2f} m³ 🏠")
        st.markdown(f'<a href="https://wa.me{msg}" target="_blank" class="whatsapp-btn">📲 Partager sur WhatsApp</a>', unsafe_allow_html=True)
    else:
        st.error("Veuillez remplir tous les champs.")

# --- SECTION HISTORIQUE ---
if st.session_state.historique:
    st.write("---")
    st.subheader("📜 Derniers calculs")
    for item in st.session_state.historique:
        st.markdown(f'<div class="histo-card">{item}</div>', unsafe_allow_html=True)
