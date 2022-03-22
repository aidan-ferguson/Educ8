import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_group_project.settings')
import django
django.setup()
from django.contrib.auth import get_user_model

admin_username = "admin"
admin_password = "password"
db_path = "./db.sqlite3"
migrations_dir = "./Educ8/migrations"

print("Re-migrating database")

if os.path.exists(db_path):
    os.remove(db_path)

if os.path.exists(migrations_dir):
    for item in os.listdir(migrations_dir):
        if os.path.isfile(item):
            os.remove(os.path.join(migrations_dir, item))

os.system("python manage.py makemigrations Educ8")
os.system("python manage.py migrate")

get_user_model().objects.create_superuser(admin_username, 'admin@admin.com', admin_password)

print(f"\nRe-migrated with following credentials for the admin account:\n\tusername: {admin_username}\n\tpassword: {admin_password}")