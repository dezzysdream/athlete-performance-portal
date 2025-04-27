import strawberry
from typing import List

@strawberry.type
class Workout:
    id: int
    activity: str
    duration: int  # in minutes

# Fake database (for now)
workouts_db = [
    Workout(id=1, activity="Running", duration=45),
    Workout(id=2, activity="Cycling", duration=30),
]

@strawberry.type
class Query:
    @strawberry.field
    def workouts(self) -> List[Workout]:
        return workouts_db

# 🆕 ADD this for creating a workout
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_workout(self, activity: str, duration: int) -> Workout:
        new_id = len(workouts_db) + 1
        new_workout = Workout(id=new_id, activity=activity, duration=duration)
        workouts_db.append(new_workout)
        return new_workout

# Update schema to include mutation
schema = strawberry.Schema(query=Query, mutation=Mutation)
