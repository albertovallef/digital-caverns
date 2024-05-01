# Use the official PostgreSQL image from the Docker library
FROM postgres:15

# Run any additional commands you require
RUN echo "Custom scripts or configurations can go here"

# Example: Increase the default connection limit
COPY ./custom-config.conf /etc/postgresql/postgresql.conf
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]

