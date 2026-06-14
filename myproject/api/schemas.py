from ninja import Schema
from typing import Optional
from datetime import datetime  # 1. 导入 datetime

class TaskSchema(Schema):
    id: int
    title: str
    completed: bool
    created_at: datetime  

class TaskCreateSchema(Schema):
    title: str
    completed: Optional[bool] = False

class TaskUpdateSchema(Schema):
    title: Optional[str] = None
    completed: Optional[bool] = None

# 异步任务响应模型
class AsyncRequest(Schema):
    async_name: str
    async_time: int
# 异步任务请求模型
class AsyncResponse(Schema):
    async_name: str
    async_time: int