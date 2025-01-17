# ingestion.py

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from models import RawData
from database import get_db
import pandas as pd
from typing import List, Dict, Union

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(None), 
    db: Session = Depends(get_db),
    request: Request = None
):
    if file:
        if file.content_type not in ["application/json", "text/csv"]:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        
        if file.content_type == "application/json":
            data = pd.read_json(file.file)
            data['date'] = data['date'].astype(str)
        elif file.content_type == "text/csv":
            data = pd.read_csv(file.file)
        
        data = data.to_dict(orient="records")

    elif request:
        data = await request.json() 
        if not isinstance(data, list):
            raise HTTPException(status_code=400, detail="Invalid JSON format, expected list of dictionaries.")

    else:
        raise HTTPException(status_code=400, detail="No data provided")

    raw_data = RawData(file_name=file.filename if file else "jsonBody", content=data)
    db.add(raw_data)
    db.commit()
    
    return {"message": "File or data uploaded successfully"}