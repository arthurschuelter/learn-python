from uuid import UUID, uuid4
from typing import Optional
from datetime import datetime

class HabitEntry:
    def __init__(
        self, 
        habit_id: UUID,
        entry_date: datetime,
        created_at: Optional[datetime] = None, 
        updated_at: Optional[datetime] = None,
    ):
        self.habit_id = habit_id
        self.entry_date = entry_date
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()