# Election Portal - IIT (BHU)
IIT (BHU) Election Portal is a dynamic web application built on Django 1.10 that helps to conduct elections over the internet/LAN for the university.
This web application is developed with the aim of reducing the hustle/fuss and human errors while conducting elections manually. It drastically reduces the resources involved and efficiently produces the result.

## Dependencies
- Python 2.7
- Django 1.10
- PostgreSQL

## Installation
1. Install PostgreSQL. See [this](https://www.postgresql.org/docs/9.2/static/installation.html) for more details.
2. Install Python 2.7. See [this](https://docs.python.org/2/using/index.html) for more details.
3. Install Django 1.10 using ``pip``:

        pip install django==1.10
  

## Usage
1. Create a superuser (admin) for handling the web app. `cd` to root of the project and enter in terminal:

        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser
    
2. Enter your username, email and password.
3. Enter following in terminal to run server on localhost:
        
        python manage.py runserver

4. Visit [http://localhost:8000](http://localhost:8000) to view the app. Login to admin area [http://localhost:8000/admin](http://localhost:8000/admin) to create, manage, edit and delete elections and users. Create election, add voters from the list of users to the election, enter the nomination and voting's start and end time.


## Contributors

  - [Karthik Kumar](https://github.com/codekika)
  - [Pranjal Jain](https://github.com/praran26)
  - [Rathi Saurabh Bhagirath](https://github.com/saurabhrathi12)
  - [Vinay Jaisinghani](https://github.com/vinayjaisinghani)