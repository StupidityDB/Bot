FROM python:slim

RUN pip install poetry

WORKDIR /usr/src/app
STOPSIGNAL INT

COPY pyproject.toml ./
RUN poetry install --no-root

COPY stupiditydb/bot.py stupiditydb/config.py .

CMD [ "poetry", "run", "python", "bot.py" ]
