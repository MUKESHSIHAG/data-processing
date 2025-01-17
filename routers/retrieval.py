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
    start_date: Optional[str] = None,  # Query parameter for start date
    end_date: Optional[str] = None,    # Query parameter for end date
    user_id: Optional[int] = None      # Query parameter for user ID
):
    # Build the query with optional filters
    query = db.query(ProcessedData)
    
    if start_date:
        query = query.filter(ProcessedData.processed_date >= start_date)
    
    if end_date:
        query = query.filter(ProcessedData.processed_date <= end_date)
    
    if user_id:
        query = query.filter(ProcessedData.user_id == user_id)
    
    # Fetch the filtered data
    data = query.all()
    
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    
    return data
