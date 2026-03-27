import os
from fastapi import FastAPI
from pydantic import BaseModel
import openai

# Inicializa o FastAPI
app = FastAPI()

# Pega a chave da OpenAI das variáveis de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

# Modelo de dados que a API recebe
class Dados(BaseModel):
    ambiente: str
    revestimento: str

# Endpoint principal
@app.post("/ambientacao")
def gerar(dados: Dados):
    try:
        # Cria o prompt com base nos dados enviados
        prompt = f"Uma ambientação de {dados.ambiente} com {dados.revestimento}"

        # Chama a API da OpenAI para gerar imagem
        result = openai.images.generate(
            model="gpt-image-1",   # modelo de geração de imagens
            prompt=prompt,
            size="1024x1024"
        )

        # Pega a URL da primeira imagem gerada
        url = result.data[0].url

        return {"url_imagem": url}

    except Exception as e:
        # Se der erro, retorna mensagem clara
        return {"erro": str(e)}
