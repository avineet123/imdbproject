# imdb movie

Restful Api managed imdb movie viewer/editor 

## Api Endpoints

- /api/movie/ 
  Method Allowed: GET, POST, HEAD, OPTIONS
  POST allowed only to admins
  Add new movie and see the list of movies
- /api/movie/{pk}/
  Method Allowed:GET, PUT, PATCH, DELETE, HEAD, OPTIONS
  PUT,PATCH,DELETE allowed only to admins
  manage and view particular movie
- /api/search/{moviename}/
  Method Allowed:GET
  search for movie that contains movie name.
- /api-token-auth/
  Method Allowed:POST
  gets authorization token on verifying credentials username and password

## Movie json data structure
    {
    "99popularity": "decimal",
    "director": "string",
    "genre": ["gene_list"],
    "imdb_score": "decimal",
    "name": "string"
    }



## To run on local machine
    python manage.py runserver --settingd=imdbproject.local

