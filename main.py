from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Dados(BaseModel):
    ambiente: str
    revestimento: str

@app.post("/ambientacao")
def gerar(dados: Dados):
    # Aqui você conecta com seu agente gerador de imagens
    # Por enquanto, devolvemos uma imagem de teste
    return {"url_imagem": "https://picsum.photos/600/400"}
