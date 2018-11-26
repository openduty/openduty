FROM redis:3.2.10-alpine

COPY healthcheck.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/healthcheck.sh

HEALTHCHECK CMD sh /usr/local/bin/healthcheck.sh

EXPOSE 6379
