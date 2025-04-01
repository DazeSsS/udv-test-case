from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from app.api.exceptions import set_exceptions
from app.api.routers import api_router


app = FastAPI(
    title='News Service'
)

set_exceptions(app)

app.include_router(api_router)

origins = settings.ORIGINS.split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET'],
    allow_headers=['*'], 
)
