from sqlalchemy import Column, Integer, String, JSON, DateTime
from database import Base
from datetime import datetime

class RawData(Base):
    __tablename__ = "raw_data"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, index=True)
    upload_date = Column(DateTime, default=datetime.utcnow)
    content = Column(JSON)

class ProcessedData(Base):
    __tablename__ = "processed_data"

    id = Column(Integer, primary_key=True, index=True)
    raw_id = Column(Integer)
    processed_date = Column(DateTime, default=datetime.utcnow)
    processed_content = Column(JSON)
