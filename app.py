import streamlit as st
import requests

st.title("Gerador de Ambientações")

ambiente = st.text_input("Ambiente:")
revestimento = st.text_input("Revestimento:")

if st.button("Gerar Imagem"):
    st.write(f"Gerando ambientação para {ambiente} com {revestimento}...")
    # Aqui futuramente você conecta com sua API de geração de imagens
