from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime

class ModelBaseInfo(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
