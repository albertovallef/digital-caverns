echo "Installing project requirements..."
pip install -r requirements.txt

echo "Applying migrations to databse..."
python3.9 manage.py migrate --noinput

echo "Collecting static files..."
python3.9 manage.py collectstatic --clear --no-input
