from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional

class TaskPublicSchema(BaseModel):
    id: UUID
    title: str
    description: str
    created_at: datetime
    is_completed: str 

class TaskCreate(BaseModel):   
    title: str = Field(..., max_length=300)
    description: str = Field(..., max_length = 399)
    is_completed: Optional[bool] = True

     