#!/bin/bash
python manage.py collectstatic && gunicorn --workers 2 office_emppro.wsgi