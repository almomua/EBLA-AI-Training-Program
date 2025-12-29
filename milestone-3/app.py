from fastapi import FastAPI
from Routes.index_routes import router as index_router
from Routes.retrieval_routes import router as retrieval_router

app = FastAPI(title="RAG Indexing API", version="1.0.0")

app.include_router(index_router, tags=["Index"])
app.include_router(retrieval_router, tags=["Search"])


@app.get("/")
def root():
    return {"message": "RAG Indexing API - Milestone 3"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run( "app:app", host="0.0.0.0", port=8000, reload=True)