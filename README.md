# To deploy Your Django app in Vercel

##### create `vercel.json` file in root directory of your project paste this line of code and change projectname your actaul project name:

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
# change projectname your actual projectname

```

##### To create `requirements.txt` run this `pip freeze > requirements.txt`.

##### create a file name `build_files.sh` in root directory of your project paste this line of code

```
# build_files.sh
pip install -r requirements.txt
python3.9 manage.py collectstatic
#here you must be give python3.9
```

#### In setting.py file of project `import os` in import section and modify ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', '.now.sh'] and below the STATIC_URL paste this lines of code

```
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles_build','static')

```

#### If you don't have install postgresql please Comment Database setion of setting.py

```
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}
```

#### In urls.py add this line code in import section

```
from django.conf import settings
from django.conf.urls.static import static
```

#### add this line of code below urlpatterns like that:

```
urlpatterns = [
###
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```

## Now Push Your code in Github and Create a account in vercel.com with github.com

# Installed Postgresql Database in ubuntu

### Just go to the postges website and copy and pase the command to install postgres shell and pgadmin4 .

#### To Show psql version `psql --version`.

#### Navigate back to the Postgres shell and run the following commands consecutively` sudo -i -u postgres`.

#### To interact with the database server run ` psql`.

#### To create Database user & password run this ` CREATE USER username WITH PASSWORD 'password';`.

#### To create a database run this `CREATE DATABASE db_name; ` or `createdb db_name `.

#### To delete a database run this `DROP DATABASE db_name;`.

#### To see list of db here `\l`.

#### To connect db run `\c db_name`.

# Install postgresql in Django

#### To install postgresql in virstual environment run `pip install psycopg2-binary`.

#### To change requirement.txt file run `pip freeze > requirements.txt`.

#### Now Change in setting.py DATABASE section

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_name',
        'USER': 'user_name_of_psql',
        'PASSWORD': 'password_pf_psql',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

```

#### To migrate database run `python3 manage.py migrate`.

#### If You face Error :

```
django.db.migrations.exceptions.MigrationSchemaMissing: Unable to create the django_migrations table (permission denied for schema public
LINE 1: CREATE TABLE "django_migrations"
```

#### Go your psql shell and GRANT the the databse to user`GRANT ALL ON DATABASE mydb TO myuser;` and `ALTER DATABASE my_db OWNER TO myuser;`.
