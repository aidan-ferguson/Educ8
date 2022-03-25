import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_group_project.settings')
import django
from django.contrib.auth import get_user_model

def reset():
    print("Re-migrating database")

    admin_username = "admin"
    admin_password = "password"
    db_path = "./db.sqlite3"
    migrations_dir = "./Educ8/migrations"
    media_files_dir = "./media/files"

    for root, dirs, files in os.walk(media_files_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    if os.path.exists(db_path):
        os.remove(db_path)

    if os.path.exists(migrations_dir):
        for item in os.listdir(migrations_dir):
            if os.path.isfile(item):
                os.remove(os.path.join(migrations_dir, item))

    django.setup()

    os.system("python manage.py makemigrations Educ8")
    os.system("python manage.py migrate")

    get_user_model().objects.create_superuser(admin_username, 'admin@admin.com', admin_password)

    print(f"\nRe-migrated with following credentials for the admin account:\n\tusername: {admin_username}\n\tpassword: {admin_password}")

if __name__ == "__main__":
    reset()