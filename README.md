##  Installation
First **clone** this project.
```sh
$ git clone https://github.com/MohamadMansourii/django_blog.git
```
Then create **docker network** and **volumes** as below.

```sh
$ docker volume create blogProject_postgresql
```
```sh
$ docker network create blogProject_network
```
Now run postgresql with **docker-compose**.
```sh
$ docker-compose up -d
```
Before run project, we need to import the following commands in Terminal
> (This command create table of database in postgresql)

```python
python manage.py makemigrations
```
and
```python
python manage.py migrate
```

Run Project with this Command:

```python
./manage.py runserver
```

Or

```python
python manage.py runserver
```
