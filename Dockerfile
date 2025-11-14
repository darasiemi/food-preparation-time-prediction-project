FROM python:3.13.5-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /code

ENV PATH="/code/.venv/bin:$PATH"

COPY "pyproject.toml" "uv.lock" ".python-version" ./
RUN uv sync --locked

RUN mkdir -p /code/model /code/utils /code/deployment

COPY deployment/ /code/deployment/
COPY utils/      /code/utils/
COPY model/      /code/model/

EXPOSE 9696

ENTRYPOINT ["uvicorn", "deployment.predict:app", "--host", "0.0.0.0", "--port", "9696"]