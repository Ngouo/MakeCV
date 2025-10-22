#!/bin/bash

pip install -r requirements.txt

# Configuration PyMySQL
echo "import pymysql\npymysql.install_as_MySQLdb()" >> MakeCV/__init__.py

# Collecte des fichiers statiques
python manage.py collectstatic --noinput