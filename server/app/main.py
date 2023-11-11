from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.auth.router import router as auth_router
from app.specialist.router import router as specialist_router
from app.parent.router import router as parent_router
from app.config import client, env, fastapi_config

app = FastAPI(**fastapi_config)


@app.on_event("shutdown")
def shutdown_db_client():
    client.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=env.CORS_ORIGINS,
    allow_methods=env.CORS_METHODS,
    allow_headers=env.CORS_HEADERS,
    allow_credentials=True,
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(specialist_router, prefix="/specialists", tags=["Specialist"])
app.include_router(parent_router, prefix="/parents", tags=["Parents"])
