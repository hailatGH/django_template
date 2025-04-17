FROM python:3.13-alpine

ENV PIPX_BIN_DIR=/root/.local/bin
ENV PATH=${PIPX_BIN_DIR}:${PATH}
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install pipx \
    && pipx ensurepath \
    && pipx install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root
    
COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application", "--workers", "3", "--threads", "8", "--timeout", "120"]