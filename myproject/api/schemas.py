from ninja import Schema
from datetime import datetime

class TaskSchema(Schema):
    id: int
    title: str
    completed: bool
    created_at: datetime

class TaskCreateSchema(Schema):
    title: str
    completed: bool = False

class TaskUpdateSchema(Schema):
    title: str = None
    completed: bool = None