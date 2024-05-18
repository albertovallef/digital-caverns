# digital-caverns
This is my personal website and blog

# Requirements
- Python 3.9
```bash
conda activate digcaverns_dev
pip install -r requirements.txt
```
- Docker
```bash
sudo apt-get update
sudo apt-get install docker-compose-plugin
```
- Postgres
```bash
sudo apt-get update
sudo apt-get install postgresql-client
```

# Environment Variables
```.env
# PostgreSQL environment variables
POSTGRES_DB=digcavernsdb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=
POSTGRES_HOST=db  # This is the service name defined in docker-compose for PostgreSQL
POSTGRES_PORT=5432
POSTGRES_URL=db:5432  # 'db' is the service name and '5432' is the default PostgreSQL port
# Superuser credentials
DJANGO_SUPERUSER_USERNAME=
DJANGO_SUPERUSER_EMAIL=
DJANGO_SUPERUSER_PASSWORD=
# Secrets
SECRET_KEY=
# Runtime
DEBUG=1  # Use 1 for True
```

# Run (with venv)
If you wish to run the project in your venv only simply do:
```bash
python manage.py runserver
```
Ensure have a database running with configs set according to `settings.py`.

# Run (with Docker)
The easies way to run the application and avoid installing software in system.
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

Run manage.py commands:
```bash
sudo docker compose run web python manage.py <command>
```

Run migrations (example):
```bash
sudo docker compose run web python manage.py makemigrations
sudo docker compose run web python manage.py migrate 
```

# Connect to the db locally
```bash
psql -d digcavernsdb -U postgres -h localhost -p 5432
```

# Run in production
- Use `--insecure` to run with `DEBUG=False` mode
- Otherwise, need to add some webserver

