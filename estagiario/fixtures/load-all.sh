#!/bin/bash

echo "address.State.yaml"
python manage.py loaddata fixtures/address.State.yaml

echo "address.City.yaml"
python manage.py loaddata fixtures/address.City.yaml

echo "internships.Field"
python manage.py loaddata fixtures/internships.Field.yaml

#python manage.py loaddata fixtures/address.City.yaml