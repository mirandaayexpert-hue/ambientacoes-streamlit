import os
import openai
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Configura a chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

class Dados(BaseModel):
    ambiente: str
    revestimento: str

@app.post("/ambientacao")
def gerar(dados: Dados):
    try:
        # Prompt simples e direto
        prompt = f"{dados.ambiente} com revestimento em {dados.revestimento}"

        result = openai.Image.create(
            prompt=prompt,
            size="1024x1024"
        )

        print("Resposta OpenAI:", result)

        if result and "data" in result and len(result["data"]) > 0 and "url" in result["data"][0]:
            return {"url_imagem": result["data"][0]["url"]}
        else:
            return {"url_imagem": None, "erro": "Nenhuma imagem foi gerada."}

    except Exception as e:
        return {"url_imagem": None, "erro": f"Erro na API ou na conexão: {str(e)}"}
