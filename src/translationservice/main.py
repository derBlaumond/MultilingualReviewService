from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="TranslationService",
    description="Handles translation requests for text using external APIs or mocked responses.",
    version="1.0.0"
)

# Include the router for translation-related endpoints
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)