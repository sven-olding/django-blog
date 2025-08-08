# Example Django Blog Application

This application uses uv as a package manager

## Setup
run the following command from the project root
```shell
uv sync
```
to install all the necessary stuff 


### DB Migrations

If starting first time run the db migrations

```shell
uv run manage.py migrate
```

and create an admin user:

```shell
uv run manage.py createsuperuser --username admin --email admin@example.com
```

## Start dev server

cd into blog and run as regular django app

```shell
cd blog
uv run manage.py runserver
```

## Formatting/Linting

This project uses [ruff](https://github.com/astral-sh/ruff) as a linter/formatter. You can run 
```shell
uv run ruff check
``` 
for checking the code or with the `--fix` option to fix all "fixable" errors
```shell
uv run ruff check --fix
```
Use the following command to format
```shell
uv run ruff format
```

### pre-commit hook

This project also uses [pre-commit](https://pre-commit.com/) with a ruff pre-commit hook so formatting/linting can be applied upon committing. Use the following command to install:
```shell
uv run pre-commit install
```