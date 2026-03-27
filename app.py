import streamlit as st
import requests

st.title("Gerador de Ambientações")

# Campos de entrada
ambiente = st.text_input("Ambiente:")
revestimento = st.text_input("Revestimento:")

# Botão para gerar imagem
if st.button("Gerar Imagem"):
    st.write(f"Gerando ambientação para {ambiente} com {revestimento}...")

    try:
        # Chamada à API hospedada no Railway
        resp = requests.post(
            "https://ambientacoes-streamlit-production.up.railway.app/ambientacao",
            json={"ambiente": ambiente, "revestimento": revestimento}
        )

        if resp.status_code == 200:
            dados = resp.json()
            # Só mostra a imagem se realmente existir uma URL válida
            if dados.get("url_imagem"):
                st.image(dados["url_imagem"], caption="Ambientação gerada")
            else:
                st.error("Não foi possível gerar a imagem. Detalhes: " + str(dados.get("erro")))
        else:
            st.error("Erro ao chamar a API: " + str(resp.status_code))

    except Exception as e:
        st.error("Erro inesperado: " + str(e))
