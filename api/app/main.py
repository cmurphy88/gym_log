from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from .home import router as home_router
from .exercise import router as exercise_router


app = FastAPI(title="GYMLOGWebApp",
              version="0.0.1")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    # "https://jarvis-qub.co.uk",
    # "https://www.jarvis-qub.co.uk",
    "http://127.0.0.1:8000",
    # "https://jarvis-qub.co.uk/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(exercise_router.router)
# app.include_router(auth_router.router)