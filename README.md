#  Django Dumpers Info System


## Description

- Django app for controlling dumpers information
- Models were covered with pytest tests

## Technology stack

- Python 3.11
- Django 4.1
- SQLite
- Docker (docker-compose)
- Poetry
- GitHub Actions (black/flake8 + pytest)
- Pre-Commit


## Installation

1. Go to the project directory
```
cd ~/dumper_manager
```
2. Set environment variables to the .env file

```
cp .env.example .env
```
3. Run docker-compose:

```
docker-compose up -d
```

In case you want to stop docker-compose:
````
docker-compose stop
````
***
# URL Guideline:

`http://0.0.0.0:8000/dumpers/` - List of all dumpers

`http://0.0.0.0:8000/dumpers/?model=<model_name>` - List of all dumpers with certain model
***

# Main Features

- **Get full information about your dumpers**

- **Filter dumpers list by choosing particular model name**

- **Enjoy BELAZ!!!**

***
