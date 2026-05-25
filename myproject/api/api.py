from ninja import Router
from ninja_jwt.authentication import JWTAuth
from .models import Task
from .schemas import TaskSchema, TaskCreateSchema, TaskUpdateSchema

router = Router()

# 公开接口：无需登录即可查看
@router.get("/tasks", response=list[TaskSchema])
def list_tasks(request):
    return Task.objects.all()

# 受保护接口：必须携带有效的 Bearer Token
@router.post("/tasks", response=TaskSchema, auth=JWTAuth())
def create_task(request, payload: TaskCreateSchema):
    return Task.objects.create(**payload.dict())

@router.put("/tasks/{task_id}", response=TaskSchema, auth=JWTAuth())
def update_task(request, task_id: int, payload: TaskUpdateSchema):
    task = Task.objects.get(id=task_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(task, attr, value)
    task.save()
    return task

@router.delete("/tasks/{task_id}", auth=JWTAuth())
def delete_task(request, task_id: int):
    Task.objects.get(id=task_id).delete()
    return {"success": True}