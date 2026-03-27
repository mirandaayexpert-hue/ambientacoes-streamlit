import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Dados(BaseModel):
    ambiente: str
    revestimento: str

@app.post("/ambientacao")
def gerar(dados: Dados):
    try:
        # Prompt mínimo e direto
        prompt = f"{dados.ambiente} com revestimento em {dados.revestimento}"

        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        print("Resposta OpenAI:", result)

        if result and result.data and len(result.data) > 0 and hasattr(result.data[0], "url"):
            return {"url_imagem": result.data[0].url}
        else:
            return {"url_imagem": None, "erro": "Nenhuma imagem foi gerada."}

    except Exception as e:
        # Captura qualquer erro e evita 502
        return {"url_imagem": None, "erro": f"Erro na API ou na conexão: {str(e)}"}
