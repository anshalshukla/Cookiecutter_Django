from django.apps import AppConfig


class {{cookiecutter.app_name[0]|upper}}{{cookiecutter.app_name[1:]|lower}}Config(AppConfig):
    name = '{{cookiecutter.app_name}}'
