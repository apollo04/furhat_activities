from datetime import datetime

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.auth.router import router as auth_router
from app.specialist.router import router as specialist_router
from app.parent.router import router as parent_router
from app.admin.router import router as admin_router
from app.config import client, env, fastapi_config, database

from app.auth.repository.repository import AuthRepository

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
app.include_router(admin_router, prefix="/admins", tags=["Admin"])
app.include_router(parent_router, prefix="/parents", tags=["Parents"])


admin_input = {
    "email": 'admin@gmail.com',
    "role": 'admin',
    "name": 'admin',
    "surname": 'admin',
    "password": 'Admin123',
    "created_at": datetime.utcnow(),
}

user = AuthRepository(database).get_user_by_email("admin@gmail.com")

if not user:
    AuthRepository(database).create_user(user=admin_input)
