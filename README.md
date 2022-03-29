# Cookiecutter_Django

A Boilerplate for all Django projects to prevent you from doing all the boring configuration stuff. Contains only essential portions that every Django requires.

## What Comes out of the Box?

* Django 3.0
* Works with Python 3.8
* Pre-configured Postgress Database.
* Separate branch for development and deployment(master) using Docker, Nginx, Gunicorn.
* DjangoRestFramework installed.
* .gitignore for Django projects (copied from gitignore.io).

## Installing Dependencies

It requires very minimal dependencies and if you are already into development, chances are high that you would just need to hit one command and you will be good to GO! or else you'll have to figure out how to install docker and docker-compose on your system to get ready.

### Install Cookiecutter

```
$ sudo pip3 install cookiecutter
```

## Usage

You can either clone this repository or can run it against this repository.

Navigate to the folder where you want to start your Django Project and run the following command.

* Running it against this repository.
```
$ cookiecutter https://github.com/cry0egnic/Cookiecutter_Django.git
```

* Running it using repository clone.

```
$ git clone https://github.com/cry0genic/Cookiecutter_Django.git
$ cookiecutter <path-to-clone>
```

**You will be prompted for some values.**<br />
You can enter custom values if you wish to or can just hit Enter to use the default ones.<br />
**Don't use a App name that has "_".**<br />

```
repo_name [repo_name]: <Enter name of Django Project.>
app_name [main]: <Enter app name you want inside of the Django Project.>
POSTGRES_USER [postgres]:
POSTGRES_PASSWORD [postgres]:
DJANGO_SECRET_KEY [djangosecretkey]:
```

To check if everything is working fine go to the project directory and run
```
$ docker-compose up
```
and now visit localhost:8000, you can also visit localhost:8000/admin to check if static files are loading correctly.<br />

Use source code in **development branch during development** so you don't have to rebuild docker image every time you make changes to your django project. All the static files will be served using nginx in deployment mode and visit your project at localhost:1337 in deployment mode.

