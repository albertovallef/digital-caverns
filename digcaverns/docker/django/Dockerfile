# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Create superuser
RUN python create_admin.py

# Copy project
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput  # Collect static files

# Run the application
CMD ["python", "manage.py", "runserver", "--insecure", "0.0.0.0:8000"]

