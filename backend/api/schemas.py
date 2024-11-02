from pydantic import BaseModel, EmailStr
from datetime import datetime
from .models import ContactType


class ContactFormCreate(BaseModel):
    name: str
    company: str = None
    email: EmailStr
    phone_number: str = None
    contact_type: ContactType
    message: str = None


class ContactFormResponse(ContactFormCreate):
    id: int
    date_sent: datetime

    class Config:
        orm_mode = True
