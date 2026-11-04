from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Pedro Studio AI",
    description="API de geração de vídeos com inteligência artificial.",
    version="0.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VideoRequest(BaseModel):
    script: str
    format: str
    scene: str
    clothing: str


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


@app.post("/generate")
def generate_video(request: VideoRequest):
    if not request.script.strip():
        return {
            "status": "error",
            "message": "O roteiro não pode estar vazio."
        }

    return {
        "status": "received",
        "message": "Roteiro recebido pelo Pedro Studio AI!",
        "video": {
            "script": request.script,
            "format": request.format,
            "scene": request.scene,
            "clothing": request.clothing
        }
    }
