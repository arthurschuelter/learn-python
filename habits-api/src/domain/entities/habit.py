from uuid import UUID, uuid4
from typing import Optional
from datetime import datetime

class Habit:
    def __init__(
        self, 
        name: str,        
        description: str,
        user_id: UUID,
        created_at: Optional[datetime] = None, 
        updated_at: Optional[datetime] = None,
    ):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()