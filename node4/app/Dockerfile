FROM python:3.12-slim

WORKDIR /app
COPY . /app
ENV PYTHONPATH /app/src 
# docker 안에 컨테이너의 environment를 지정하는 커멘드

RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

CMD ["python3", "src/main.py"]