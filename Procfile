web: python -m rt_playground.dashboard
worker1: PYTHONPATH=$PYTHONPATH:$PWD redis_tasks worker
worker2: PYTHONPATH=$PYTHONPATH:$PWD redis_tasks worker
scheduler: PYTHONPATH=$PYTHONPATH:$PWD redis_tasks scheduler
