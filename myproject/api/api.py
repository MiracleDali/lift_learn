from ninja import Router
from ninja_jwt.authentication import JWTAuth
from loguru import logger  # ← 导入 loguru logger（这里已经自动带上下文了）
from .models import Task
from .schemas import (TaskSchema, TaskCreateSchema, TaskUpdateSchema, AsyncRequest, 
                      AsyncResponse)
import asyncio

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


async def task(async_time):
    logger.info(f"开始异步任务1")
    await asyncio.sleep(async_time)
    logger.info(f"结束异步任务1")

async def tasks():
    logger.info(f"开始异步任务2")
    await asyncio.sleep(2)
    logger.info(f"结束异步任务2")
    
# 异步举例
@router.post("/async", response=AsyncRequest, auth=None)
async def async_test(request, playload: AsyncResponse):
    logger.info(f"开始异步任务: {playload.async_name}")

    # ==============================================
    # 1️⃣ 基础异步等待：直接使用 await asyncio.sleep()
    # ==============================================
    # - asyncio.sleep() 是异步版本的 time.sleep()
    # - await 关键字会暂停当前协程的执行
    # - 暂停期间，事件循环可以去处理其他请求（这是异步的核心优势）
    # - 模拟场景：等待数据库查询、外部API响应等IO操作
    await asyncio.sleep(playload.async_time)   

    # ==============================================
    # 2️⃣ 调用自定义异步函数：使用 await + async def 函数
    # ==============================================
    # - task() 是用 async def 定义的异步函数
    # - await 会等待 task() 内部所有操作完成后才继续执行
    # - 如果 task() 内部有 await，等待期间事件循环同样可以处理其他请求
    # - 注意：被 await 的函数必须是 async def 定义的协程
    await task(playload.async_time)

    # ==============================================
    # 3️⃣ 并发执行多个异步任务：使用 asyncio.gather()
    # ==============================================
    # - asyncio.gather() 接收多个协程对象作为参数
    # - 所有协程会被同时调度执行（真正的并行）
    # - await 会等待所有协程都完成后才继续
    # - 性能优势：总耗时 = 最长任务的耗时，而非各任务耗时之和
    # - 例如：两个各等待2秒的任务，顺序执行需4秒，并发执行仅需2秒
    # - 模拟场景：同时调用多个外部API、并行查询多个数据库表
    await asyncio.gather(
        tasks(),  # 任务A：等待2秒
        tasks()   # 任务B：等待2秒（与A同时开始）
    )
    
    # ==============================================
    # 4️⃣ 所有异步操作完成，准备返回响应
    # ==============================================
    logger.info(f"结束异步任务: {playload.async_name}")
    return {"async_name": playload.async_name, "async_time": playload.async_time}