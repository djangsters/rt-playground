rt-playground
=============

`rt-playground` allows you to easily try out [redis-tasks](
https://github.com/djangsters/redis-tasks) and [rt-dashboard](
https://github.com/djangsters/rt-dashboard).

Heroku setup
------------
`rt-playground` can be easily deployed to Heroku by pressing the button below,
however it requires at least three different processes to run, in particular
web, scheduler and worker, which prevents usage of free Heroku dynos and requires
Heroku account validation.    

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

**Warning**: Paid Heroku dynos will be used! 

Local setup
-----------
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

Docker setup
------------
1. Start all containers
    ```
    docker-compose up
    ```
2. rt-dashboard should be accessible at http://localhost:8080
