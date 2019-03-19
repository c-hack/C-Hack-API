FROM scratch AS source

COPY .docker/ /.docker/
COPY requirements.txt setup.py logging_config.json /app/
COPY c_hack_api /app/c_hack_api

FROM python:3.6-alpine 

COPY --from=source /.docker/requirements-docker.txt /app/
COPY --from=source /app/ /app/

RUN python3.6 -m pip install --no-cache-dir -r /app/requirements.txt
RUN python3.6 -m pip install --no-cache-dir -r /app/requirements-docker.txt
RUN python3.6 -m pip install --no-cache-dir -e /app/

WORKDIR /app

EXPOSE 80
LABEL configDir="/etc/c-hack-api.conf"

CMD ["gunicorn", "-b", "0.0.0.0:80", "--access-logfile", "-", "--error-logfile", "-", "c_hack_api:APP"]