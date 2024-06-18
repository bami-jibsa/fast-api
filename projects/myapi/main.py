from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router
from domain.youtube import youtube_real_router
from domain.youtube import youtube_router


app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# 모든 출처에서 오는 요청을 허용하도록 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello")
# def hello():
#     return {"message": "안녕하세요 파이보"}


app.include_router(question_router.router)
app.include_router(answer_router.router)

app.include_router(youtube_router.router)
app.include_router(youtube_real_router.router)