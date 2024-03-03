from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.children import router as children
from routers.categories import router as categories
from routers.furhat import router as furhat
from routers.mirai_actions import router as mirai_actions

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
app.include_router(furhat, prefix="/furhat", tags=["furhat"])
app.include_router(mirai_actions, prefix="/mirai_actions", tags=["mirai_actions"])
