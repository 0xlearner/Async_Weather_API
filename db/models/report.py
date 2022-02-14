import uuid
import datetime

from sqlalchemy import (
    Column,
    Float,
    ForeignKeyConstraint,
    Integer,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.base_class import Base


class Report(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    description = Column(String, nullable=True)
    location = Column(String, nullable=True)
    temp = Column(Float, nullable=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    # weather = relationship("Weather", back_populates="report")
    # __table_args__ = (
    #     ForeignKeyConstraint(["location", "temp"], ["weather.city", "weather.temperature"]),
    #     {},
    # )
