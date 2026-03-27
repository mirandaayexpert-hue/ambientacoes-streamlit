import openai
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

openai.api_key = "SUA_CHAVE_OPENAI"

class Dados(BaseModel):
    ambiente: str
    revestimento: str

@app.post("/ambientacao")
def gerar(dados: Dados):
    prompt = f"Uma ambientação de {dados.ambiente} com {dados.revestimento}"
    result = openai.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )
    url = result.data[0].url
    return {"url_imagem": url}
