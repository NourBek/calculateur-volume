import streamlit as st
import urllib.parse

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
    .stNumberInput label { color: #ecf0f1 !important; }
    div[data-baseweb="input"] { border-radius: 15px !important; background-color: #1e1e1e !important; }
    input { color: white !important; }
    /* Style du bouton */
    .stButton>button {
        width: 100%; border-radius: 50px; height: 3em;
        background: linear-gradient(90deg, #3498db, #2980b9);
        color: white; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🏠 Volume Master Pro</h1>", unsafe_allow_html=True)

# --- FORMULAIRE (Gère nativement la touche Entrée) ---
# clear_on_submit=True vide les champs automatiquement après le clic
with st.form("calcul_form", clear_on_submit=True):
    st.write("Entrez les dimensions :")
    # value=None permet d'afficher un champ vide au lieu de 0.0 sur les navigateurs modernes
    L = st.number_input("📏 Longueur (m)", min_value=0.0, format="%.2f", value=None, placeholder="Ex: 10.5")
    l = st.number_input("↔️ Largeur (m)", min_value=0.0, format="%.2f", value=None, placeholder="Ex: 8.0")
    h = st.number_input("⬆️ Hauteur (m)", min_value=0.0, format="%.2f", value=None, placeholder="Ex: 2.5")
    
    submit = st.form_submit_button("🚀 CALCULER LE VOLUME")

if submit:
    if L and l and h:
        volume = float(L) * float(l) * float(h)
        st.session_state.dernier_vol = volume
        st.session_state.historique.insert(0, f"{L}m x {l}m x {h}m = {volume:.2f} m³")
        st.session_state.historique = st.session_state.historique[:5]
        st.balloons()
    else:
        st.error("⚠️ Veuillez remplir tous les champs avant de valider.")

# --- AFFICHAGE RÉSULTAT ---
if st.session_state.dernier_vol is not None:
    vol = st.session_state.dernier_vol
    st.markdown(f"""
        <div style="background: rgba(146, 254, 157, 0.1); border: 2px solid #92FE9D; border-radius: 20px; padding: 20px; text-align: center; margin-top: 10px;">
            <h1 style="background: none; -webkit-text-fill-color: #92FE9D; font-size: 45px !important; margin: 0;">{vol:.2f} m³</h1>
        </div>
        """, unsafe_allow_html=True)
    
    # WhatsApp
    msg = urllib.parse.quote(f"Volume calculé : {vol:.2f} m³ 🏠")
    st.markdown(f'''<a href="https://wa.me{msg}" target="_blank" 
        style="display: block; background-color: #25D366; color: white; text-align: center; 
        padding: 15px; border-radius: 50px; text-decoration: none; font-weight: bold; margin-top: 10px;">
        📲 Partager sur WhatsApp</a>''', unsafe_allow_html=True)

# --- HISTORIQUE ---
if st.session_state.historique:
    st.write("---")
    st.subheader("📜 Historique")
    for item in st.session_state.historique:
        st.info(item)
