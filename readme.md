# limitation des sites qui peuvent accéder à l' API
# A ne pas decommenter

```PYTHON
CORS_ALLOWED_ORIGINS = [
    "https://nanweb.herokuapp.com",
    "http://127.0.0.1:8000",
]

X_FRAME_OPTIONS = 'SAMEORIGIN' à mettre dans le settings 

```