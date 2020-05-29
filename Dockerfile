FROM python:3.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH="/usr/src/app"
EXPOSE 8080

CMD [ "python", "-m", "rt_playground.dashboard" ]
