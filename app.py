import streamlit as st
from streamlit_confetti import confetti
import urllib.parse

# Configuration
st.set_page_config(page_title="Volume Master", page_icon="🏠")

# --- DESIGN CSS AVANCÉ ---
st.markdown("""
    <style>
    .stApp { background: #121212; }
    h1 { background: linear-gradient(90deg, #00C9FF, #92FE9D); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; }
    
    /* Bouton WhatsApp Vert */
    .whatsapp-btn {
        display: inline-block;
        background-color: #25D366;
        color: white !important;
        padding: 15px 25px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        width: 100%;
        margin-top: 10px;
        box-shadow: 0 4px 10px rgba(37, 211, 102, 0.3);
    }
    
    .main-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🏠 Volume Master Pro</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    L = st.number_input("📏 Longueur (m)", min_value=0.0, format="%.2f")
    l = st.number_input("↔️ Largeur (m)", min_value=0.0, format="%.2f")
    h = st.number_input("⬆️ Hauteur (m)", min_value=0.0, format="%.2f")
    st.markdown('</div>', unsafe_allow_html=True)

if st.button("🚀 CALCULER LE VOLUME"):
    if L > 0 and l > 0 and h > 0:
        volume = L * l * h
        confetti() # Animation de fête !
        
        # Affichage du résultat
        st.markdown(f"""
            <div style="background: rgba(146, 254, 157, 0.1); border: 2px solid #92FE9D; border-radius: 20px; padding: 20px; text-align: center; margin-top: 20px;">
                <p style="color: #92FE9D; margin: 0;">RÉSULTAT</p>
                <h1 style="background: none; -webkit-text-fill-color: #92FE9D; font-size: 50px !important;">{volume:.2f} m³</h1>
            </div>
            """, unsafe_allow_html=True)
        
        # --- BOUTON WHATSAPP ---
        message = f"Salut ! Le volume calculé pour ma maison est de {volume:.2f} m³. 🏠"
        msg_encode = urllib.parse.quote(message)
        whatsapp_url = f"https://wa.me{msg_encode}"
        
        st.markdown(f'<a href="{whatsapp_url}" target="_blank" class="whatsapp-btn">📲 Partager sur WhatsApp</a>', unsafe_allow_html=True)
    else:
        st.warning("Complétez les mesures pour continuer.")

st.caption("<p style='text-align: center;'>Version 2.0 - Design Mobile Optimisé</p>", unsafe_allow_html=True)
