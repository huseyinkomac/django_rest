# Simple Rest API written with Python/Django Rest Framework

## Requirements
Python 3.6
Libraries to be installed in requirements.txt

## Installation
After installing libraries

## Running the Project
You can run the project through local install of python or with docker compose

### Docker
Running docker compose up from main directory will expose port 8000 and run the project

```
docker compose up -d
```

### Local Machine
Run the project with following commands

```
python manage.py migrate
python manage.py runserver
```

## Structure
Endpoint | HTTP Method | Job
-- | -- |--
`games` | GET | Get all games
`games/create`| POST | Create a new game
`games/:id` | GET | Get a single game
`games/:id` | PUT | Update a game
`games/:id` | DELETE | Delete a game
