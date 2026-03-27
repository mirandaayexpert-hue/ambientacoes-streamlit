import os
from fastapi import FastAPI
from pydantic import BaseModel
import openai

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
        result = openai.Image.create(
            prompt=prompt,
            size="1024x1024"
        )

        # Log para debug (aparece nos logs do Railway)
        print("Resposta OpenAI:", result)

        # Garante que existe pelo menos uma imagem
        if "data" in result and len(result["data"]) > 0 and "url" in result["data"][0]:
            url = result["data"][0]["url"]
            return {"url_imagem": url}
        else:
            return {"url_imagem": None, "erro": "Nenhuma imagem foi gerada pela API."}

    except Exception as e:
        return {"url_imagem": None, "erro": str(e)}
