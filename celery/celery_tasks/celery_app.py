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