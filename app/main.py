from fastapi import FastAPI

app = FastAPI(title="Gestor Simples API",
              description="API para gerenciamento de pedidos simples",
              version="0.1.0"
              )

@app.get("/")
def read_root():
    return {"message": "Bem-vindo a API do Gestor Simples!"}


