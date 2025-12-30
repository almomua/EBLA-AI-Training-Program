from fastapi import FastAPI
from Routes.index_routes import router as index_router
from Routes.retrieval_routes import router as retrieval_router
from Routes.ask_routes import router as ask_router

app = FastAPI(title="RAG API", version="1.0.0")

app.include_router(index_router, tags=["Index"])
app.include_router(retrieval_router, tags=["Search"])
app.include_router(ask_router, tags=["Ask"])


@app.get("/")
def root():
    return {"message": "RAG API - Milestone 4"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run( "app:app", host="0.0.0.0", port=8000, reload=True)