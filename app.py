import Core.database as get_db
from fastapi import FastAPI
from Routes.route import router

app = FastAPI(
    title="API de prueba",
    description="API de prueba",
    version="1.0.0",
)

app.include_router(router)

def main():
    import uvicorn
    import webbrowser
    from threading import Timer
    
    host = "127.0.0.1"
    port = 8000
    
    def abrir_browser():
        webbrowser.open(f"http://{host}:{port}/ping")
        
    Timer(1.5, abrir_browser).start()
    
    uvicorn.run(app, host=host, port=port, log_level="info")
    
if __name__ == "__main__":
    main()

