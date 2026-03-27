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

        # Log para debug (aparece nos logs do Railway)
