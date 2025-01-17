import pandas as pd
from models import RawData, ProcessedData
from sqlalchemy.orm import Session

def process_data(raw_data: RawData, db: Session):
    """
        total_cost = sum(cost1, cost2, cost3)
        total_profit = profit - total_cost
    """
    df = pd.DataFrame(raw_data.content)
    
    df['total_cost'] = df[['cost1', 'cost2', 'cost3']].sum(axis=1)
    
    df['total_profit'] = df['profit'] - df['total_cost']
    
    processed_content = df.to_dict(orient='records')
    
    processed_data = ProcessedData(raw_id=raw_data.id, processed_content=processed_content)
    db.add(processed_data)
    db.commit()

    return processed_content

