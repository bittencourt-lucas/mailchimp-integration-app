from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.router import root_router


app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'],
)

app.include_router(root_router)
