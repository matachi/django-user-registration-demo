#!/bin/bash -e

# Linux user account that will be owner of created folders
USER=''

# virtualenv folder name
ENV='env'

# Where it's being installed
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if USER is empty
if [[ $USER == "" ]]; then
echo "ERROR: USER is empty. Add your Linux username."
    exit 1
fi

# Check if the script is being run as root
if [ $EUID -ne 0 ]; then
echo "ERROR: Must be run as root."
    exit 1
fi

# Store if python-virtualenv is installed
PYTHON_VIRTUALENV_INSTALLED=$(pacman -Qs python2-virtualenv)

# Install virtualenv
if [ -n $PYTHON_VIRTUALENV_INSTALLED ]; then
    pacman -Sy python2-virtualenv
fi

# Set up a virtualenv
sudo -u $USER virtualenv2 $ENV

# Install django and dependencies
sudo -u $USER $ENV/bin/pip install django==1.5.1 djangorestframework==2.3.6 -e git+https://github.com/MaTachi/django-userena.git#egg=django-userena django-breadcrumbs==1.1.3-p1 Pillow==2.1.0 django-widget-tweaks==1.3

# Update the project's folder path in accountdemo/settings.py
ESCAPED_DIR=$(sed 's/\//\\\//g' <<< "$DIR")
sed -i -e "s/INSERT_PROJECT_FOLDER/$ESCAPED_DIR\//g" $DIR/accountdemo/settings.py

# Generate a secret key in the same way as in: https://github.com/django/django/blob/master/django/core/management/commands/startproject.py
SECRET_KEY="$( echo -e "from django.utils.crypto import get_random_string\nchars='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'\nprint(get_random_string(50,chars))" | $ENV/bin/python )"
# Escape &
SECRET_KEY=$(sed 's/\&/\\\&/g' <<< $SECRET_KEY)

# Insert secret key into accountdemo/settings.py
sed -i -e "s/INSERT_SECRET_KEY/$SECRET_KEY/g" $DIR/accountdemo/settings.py

# Syncdb
sudo -u $USER $ENV/bin/python manage.py syncdb

# Insert some sample data into the DB
sudo -u $USER $ENV/bin/python insert_sample_db_data.py
