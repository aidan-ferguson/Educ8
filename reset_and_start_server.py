from reset_db import reset
from populate_educ8 import populate
import os

print("Removing old migrations and media files, and migrating database")
reset()
print("Reset complete")
print("Database re-migrated")
print("Populating")
populate()
print("Populated")
print("Running server")
os.system("python manage.py runserver")