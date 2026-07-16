import streamlit as st

st.set_page_config(
    page_title="🍔 Burger House",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    .stLinkButton a {
        background: linear-gradient(135deg, #25D366, #128C7E) !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        padding: 18px 48px !important;
        border-radius: 60px !important;
        border: none !important;
        letter-spacing: 2px !important;
        box-shadow: 0 8px 30px rgba(37,211,102,0.5) !important;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with open("hamburguesas.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=3000, scrolling=False)

st.markdown("""
<div style="background-color:#1A0A00; text-align:center; padding: 10px 20px 10px;">
  <p style="font-family:Georgia,serif; font-style:italic; font-size:1.1rem; color:rgba(255,255,255,0.6); margin-bottom:16px;">
    ¿Ya tenés el antojo? Hacé tu pedido ahora 👇
  </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.link_button(
        "💬 PEDIR POR WHATSAPP",
        "https://wa.me/573103461997?text=¡Hola!%20Quiero%20hacer%20un%20pedido%20de%20hamburguesas%20🍔",
        use_container_width=True
    )

st.markdown("""
<div style="background-color:#1A0A00; text-align:center; padding:10px 20px 40px;">
  <p style="font-size:0.8rem; color:rgba(255,255,255,0.25); letter-spacing:2px;">
    Te respondo lo antes posible 🤝
  </p>
  <p style="font-size:0.75rem; color:rgba(255,255,255,0.15); letter-spacing:2px; margin-top:20px; border-top:1px solid rgba(255,255,255,0.08); padding-top:16px;">
    🍔 BURGER HOUSE · HECHO CON AMOR · 8 MAYO 2026
  </p>
</div>
""", unsafe_allow_html=True)
