from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from . import crud, schemas, models

app = FastAPI()

# Initialize tables
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/contact/", response_model=schemas.ContactFormResponse, status_code=201)
async def create_contact(form: schemas.ContactFormCreate, db: Session = Depends(get_db)):
    try:
        contact_entry = crud.create_contact_form(
            db, form.name, form.company, form.email, form.phone_number, form.contact_type, form.message)
        return contact_entry
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
