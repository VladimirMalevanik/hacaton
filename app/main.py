import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles

# ↓ добавь эти две строки
from dotenv import load_dotenv
load_dotenv()

from .db import engine, Base
from .auth_routes import router as auth_router
from .chat_routes import router as chat_router
