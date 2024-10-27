#!/bin/bash

python3 manage.py makemigrations core
python3 manage.py makemigrations steprepo
python3 manage.py makemigrations testcatalog
python3 manage.py migrate
