import streamlit as st
import requests
from PIL import Image
import io

st.title("Gerador de Ambientações")

# Lista de ambientes válidos
ambientes_validos = ["sala", "cozinha", "quarto", "banheiro", "escritorio", "varanda"]

# Campo de entrada normalizado
ambiente = st.text_input("Ambiente").strip().lower()
superficie = st.text_input("Superfície")
revestimento = st.text_input("Revestimento")

# Se não for válido, força para "sala"
if ambiente not in ambientes_validos:
    ambiente = "sala"

# Campo de upload de imagem
uploaded_file = st.file_uploader("Envie sua própria imagem", type=["png", "jpg", "jpeg"])

# Botão de envio
if st.button("Gerar ambientação"):
    # Monta os dados
    data = {
        "ambiente": ambiente,
        "superficie": superficie,
        "revestimento": revestimento
    }

    # Se o usuário enviou uma imagem, manda como arquivo
    if uploaded_file is not None:
        files = {"ambiente": uploaded_file.getvalue()}
        response = requests.post(
            "https://primary-production-2a5a7.up.railway.app/webhook/simulacao-revestimento",
            data=data,
            files=files
        )
    else:
        # Caso não tenha upload, só manda os parâmetros
        response = requests.post(
            "https://primary-production-2a5a7.up.railway.app/webhook/simulacao-revestimento",
            json=data
        )

    # Exibe a imagem retornada
    if response.status_code == 200:
        try:
            img = Image.open(io.BytesIO(response.content))
            st.image(img, caption=f"Ambientação gerada ({ambiente})")
        except Exception as e:
            st.error(f"Não foi possível abrir a imagem retornada: {e}")
    else:
        st.error(f"Erro na requisição: {response.status_code}")
