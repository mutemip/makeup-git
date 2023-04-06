
# How to install this project
---

### Create Venv
- Do this:
``mkdir myfolder`` , ``cd myfolder`` , 
- Run this command:
``python -m venv myenv `` OR ``pipenv install django `` OR ``virtualenv myenv``

### Activate venv
Use this command: - ``.\myenv\Scripts\actvate`` for `Windows`
                  - ``source/myenv/bib/activate`` for `Linux`

### INstall Django
Use this: ``pip install django``

### create django project
Use this: ``django-admin startproject myproject``

### create django app
use this: - `` django-admin startapp myapp`` OR
        - ``python manage.py startapp myapp``

### makemigrations
``python manage.py makemigrations`` then this: ``python manage.py migrate``

### Learn about
``sqlmigrate`` and ``showmigrations``

