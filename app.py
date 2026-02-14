import streamlit as st
import urllib.parse
from streamlit.components.v1 import html

# Configuration
st.set_page_config(page_title="Volume Master", page_icon="🏠")

# Initialisation
if "historique" not in st.session_state:
    st.session_state.historique = []
if "dernier_vol" not in st.session_state:
    st.session_state.dernier_vol = None

# --- DESIGN CSS ---
st.markdown("""
    <style>
    .stApp { background: #121212; }
    h1 { background: linear-gradient(90deg, #00C9FF, #92FE9D); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: bold; }
    div[data-baseweb="input"] { border-radius: 15px !important; background-color: #1e1e1e !important; }
    input { color: white !important; }
    .stButton>button { width: 100%; border-radius: 50px; background: linear-gradient(90deg, #3498db, #2980b9); color: white; font-weight: bold; border: none; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

# --- SCRIPT JAVASCRIPT CORRIGÉ ---
# Ce script force le passage au champ suivant SANS valider le formulaire
js_fix = """
<script>
    setTimeout(() => {
        const inputs = window.parent.document.querySelectorAll('input[type="number"]');
        inputs.forEach((input, index) => {
            input.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault(); // Empêche la validation du formulaire
                    const next = inputs[index + 1];
                    if (next) {
                        next.focus(); // Passe au suivant
                    } else {
                        // Si c'est le dernier, on clique sur le bouton
                        const btn = window.parent.document.querySelector('button[kind="primary"]');
                        if (btn) btn.click();
                    }
                }
            });
        });
    }, 500); // Petit délai pour laisser Streamlit charger les éléments
</script>
"""
html(js_fix, height=0)

st.markdown("<h1>🏠 Volume Master Pro</h1>", unsafe_allow_html=True)

# --- UTILISATION SANS FORM (Pour éviter la validation précoce) ---
# On utilise des colonnes pour un look sympa
L = st.number_input("📏 Longueur (m)", min_value=0.0, format="%.2f", value=None, placeholder="Ex: 10.5", key="L")
l = st.number_input("↔️ Largeur (m)", min_value=0.0, format="%.2f", value=None, placeholder="Ex: 8.0", key="l")
h = st.number_input("⬆️ Hauteur (m)", min_value=0.0, format="%.2f", value=None, placeholder="Ex: 2.5", key="h")

# Le bouton doit être de type "primary" pour être reconnu par le script JS
if st.button("🚀 CALCULER LE VOLUME", type="primary"):
    if L and l and h:
        volume = float(L) * float(l) * float(h)
        st.session_state.dernier_vol = volume
        st.session_state.historique.insert(0, f"{L}m x {l}m x {h}m = {volume:.2f} m³")
        st.session_state.historique = st.session_state.historique[:5]
        st.balloons()
    else:
        st.error("⚠️ Veuillez remplir tous les champs.")

# --- AFFICHAGE RÉSULTAT ---
if st.session_state.dernier_vol:
    vol = st.session_state.dernier_vol
    st.markdown(f"""
        <div style="background: rgba(146, 254, 157, 0.1); border: 2px solid #92FE9D; border-radius: 20px; padding: 20px; text-align: center; margin-top: 10px;">
            <h1 style="background: none; -webkit-text-fill-color: #92FE9D; font-size: 45px !important; margin: 0;">{vol:.2f} m³</h1>
        </div>
        """, unsafe_allow_html=True)
    
    msg = urllib.parse.quote(f"Volume : {vol:.2f} m³ 🏠")
    st.markdown(f'<a href="https://wa.me{msg}" target="_blank" style="display: block; background-color: #25D366; color: white; text-align: center; padding: 15px; border-radius: 50px; text-decoration: none; font-weight: bold; margin-top: 10px;">📲 Partager</a>', unsafe_allow_html=True)

# --- HISTORIQUE ---
if st.session_state.historique:
    st.write("---")
    st.subheader("📜 Historique")
    for item in st.session_state.historique:
        st.info(item)
