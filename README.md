![Static Badge](https://img.shields.io/badge/Python-%23?style=for-the-badge&logo=python&logoColor=white&labelColor=%230a0a0a&color=%233776AB)
![Static Badge](https://img.shields.io/badge/Django-%23?style=for-the-badge&logo=django&logoColor=white&labelColor=%230a0a0a&color=%23092E20)
![Static Badge](https://img.shields.io/badge/Django%20REST%20Framework-%23?style=for-the-badge&logo=drf&logoColor=white&label=DRF&labelColor=%230a0a0a&color=b81414)
![Static Badge](https://img.shields.io/badge/Django%20Baton-%23?style=for-the-badge&logo=otto&labelColor=%230a0a0a&color=%23D4021D)
![Static Badge](https://img.shields.io/badge/Django%20Split%20Settings-%23?style=for-the-badge&label=DSS&labelColor=%230a0a0a&color=%23fff)
![Static Badge](https://img.shields.io/badge/Django%20Filter-%23?style=for-the-badge&label=DF&labelColor=%230a0a0a&color=%23428813)
![Static Badge](https://img.shields.io/badge/Django%20CORS%20Headers-%23?style=for-the-badge&logo=DCH&label=DCH&labelColor=%230a0a0a&color=%237F2B7B)
![Static Badge](https://img.shields.io/badge/Swagger-%23?style=for-the-badge&logo=swagger&logoColor=white&labelColor=%230a0a0a&color=%2385EA2D)
![Static Badge](https://img.shields.io/badge/Postgres-%23?style=for-the-badge&logo=postgresql&logoColor=white&labelColor=%230a0a0a&color=%234169E1)
![Static Badge](https://img.shields.io/badge/Docker-%23?style=for-the-badge&logo=docker&logoColor=white&labelColor=%230a0a0a&color=%232496ED)
![Static Badge](https://img.shields.io/badge/%20pre%20commit-%23?style=for-the-badge&logo=pre-commit&logoColor=white&labelColor=%230a0a0a&color=%23FAB040)
![Static Badge](https://img.shields.io/badge/Ruff-%23?style=for-the-badge&logo=ruff&logoColor=white&labelColor=%230a0a0a&color=%23D7FF64)
![Static Badge](https://img.shields.io/badge/nginx-%23?style=for-the-badge&logo=nginx&logoColor=white&labelColor=%230a0a0a&color=%23009639)
![Static Badge](https://img.shields.io/badge/poetry-%23?style=for-the-badge&logo=poetry&logoColor=white&labelColor=%230a0a0a&color=%2360A5FA)
![Static Badge](https://img.shields.io/badge/gunicorn-%23?style=for-the-badge&logo=gunicorn&logoColor=white&labelColor=%230a0a0a&color=%23499848)

***
# Boiler shop api
### All Environment values
#### Django environment values
* **DJANGO_SECRET_KEY** - secret key of django app.
* **DJANGO_SETTINGS_ENV** - load production or development settings
of django app. It's `production`, by default.
* **DJANGO_ALLOWED_HOSTS** - list of allowed hosts for django app.
Add needed your hosts to list django app allow you to enter on site 
by these hosts. It's `localhost [::1] 127.0.0.1 0.0.0.0` by default.
* **DJANGO_SUPERUSER_USERNAME** - username of superuser for django admin site.
It's `admin` by default.
* **DJANGO_SUPERUSER_EMAIL** - email of superuser for django admin site.
It's `admin@admin.com` by default.
* **DJANGO_SUPERUSER_PASSWORD** - password of superuser for django admin site.
It's `123` by default.
* **DJANGO_GOOGLE_EMAIL_HOST_USER** - your google email for shop.
* **DJANGO_GOOGLE_EMAIL_HOST_PASSWORD** - password of google application. 


#### Postgres environment values
- **POSTGRES_DB** - database name for Postgres. It's `postgres` by default.
- **POSTGRES_USER** - user to enter to database. It's `postgres` by default.
- **POSTGRES_PASSWORD** - user password to enter to database. 
It's `postgres` by default.
- **POSTGRES_HOST** - host for postgres. Host must be similarly 
name of docker compose service for Postgres. 
- **POSTGRES_PORT** - port for Postgres listening. It's `5432` by default.

#### Gunicorn environment values
- **GUNICORN_WORKERS** - quantity workers for gunicorn. It's `2` by default.

#### CORS environment values
- **CORS_ALLOWED_ORIGINS** - list of allowed site address with port. 

### Template of .env file with required environment values
```dotenv
DJANGO_SECRET_KEY=<secret key>
DJANGO_ALLOWED_HOSTS='localhost [::1] 127.0.0.1 0.0.0.0'
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@admin.com
DJANGO_SUPERUSER_PASSWORD=123
DJANGO_GOOGLE_EMAIL_HOST_USER=<email>
DJANGO_GOOGLE_EMAIL_HOST_PASSWORD=<password>

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=<host>
```

***
### Django admin site credential by default
- Username: admin
- Password: 123

***
### Docker commands
#### Run steck of containers
```commandline
docker compose up
```

#### Stop steck of container
```
ctrl + C
```
OR
```commandline
docker compose stop
```
#### Delete steck of containers
```commandline
docker compose down
```
with volumes
```commandline
docker compose down -v
```

If you installed docker compose as application to your OS that command must start with 
`docker-compose` instead `docker compose`.
***
### Product Filters
#### By name/s
The filter filters by a name or part of name and by multiple names or parts of names.
It isn't сase sensitive.
Example: single `names=Name`, multiple `names=Name, Name`.
- http://localhost/api/product/?names=
#### By category
The filter filters by full name of category.
It isn't сase sensitive.
Example: `cateogry=Category`
- http://localhost/api/product/?category=
#### By attribute/s
The filter filters by full name and value of attribute or multiple attributes.
It's сase sensitive.
Example: single `attributes=Name:Value`, multiple `attributs=Name:Value, Name:Value`.
- http://localhost/api/product/?attributes=
#### By price range
The filter filters by price range. Example: `min_range=1000&max_range=2000`
- http://localhost/api/product/?min_range=&max_range=
***
### Links
#### Api
- http://localhost/api/
#### Admin Site
- http://localhost/admin/
#### Swagger
- http://localhost/api/schema/swagger-ui/

#### Redoc
- http://localhost/api/schema/redoc/
