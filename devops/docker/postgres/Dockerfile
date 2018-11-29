FROM postgres:9.6.5-alpine

# Attention: This script is only run, when no database exists
COPY init.sh /docker-entrypoint-initdb.d/

RUN chmod +x /docker-entrypoint-initdb.d/init.sh

HEALTHCHECK CMD pg_isready -U postgres
