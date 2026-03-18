from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, jobs
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Application Tracker", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(jobs.router)

@app.get("/")
def root():
    return {"message": "Job Tracker API is running"}