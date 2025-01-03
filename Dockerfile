FROM python:3.12.1-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry

# установка зависимостей
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

COPY ./app ./app

# нужно для правильного импорта
ENV PYTHONPATH=/app

# запускаем FastAPI приложение (убрали код if __name__ == '__main__.py')
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8008"]
