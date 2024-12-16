import threading
from fastapi import FastAPI
from .routes import router
from .grpc_server import serve

app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the ReviewService API!"}

# Start gRPC server in a separate thread
def start_grpc_server():
    serve()

if __name__ == "__main__":
    import uvicorn

    # Start gRPC server in a background thread
    grpc_thread = threading.Thread(target=start_grpc_server, daemon=True)
    grpc_thread.start()

    # Start FastAPI application
    uvicorn.run(app, host="0.0.0.0", port=8000)