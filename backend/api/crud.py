from sqlalchemy.orm import Session
from .models import ContactForm, ContactType


def create_contact_form(db: Session, name: str, company: str, email: str, phone_number: str, contact_type: ContactType, message: str):

    form = ContactForm(name=name, company=company, email=email, phone_number=phone_number,
                       contact_type=contact_type, message=message)
    db.add(form)
    db.commit()
    db.refresh(form)
    return form
