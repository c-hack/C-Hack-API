#!/usr/bin/env bash

. venv/bin/activate
export FLASK_APP=c_hack_api
export FLASK_DEBUG=1  # to enable autoreload
export FLASK_ENV=debug

flask create_db

# start server
flask run
