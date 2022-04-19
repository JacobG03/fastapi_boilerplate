import uvicorn
from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from app.api import api
from app.core import config


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=config.server.ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(title=config.server.TITLE, middleware=middleware)
app.include_router(api)

if __name__ == "__main__":
    uvicorn.run(app, host=config.server.HOST, port=config.server.PORT)
