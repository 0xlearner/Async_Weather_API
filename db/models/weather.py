import uuid
import datetime

from sqlalchemy import Column, Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.base_class import Base


class Weather(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    city = Column(String, nullable=False)
    state = Column(String, nullable=True)
    country = Column(String, nullable=False)
    units = Column(String, nullable=True, default="metric")
    temperature = Column(Float, nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
