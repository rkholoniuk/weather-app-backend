# weather-app-backend

Create and source a virtual environment (Python 3.10.0):
```
eval "$(pyenv init -)"
```

```
python3 -m venv venv
source venv/bin/activate
```
Run project
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```