#!/bin/bash

python manage.py loaddata fixtures/address.State.yaml
python manage.py loaddata fixtures/address.City.yaml