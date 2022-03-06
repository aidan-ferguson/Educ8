%echo off
echo Y | del /f .\db.sqlite3
echo Y | del /f  .\Educ8\migrations
python .\manage.py makemigrations Educ8
python .\manage.py migrate
python .\manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')"
echo:
echo:
echo Username : admin
echo Password : password