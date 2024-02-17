from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.children import router as children
from routers.categories import router as categories

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(children, prefix="/children", tags=["children"])
app.include_router(categories, prefix="/categories", tags=["categories"])
