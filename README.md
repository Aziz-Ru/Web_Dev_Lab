# To create Virtual Environment to install Django in Ubuntu

##### If you dont have venv then install it

`sudo apt install python3-venv`

##### To create environment ` python3 -m venv my_env`

##### Activate the environment `source my_env/bin/activate`

##### Deactivate the environment `deactivate `

##### Install django `python3 -m pip install Django`

##### If you want to install django specifiq version `python3 -m pip install Django==3.2`

##### Create A project `django-admin startproject mysite`

##### Create App `python3 manage.py startapp app_name`

##### Migrate database run `python3 manage.py migrate`

# To deploy Your Django app in Vercel

### create `vercel.json` file of your project directory and paste this line of code and change projectname your actaul project name:

```
{
  "version": 2,
  "builds": [
    {
      "src": "projectname/wsgi.py",
      "use": "@vercel/python",
      "config": { "maxLambdaSize": "15mb", "runtime": "python3.11" }
    },
    {
      "src": "build_files.sh",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "staticfiles_build"
      }
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "projectname/wsgi.py"
    }
  ]
}

```

### To create `requirements.txt` run this `pip freeze > requirements.txt`

### Create a file name `build_files.sh` in your project directory and paste this line of code

```
# build_files.sh
pip install -r requirements.txt
python3.9 manage.py collectstatic
#here you must be give python3.9
```

### Modify setting.py-------

##### In import section

```
import os
##Change in Allowed host
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', '.now.sh']
```

##### If you don't have install postgresql please Comment Database setion of setting.py

```
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}
```

##### Below the `STATIC_URL = 'static/'` paste this lines of code:

```
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles_build','static')

```

### Modify urls.py-------

##### Import section add these line code:

```
from django.conf import settings
from django.conf.urls.static import static
```

#### Add this line of code below `urlpatterns` list :

```
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```

### -------

### Modify in wsgi.py

#### Add this at the end

```
app=application
```

## Now Push Your code in Github and Create a account in vercel.com with github.com

# Installed Postgresql Database in ubuntu

### Just go to the postges website and copy and pase the command to install postgres shell and pgadmin4 .

#### To Show psql version

```
psql --version
```

#### Navigate back to the Postgres shell and run the following commands consecutively

```
sudo -i -u postgres
```

#### To interact with the database server run

```
psql
```

#### To create Database user & password run this

```
CREATE USER username WITH PASSWORD 'password';
```

#### To create a database run this

```
CREATE DATABASE db_name;
or
createdb db_name
```

#### To delete a database run this

```
DROP DATABASE db_name;
```

#### To see list of db here

```
\l
```

#### To see list of user

```
\du
```

#### Delete user

```
DROP USER IF EXISTS username;
//if this command not working  show cannot be dropped because some objects depend on it//
Reassign the user  run this command
REASSIGN OWNED BY username TO postgres;
and the drop
DROP OWNED BY username;



```

#### To connect db run `\c db_name`

# Install postgresql in Django

#### To install postgresql in virstual environment run

```
pip install psycopg2-binary
```

#### To change requirement.txt file run

```
pip freeze > requirements.txt
```

#### Now Change in setting.py DATABASE section

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_name',
        'USER': 'user_name',
        'PASSWORD': 'password_of_user',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

```

#### Alter database owner from postgres to user

```
ALTER DATABASE my_db OWNER TO user;
```

#### To migrate database run `python3 manage.py migrate`.

#### If You face Error :

```
django.db.migrations.exceptions.MigrationSchemaMissing: Unable to create the django_migrations table (permission denied for schema public
LINE 1: CREATE TABLE "django_migrations"
```

#### Go your psql shell and GRANT the the databse to user

```
GRANT ALL ON DATABASE mydb TO myuser;
 and
ALTER DATABASE my_db OWNER TO myuser;
```
