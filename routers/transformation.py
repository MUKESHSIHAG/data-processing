# transformation.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import RawData
from database import get_db
from .utils import process

router = APIRouter()

@router.post("/process")
async def transform(raw_id: int, db: Session = Depends(get_db)):
    raw_data = db.query(RawData).filter(RawData.id == raw_id).first()
    if not raw_data:
        raise HTTPException(status_code=404, detail="Raw data not found")

    processed_content = process.process_data(raw_data, db)
    
    return {"message": "Data processed successfully", "processed_data": processed_content}

