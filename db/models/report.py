import uuid
import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from db.base_class import Base


class Report(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    description = Column(String, nullable=False)
    location = Column(String, nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
