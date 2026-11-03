from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Pedro Studio AI",
    description="API pessoal para geração de vídeos com inteligência artificial.",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "projeto": "Pedro Studio AI",
        "status": "online",
        "mensagem": "Backend iniciado com sucesso!"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
