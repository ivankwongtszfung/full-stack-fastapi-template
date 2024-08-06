# FastAPI Project - Backend

## Local Development

* Start the stack with Docker Compose:

```bash
docker compose up -d
```


Automatic documentation: http://localhost/docs

To check the logs, run:

```bash
docker compose logs
```

To check the logs of a specific service, add the name of the service, e.g.:

```bash
docker compose logs backend
```

## Backend local development, additional details

### General workflow

By default, the dependencies are managed with [Poetry](https://python-poetry.org/), go there and install it.

From `./backend/` you can install all the dependencies with:

```console
$ poetry install
```

Then you can start a shell session with the new environment with:

```console
$ poetry shell
```

#### Test running stack


Run test
```bash
docker compose exec backend bash /app/tests-start.sh
```


to stop on first error:
```bash
docker compose exec backend bash /app/tests-start.sh -x
```

#### Test Coverage

When the tests are run, a file `htmlcov/index.html` is generated, you can open it in your browser to see the coverage of the tests.

### Migrations


* generate migration
```console
$ alembic revision --autogenerate -m "Add column last_name to User model"
```

* Upgrade

```console
$ alembic upgrade head
```

If you don't want to use migrations at all, uncomment the lines in the file at `./backend/app/core/db.py` that end in:

```python
SQLModel.metadata.create_all(engine)
```
