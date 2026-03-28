import streamlit as st
import requests
from PIL import Image
import io

st.title("Gerador de Ambientações")

# Campos de entrada
ambiente = st.text_input("Ambiente")
superficie = st.text_input("Superfície")
revestimento = st.text_input("Revestimento")

# Campo de upload de imagem
uploaded_file = st.file_uploader("Envie sua própria imagem", type=["png", "jpg", "jpeg"])

# Botão de envio
if st.button("Gerar ambientação"):
    # Monta os dados
    data = {
        "superficie": superficie,
        "revestimento": revestimento
    }

    # Se o usuário enviou uma imagem, manda como arquivo
    if uploaded_file is not None:
        files = {"ambiente": uploaded_file.getvalue()}
        response = requests.post("URL_DO_SEU_WEBHOOK", data=data, files=files)
    else:
        # Caso não tenha upload, só manda os parâmetros
        response = requests.post("URL_DO_SEU_WEBHOOK", json=data)

    # Exibe a imagem retornada
    if response.status_code == 200:
        try:
            img = Image.open(io.BytesIO(response.content))
            st.image(img, caption="Ambientação gerada")
        except Exception:
            st.error("Não foi possível abrir a imagem retornada.")
    else:
        st.error(f"Erro na requisição: {response.status_code}")
