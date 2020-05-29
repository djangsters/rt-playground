rt-playground
=============

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

**Warning**: Paid Heroku dynos will be used! 

rt-playground allows you to easily try out [redis-tasks](
https://github.com/djangsters/redis-tasks) and [rt-dashboard](
https://github.com/djangsters/rt-dashboard).

Setup
-----
1. Create and activate a python virtualenv
2. Install python requirements 
    ```
    pip install -r requirements.txt
   ```
3. Install redis as described [here](https://redis.io/topics/quickstart)
4. Start redis
    ```
    redis-server
   ```
5. Start `redis-tasks` workers and scheduler as well as a `rt-dashboard` server
    ```
    honcho start
   ```
6. rt-dashboard should be accessible at http://localhost:8080
