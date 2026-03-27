import streamlit as st
import requests

st.title("Gerador de Ambientações")

ambiente = st.text_input("Ambiente:")
revestimento = st.text_input("Revestimento:")

if st.button("Gerar Imagem"):
    st.write(f"Gerando ambientação para {ambiente} com {revestimento}...")

    # Chamada à API no Railway
    resp = requests.post(
        "https://ambientacoes-streamlit-production.up.railway.app/ambientacao",
        json={"ambiente": ambiente, "revestimento": revestimento}
    )

    if resp.status_code == 200:
        dados = resp.json()
        if "url_imagem" in dados:
            st.image(dados["url_imagem"], caption="Ambientação gerada")
        else:
            st.write("Resposta recebida, mas não encontrei a chave 'url_imagem'.")
    else:
        st.error("Erro ao chamar a API: " + str(resp.status_code))
