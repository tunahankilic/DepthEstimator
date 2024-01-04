FROM python:3.11

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libjpeg-dev && \
    apt-get clean 

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false && \
    poetry install --no-root

COPY . /app

EXPOSE 8041

CMD ["poetry", "run", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8041"]