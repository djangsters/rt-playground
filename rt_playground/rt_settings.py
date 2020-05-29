import os

from redis_tasks import run_every

REDIS_URL = os.environ.get("REDIS_URL", "redis://127.0.0.1:6379")
REDIS_PREFIX = "rt_playground"
SCHEDULE = {
    "success": {
        "task": "rt_playground.tasks.success",
        "args": [40],
        "schedule": run_every(seconds=30),
    },
    "failure": {
        "task": "rt_playground.tasks.failure",
        "kwargs": {"sleep_time": 5},
        "schedule": run_every(minutes=1)
    }
}
