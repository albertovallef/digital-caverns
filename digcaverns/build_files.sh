echo "Installing project requirements..."
pip install -r requirements.txt
echo "Collecting static files..."
python3.9 manage.py collectstatic --clear --no-input
