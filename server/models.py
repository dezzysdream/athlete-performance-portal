from sqlalchemy import Column, Integer, String
from database import Base

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    activity = Column(String, index=True)
    duration = Column(Integer)
