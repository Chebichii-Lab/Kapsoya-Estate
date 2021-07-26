# KAPSOYA ESTATE

## Author
Natasha Serem

### Description
This is a Django application of a neighburhood where a user can add a neighbourhood, join a neighbourhood that has been displayed, view various busineese, add a post that the whole neighbourhood can view and also be able to leave the neighbourhood.

### Setup and Installations
To get the code, clone the repository:
And run the following commands;

    $ cd Kapsoya-Estate
    $ pip install -r requirements.txt

### Install and activate the virtual emvironment

    $ python3.8 -m venv virtual
    $ source virtual/bin/activate

### Create database 

    $ psql
    $ CREATE DATABASE (name_of_databse);

### Make migrations 

    $ python3.8 manage.py check
    $ python3.8 manage.py makemigrations (app_name)
    $ python3.8 manage.py migrate 

### Testing the application 
 
    $ python3.8 manage.py test (app_name)

### Running the Application

    $python3.8 manage.py runserver

Then once you are done, open your browser with the local host; 127.0.0.1:8000

## Dependencies
1. python3.8
2. Django 3.2.5
3. Virtual environment
4. Heroku
5. Gunicorn

## Technologies used
1. python 3.8.10
2. HTML
3. Django 3.2.5
4. Bootstrap 3
5. Heroku
6. Postgresql

# Live Link
View [live](https://kapsoya254.herokuapp.com/).


