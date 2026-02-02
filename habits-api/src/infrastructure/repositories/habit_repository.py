from typing import List, Optional
from uuid import UUID
from application.interfaces.habit_repository_interface import HabitRepositoryInterface
from domain.entities.habit import Habit
from infrastructure.database.connection import get_db
import datetime

class HabitRepository(HabitRepositoryInterface):
    def __init__(self, db_session):
        self.db_session = db_session

    def create(self, habit: Habit):
        print("Creating habit in the database")
        from sqlalchemy import text
        try:
            query = text("INSERT INTO habits (name, description, user_id, created_at) VALUES (:name, :description, :user_id, :created_at) RETURNING id")
            result = self.db_session.execute(
                query,
                {"name": habit.name, "description": habit.description, "user_id": habit.user_id, "created_at": datetime.datetime.now()}
            )
            self.db_session.commit()
            habit_id = result.fetchone()[0]
            print(f"Habit created with id: {habit_id}")
            return habit
        except Exception as e:
            print(f"Error creating habit: {e}")
            self.db_session.rollback()
            raise

    # async def get_by_id(self, habit_id: int) -> Optional[Habit]:
    #     return self.db_session.query(Habit).filter(Habit.id == habit_id).first()

    async def get_by_user_id(self, user_id: UUID) -> List[Habit]:
        from sqlalchemy import text
        query = text("SELECT id, name, description, user_id, created_at, updated_at FROM habits WHERE user_id = :user_id")
        result = self.db_session.execute(query, {"user_id": str(user_id)})
        rows = result.fetchall()

        # Convert rows to Habit domain entities
        habits = []
        for row in rows:
            habit = Habit(
                name=row[1],
                description=row[2],
                user_id=row[3],
                created_at=row[4],
                updated_at=row[5]
            )
            habits.append(habit)
        return habits

    # async def update(self, habit: Habit) -> Habit:
    #     self.db_session.merge(habit)
    #     self.db_session.commit()
    #     return habit

    # async def delete(self, habit_id: int) -> bool:
    #     habit = self.db_session.query(Habit).filter(Habit.id == habit_id).first()
    #     if habit:
    #         self.db_session.delete(habit)
    #         self.db_session.commit()
    #         return True
    #     return False