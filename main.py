import os
from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class Dados(BaseModel):
    ambiente: str
    revestimento: str

@app.post("/ambientacao")
def gerar(dados: Dados):
    try:
        prompt = f"Uma ambientação de {dados.ambiente} com {dados.revestimento}"

        result = openai.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        # Garante que existe pelo menos uma imagem
        if result and "data" in result and len(result.data) > 0:
            url = result.data[0].url
            return {"url_imagem": url}
        else:
            return {"erro": "Nenhuma imagem foi gerada pela API."}

    except Exception as e:
        return {"erro": str(e)}
