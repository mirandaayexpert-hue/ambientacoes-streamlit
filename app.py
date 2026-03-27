import streamlit as st
import requests

st.title("Gerador de Ambientações")

ambiente = st.text_input("Ambiente:")
revestimento = st.text_input("Revestimento:")

if st.button("Gerar Imagem"):
    st.write(f"Gerando ambientação para {ambiente} com {revestimento}...")

    # Faz a chamada ao seu agente no Railway
    resp = requests.post(
        "https://primary-production-2a5a7.up.railway.app/webhook-test/ambientacao",
        json={
            "ambiente": ambiente,
            "revestimento": revestimento
        }
    )

    # Se sua API devolve um JSON com a URL da imagem
    if resp.status_code == 200:
        dados = resp.json()
        if "url_imagem" in dados:
            st.image(dados["url_imagem"])
        else:
            st.write("Resposta recebida, mas não encontrei a chave 'url_imagem'.")
    else:
        st.error("Erro ao chamar a API: " + str(resp.status_code))
