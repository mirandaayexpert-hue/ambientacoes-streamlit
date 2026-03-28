import streamlit as st
import requests
import json

st.title("Simulação de Revestimento")

# Inputs do usuário
ambiente = st.selectbox("Escolha o ambiente", ["sala", "cozinha", "quarto", "banheiro", "escritorio", "varanda"])
superficie = st.selectbox("Escolha a superfície", ["parede", "piso", "teto"])
revestimento = st.text_input("Digite o revestimento desejado")
uploaded_file = st.file_uploader("Envie uma imagem do ambiente (opcional)", type=["jpg", "jpeg", "png"])

# Botão para enviar
if st.button("Simular"):
    data = {
        "ambiente": ambiente,
        "superficie": superficie,
        "revestimento": revestimento
    }

    if uploaded_file is not None:
        files = {"imagem": uploaded_file.getvalue()}
        response = requests.post(
            "https://primary-production-2a5a7.up.railway.app/webhook/simulacao-revestimento",
            data={"json": json.dumps(data)},  # força envio dos campos como JSON
            files=files
        )
    else:
        response = requests.post(
            "https://primary-production-2a5a7.up.railway.app/webhook/simulacao-revestimento",
            json=data
        )

    # Exibir resultado
    if response.status_code == 200:
        st.success("Requisição enviada com sucesso!")
        st.write(response.json())
    else:
        st.error(f"Erro na requisição: {response.status_code}")
        st.write(response.text)
