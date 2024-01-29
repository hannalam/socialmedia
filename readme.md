# List of development environment:

operating system: Window 11
python version: Python 3.10.11

Logging into django-admin:

# super user

username: user
password: user1234

# How to run the unit test:

python manage.py test

# Location of the data loading script

social/socialmedia/db.sqlite3

# How to run this web

python -m pip install virtualwrapper
py -3 -m venv .venv
.venv\scripts\activate
cd socialmedia
pip install -r requirements.txt
python manage.py runserver 127.0.0.1:8080

# URLS

Admin page
http://127.0.0.1:8000/admin

Django REST framework A P I
http://127.0.0.1:8000/users

Home page
http://127.0.0.1:8000/status/main

# Reference of media used

logo https://www.transparentpng.com/thumb/instagram-logo-icon/JdEuI8-instagram-logo-images-png-icon.png
like https://icons.veryicon.com/png/o/miscellaneous/ui-basic-linear-icon/like-106.png
comment https://cdn-icons-png.flaticon.com/512/5338/5338282.png
share https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Noun_Project_Share_icon_3282968.svg/2048px-Noun_Project_Share_icon_3282968.svg.png
