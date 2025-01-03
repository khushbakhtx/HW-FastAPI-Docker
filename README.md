# Heart Disease Prediction API с использованием FastAPI и Docker

Этот проект представляет собой приложение для классификации заболеваний сердца с использованием модели машинного обучения и FastAPI. Проект упакован в Docker-контейнер для легкости развертывания и тестирования.

## Описание проекта

Приложение реализует классификацию заболеваний сердца на основе различных факторов (например, возраст, уровень холестерина, максимальный пульс и т.д.). API предоставляет два основных эндпоинта:
1. `POST /predict` — принимает входные данные в формате JSON, передает их в модель и возвращает предсказание.
2. `GET /health` — проверяет состояние сервиса и возвращает статус `"success"`.

## Структура проекта

Проект состоит из следующих файлов и каталогов:

- `app/`: Каталог с исходным кодом приложения.
  - `main.py`: Основной файл FastAPI приложения с определением эндпоинтов.
  - `model/engine.py`: Логика работы с моделью машинного обучения (интерфейс для предсказаний).
  - `dto/dto.py`: Определения данных, которые передаются через API (с использованием Pydantic).
  - `preprocessing/data_preprocessing.py`: Функции для предварительной обработки данных.
- `Dockerfile`: Файл для создания Docker-образа.
- `pyproject.toml`: Конфигурация для Poetry (для управления зависимостями).
- `poetry.lock`: Лок файл для Poetry.
- `model-engineering.ipynb`: и так понятно.

## Установка и запуск

1. Установить Docker Desktop и оставить его включенным. Удостовериться что галочка стоит на "Use the WSL 2 based engine".
2. Собрать образ:
  ```
  docker build -t fastapi-heart-disease-app .
  ```
3. Если возникнут ошибки с зависимостями, обновить файл, и запустить сборку заново:
    ```
    poetry lock
    ```
4. После успешной сборки, запустить контейнер:
    ```
    docker run -d -p 8008:8008 fastapi-heart-disease-app
    ```
5. Можно проверить работу приложения:
    ```http://localhost:8008/readiness```
    должно вернуть status: success.

6. Для тестирования можно отправить post запрос c необходимыми входными данными:
```
{
    "Age": 45,
    "Sex": 1,
    "RestingBP": 120,
    "Cholesterol": 200,
    "FastingBS": 0,
    "MaxHR": 150,
    "ExerciseAngina": 0,
    "Oldpeak": 1.5,
    "chest_pain_ASY": 1,
    "chest_pain_ATA": 0,
    "chest_pain_NAP": 0,
    "chest_pain_TA": 0,
    "restingECG_LVH": 0,
    "restingECG_Normal": 1,
    "restingECG_ST": 0,
    "st_slope_Down": 0,
    "st_slope_Flat": 1,
    "st_slope_Up": 0
}
``` 
7. если запускать через fastapi, то:
```
uvicorn app.main:app --reload
```
## Как это работает

1. **Предсказания**: Модель, загруженная из файла (`catboost-estimated-model.joblib`), принимает обработанные данные и генерирует предсказание.
2. **Ответ**: API возвращает предсказание (0 или 1), где 1 означает наличие заболевания, а 0 — отсутствие, а еще название модели.

ps. работая с docker.desktop, контейнер запускается там соответственно.