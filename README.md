# django-api
    Django directory structure and api basic settings
------
**VERSION**
> python 3.11<br>
> pip 23.0.1<br>
> django 4.1.7<br>

### Directory Structure
    repo
    ├── apps
    │   └── app_1
    │       ├── admin.py
    │       ├── apps.py
    │       ├── migrations
    │       ├── models.py
    │       └── v1                   # versioning
    │           ├── serializers
    │           ├── tests
    │           ├── utils            
    │           └── views
    ├── common                       # all apps use class, function etc...
    ├── manage.py
    ├── project                      # main project directory
    │   ├── admin.py
    │   ├── asgi.py
    │   ├── env.py                   # environment
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── static                       # can be generated [ manage.py collectstatic ]
    └── templates
        └── admin
            └── base.html            # set admin site design


### Getting Start
1. **Make Project**
<!-- <br/> -->
    django-admin startproject {project_name} {path (want to makr current directory use . )}

2. **Make App**
<!-- <br/> -->
    python3 manage.py startapp {app_name}

3. **Docs**
<!-- <br/> -->
    Setting docs: repo/docs/settings.md
    Admin docs: repo/docs/admin.md
