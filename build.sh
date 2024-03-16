#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
python3.9 manage.py migrate