import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from models.location import Location


class ReportSubmittal(BaseModel):
    description: str
    location: str

    class Config:
        orm_mode = True


class Reports(ReportSubmittal):
    id: UUID
    created_date: Optional[datetime.datetime]

    class Config:
        orm_mode = True
