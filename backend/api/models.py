from sqlalchemy import Column, Integer, String, ForeignKey, Table, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
from datetime import datetime
import enum


class ContactType(str, enum.Enum):
    collaboration = "collaboration"
    personal_interest = "person interest"
    work = "work"
    education = "education"
    other = "other"


class ContactForm(Base):
    __tablename__ = "contact_forms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    company = Column(String, nullable=True)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    contact_type = Column(Enum(ContactType), nullable=False)
    message = Column(String, nullable=True)
    date_sent = Column(DateTime, default=func.now())
