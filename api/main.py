from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

app = FastAPI(title="AgentSai Factory API")

# 🔐 CORS (OBLIGATORIO para Next.js)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
