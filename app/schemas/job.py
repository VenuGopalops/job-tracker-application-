from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobCreate(BaseModel):
    company: str
    role: str
    status: str = "applied"
    notes: Optional[str] = None

class JobUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None

class JobResponse(BaseModel):
    id: int
    company: str
    role: str
    status: str
    notes: Optional[str] = None
    applied_date: datetime
    user_id: int

    class Config:
        from_attributes = True