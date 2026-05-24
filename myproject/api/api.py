from ninja import Router
from .models import Task
from .schemas import TaskSchema, TaskCreateSchema, TaskUpdateSchema

router = Router()

# 获取任务列表
@router.get("/tasks", response=list[TaskSchema])
def list_tasks(request):
    return Task.objects.all()

# 获取单个任务
@router.get("/tasks/{task_id}", response=TaskSchema)
def get_task(request, task_id: int):
    task = Task.objects.get(id=task_id)
    return task

# 创建任务
@router.post("/tasks", response=TaskSchema)
def create_task(request, payload: TaskCreateSchema):
    task = Task.objects.create(**payload.dict())
    return task

# 更新任务
@router.put("/tasks/{task_id}", response=TaskSchema)
def update_task(request, task_id: int, payload: TaskUpdateSchema):
    task = Task.objects.get(id=task_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(task, attr, value)
    task.save()
    return task

# 删除任务
@router.delete("/tasks/{task_id}")
def delete_task(request, task_id: int):
    task = Task.objects.get(id=task_id)
    task.delete()
    return {"success": True}