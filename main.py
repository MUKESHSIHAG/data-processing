from fastapi import FastAPI
from routers import ingestion, transformation, retrieval

app = FastAPI()

app.include_router(ingestion.router, prefix="/ingestion", tags=["ingestion"])
app.include_router(transformation.router, prefix="/transformation", tags=["transformation"])
app.include_router(retrieval.router, prefix="/retrieval", tags=["retrieval"])
