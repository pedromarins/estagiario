rm db.sqlite 
./manage.py syncdb
./manage.py migrate

./manage.py loaddata fixtures/internships.Field.yaml 

./manage.py runscript mock_site