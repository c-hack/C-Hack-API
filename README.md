# C-HackAPI
The C-Hack API

##Deployment
The easiest method to deploy this software is with docker.
Create a configuration file on the host. (See Section Config)
Run a container with `docker run -p <host_port>:80 -v <host_conf_file>:/etc/c-hack-api.conf cminushack/c-hack-api`

##Config
The config file are key value pairs like this: `KEY = value`. The value is in python notation. E.g. `KEY = 'string'` or `KEY = ['string1', 'string 2']`.
Config Key | Example | Description
--- | --- | ---
SQLALCHEMY_DATABASE_URI | `sqlite:////etc/data.db` | The uri to the database.
URI_BASE_PATH | `/` | The base path used to build uris
LOGGING_CONFIGS | `['logging_config.json']` | A list of logging config files.
DB_UNIQUE_CONSTRAIN_FAIL | `UNIQUE constraint failed` | The unique constraint failed message of the database in use. (To be able to return correct error codes)

## Development
### Setup dev env

```shell
# setup virtualenv
virtualenv venv # or python -m venv venv
. venv/bin/activate


# install requirements
pip install -r requirements_developement.txt
pip install -r requirements.txt

pip install -e . 
```

### Start server
```shell
./start.sh
```
