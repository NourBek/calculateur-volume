import streamlit as st
import urllib.parse
from streamlit.components.v1 import html

# Configuration
st.set_page_config(page_title="Volume Master", page_icon="🏠")

# Initialisation de la session (Historique et Compteur pour vider les champs)
if "historique" not in st.session_state:
    st.session_state.historique = []
if "compteur_reset" not in st.session_state:
    st.session_state.compteur_reset = 0

# --- SCRIPT JAVASCRIPT (Navigation Entrée + Auto-Focus) ---
js_nav = """
<script>
    const inputs = window.parent.document.querySelectorAll('input[type="number"]');
    inputs.forEach((input, index) => {
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                const next = inputs[index + 1];
                if (next) {
                    next.focus();
                } else {
                    const btn = window.parent.document.querySelector('button[kind="primary"]');
                    if (btn) btn.click();
                }
            }
        });
    });
    // Focus sur le premier champ au chargement
    if(inputs[0]) inputs[0].focus();
</script>
"""

# --- DESIGN CSS ---
st.markdown("""
    <style>
    .stApp { background: #121212; }
    h1 { background: linear-gradient(90deg, #00C9FF, #92FE9D); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; }
    .whatsapp-btn {
        display: inline-block; background-color: #25D366; color: white !important;
        padding: 15px; border-radius: 50px; text-decoration: none;
        font-weight: bold; text-align: center; width: 100%; margin-top: 15px;
    }
    .histo-card {
        background: rgba(255, 255, 255, 0.05); padding: 12px;
        border-radius: 12px; margin-top: 8px; border-left: 5px solid #3498db; color: #ecf0f1;
    }
    div[data-baseweb="input"] { border-radius: 15px !important; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

html(js_nav, height=0)

st.markdown("<h1>🏠 Volume Master Pro</h1>", unsafe_allow_html=True)

# --- CHAMPS DE SAISIE (Utilisation du compteur pour le Reset) ---
c = st.session_state.compteur_reset
L = st.number_input("📏 Longueur (m)", min_value=0.0, format="%.2f", key=f"L_{c}")
l = st.number_input("↔️ Largeur (m)", min_value=0.0, format="%.2f", key=f"l_{c}")
h = st.number_input("⬆️ Hauteur (m)", min_value=0.0, format="%.2f", key=f"h_{c}")

if st.button("🚀 CALCULER ET VIDER", type="primary"):
    if L > 0 and l > 0 and h > 0:
        volume = float(L) * float(l) * float(h)
        st.balloons() 
        
        # Sauvegarde résultat temporaire pour l'affichage avant le reset
        st.session_state.dernier_vol = volume
        
        # Mise à jour historique
        st.session_state.historique.insert(0, f"{L}m x {l}m x {h}m = {volume:.2f} m³")
        st.session_state.historique = st.session_state.historique[:5]
        
        # INCORPORER LE RESET : On change le compteur pour vider les champs
        st.session_state.compteur_reset += 1
        st.rerun() # Relance l'app pour appliquer le vidage
    else:
        st.error("⚠️ Saisie incomplète.")

# --- AFFICHAGE DU RÉSULTAT APRÈS RELANCE ---
if "dernier_vol" in st.session_state:
    vol = st.session_state.dernier_vol
    st.markdown(f"""
        <div style="background: rgba(146, 254, 157, 0.1); border: 2px solid #92FE9D; border-radius: 20px; padding: 25px; text-align: center; margin-top: 10px;">
            <p style="color: #92FE9D; margin: 0; font-weight: bold;">RÉSULTAT DU CALCUL</p>
            <h1 style="background: none; -webkit-text-fill-color: #92FE9D; font-size: 55px !important; margin: 0;">{vol:.2f} m³</h1>
        </div>
        """, unsafe_allow_html=True)
    
    # Bouton WhatsApp
    msg = urllib.parse.quote(f"Volume calculé : {vol:.2f} m³ 🏠")
    st.markdown(f'<a href="https://wa.me{msg}" target="_blank" class="whatsapp-btn">📲 Partager sur WhatsApp</a>', unsafe_allow_html=True)

# --- HISTORIQUE ---
if st.session_state.historique:
    st.write("")
    st.subheader("📜 Historique récent")
    for item in st.session_state.historique:
        st.markdown(f'<div class="histo-card">{item}</div>', unsafe_allow_html=True)
