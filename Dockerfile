FROM python:3.8-slim-buster

WORKDIR /app
RUN pip install requests
COPY . .

ENTRYPOINT [ "/app/run_inside_docker.sh" ]