# digital-caverns
This is my personal website and blog

# Requirements
- Python 3.9
    - Install `requirements.txt`
- Docker
    - docker compose plugin
- Postgres
    - `postgresql-client`

# Run (with venv)
```bash
python manage.py runserver
```

# Run (with Docker)

Bring service up:
 ```bash
 sudo docker compose up
 ```

 Verify services are running:
 ```bash
sudo docker ps
 ```

 Bring services down: 
 ```bash
 sudo docker compose down -v 
 ```

 Run migrations
 ```bash
 sudo docker compose run web manage.py makemigrations
 sudo docker compose run web manage.py migrate 
 ```

# Connect to the db locally
```bash
psql -d digcavernsdb -U postgres -h localhost -p 5432
```

