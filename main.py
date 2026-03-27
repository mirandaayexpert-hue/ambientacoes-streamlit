import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# Lê a chave da OpenAI das variáveis de ambiente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Modelo de dados que a API recebe
class Dados(BaseModel):
    ambiente: str
    revestimento: str

# Endpoint principal
@app.post("/ambientacao")
def gerar(dados: Dados):
    try:
        # Prompt mais detalhado para melhorar a qualidade da imagem
        prompt = (
            f"Renderização realista de {dados.ambiente} "
            f"com revestimento em {dados.revestimento}, "
            f"estilo moderno, iluminação natural suave, "
            f"perspectiva arquitetônica detalhada"
        )

        # Chamada à API da OpenAI para gerar imagem
        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        # Log para debug (aparece nos logs do Railway)
        print("Resposta OpenAI:", result)

        # Garante que existe
