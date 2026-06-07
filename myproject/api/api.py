from ninja import Router
from ninja_jwt.authentication import JWTAuth
from loguru import logger  # ← 导入 loguru logger（这里已经自动带上下文了）
from .models import Task
from .schemas import TaskSchema, TaskCreateSchema, TaskUpdateSchema

router = Router()

# 公开接口：无需登录即可查看
@router.get("/tasks", response=list[TaskSchema])
def tasks(request):
    # ↓ 直接用 logger，自动带上当前用户名（匿名就是 anonymous）
    logger.info("查询所有任务")
    tasks = Task.objects.all()
    logger.debug(f"返回 {len(tasks)} 条任务")
    return tasks

# 受保护接口：必须携带有效的 Bearer Token
@router.post("/tasks", response=TaskSchema, auth=JWTAuth())
def create_task(request, payload: TaskCreateSchema):
    # ↓ JWT 认证通过后，request.user 已经是当前用户，自动注入到日志
    logger.info(f"创建任务: {payload.title}")
    task = Task.objects.create(**payload.dict())
    logger.success(f"任务创建成功: id={task.id}")
    return task

@router.put("/tasks/{task_id}", response=TaskSchema, auth=JWTAuth())
def update_task(request, task_id: int, payload: TaskUpdateSchema):
    logger.info(f"更新任务: id={task_id}")
    task = Task.objects.get(id=task_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(task, attr, value)
    task.save()
    logger.success(f"任务更新成功: id={task_id}")
    return task

@router.delete("/tasks/{task_id}", auth=JWTAuth())
def delete_task(request, task_id: int):
    logger.warning(f"删除任务: id={task_id}")
    Task.objects.get(id=task_id).delete()
    logger.info(f"删除成功: id={task_id}")
    return {"success": True}