from fastapi import FastAPI
from app.api.routes.analysis import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def health_check():
    return "Server läuft"

app.include_router(router, prefix="/api")