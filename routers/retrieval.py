from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_
from models import ProcessedData
from database import get_db
from typing import Optional

router = APIRouter()

@router.get("/data")
async def get_data(
    db: Session = Depends(get_db),
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    user_id: Optional[int] = None
):
    query = db.query(ProcessedData)
    
    if start_date:
        query = query.filter(ProcessedData.processed_date >= start_date)
    
    if end_date:
        query = query.filter(ProcessedData.processed_date <= end_date)
    
    if user_id:
        query = query.filter(ProcessedData.user_id == user_id)

    data = query.all()
    
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    
    return data
