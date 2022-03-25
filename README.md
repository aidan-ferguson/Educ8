# Educ8 - WAD2 Django Group Project
Educ8 is an online learning platform created as coursework. Educ8 allows teachers to create courses and add files and students to courses. Students can add flashcards to courses they have been added to, in addition to viewing files uploaded by the teacher.
Educ8 features a full authentication system with registration, login and account editing pages.


![educ8 logo concept](https://user-images.githubusercontent.com/98108156/156836592-98af42b2-9a45-4205-8703-00644300d645.png)

# Running Educ8
### Requirements
All requirements needed to run Educ8 can be found in `requirements.txt`. To install these navigate to the root directory of the project and run:
`pip install -r requirements.txt`
Note, Educ8 has been created using python 3.8-3.9, however other python 3 versions may work

### Running Manually
If you want to run manually run the following commands:
`python manage.py makemigrations Educ8`
`python manage.py migrate`
then, if you wish to populate the database, run:
`python populate_educ8.py`
finally, to run the webserver:
`python manage.py runserver`

### Running automatically
During development, we created a utility script to
- Delete old migrations
- Re-migrate the database
- Set default admin username and password
- Populate the database
- Run the server
It can be run with the following command:
`python reset_and_start_server.py`

### Unit testing
Unit tests are located in `Educ8/tests.py` and can be run with the following command:
`python manage.py test`