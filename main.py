import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# Lê a variável de ambiente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Dados(BaseModel):
    ambiente: str
    revestimento: str

@app.post("/ambientacao")
def gerar(dados: Dados):
    try:
        prompt = f"Uma ambientação de {dados.ambiente} com {dados.revestimento}"

        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        print("Resposta OpenAI:", result)

        if result.data and len(result.data) > 0 and hasattr(result.data[0], "url"):
            return {"url_imagem": result.data[0].url}
        else:
            return {"url_imagem": None, "erro": "Nenhuma imagem foi gerada."}

    except Exception as e:
        return {"url_imagem": None, "erro": str(e)}
