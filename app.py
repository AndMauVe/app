import Core.database as get_db
from fastapi import FastAPI
from Routes.route import router
import os

app = FastAPI(
    title="API de prueba",
    description="API de prueba",
    version="1.0.0",
)

app.include_router(router)


@app.on_event("startup")
def _startup_init_db():
    # Evita romper el arranque si no hay BD disponible (ej. CI sin Postgres).
    try:
        get_db.init_db()
    except Exception as e:
        print(f"[WARN] No se pudo inicializar la BD: {e}")

def main():
    import uvicorn
    
    host = "0.0.0.0"
    port = int(os.environ.get("PORT", 8000))
    
    uvicorn.run(app, host=host, port=port, log_level="info")
    
if __name__ == "__main__":
    main()

