import streamlit as st

st.set_page_config(
    page_title="🍔 Burger House",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ocultar el menú y footer de Streamlit para pantalla limpia
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Leer el HTML
with open("hamburguesas.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Renderizar la página completa
st.components.v1.html(html_content, height=3200, scrolling=True)