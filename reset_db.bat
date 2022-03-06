%echo off
del /f .\db.sqlite3
del /f  .\Educ8\migrations
python .\manage.py makemigrations Educ8
python .\manage.py migrate
python .\manage.py createsuperuser