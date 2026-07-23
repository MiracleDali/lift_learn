from celery import Celery


cel = Celery('celery_dome',      # celery 任务名称       
             broker='redis://localhost:6379/1',     # 消息中间件地址
             backend='redis://localhost:6379/2',    # 保存任务结果的数据库地址
             # 包含以下任务模块，去相应的py文件中找任务。对多个任务做分类
             include=['celery_tasks.task01',
                      'celery_tasks.task02'
                      ]
            )

# 时区
cel.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC时间
cel.conf.enable_utc = False


########################################################
# 周期性任务
cel.conf.beat_schedule = {
    # 任务随意命名
    'add_every_10_seconds': {
        # 执行的任务
        'task': 'celery_tasks.task01.send_email',
        # 执行的时间间隔
        'schedule': 6.0,
        # 任务参数
        'args': ('小王',)
    },
}