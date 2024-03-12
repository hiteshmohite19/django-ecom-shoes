from .base import *


CORS_ORIGIN_ALLOW_ALL = False
ALLOWED_HOSTS = ["localhost", "localhost:3000", "127.0.0.1:3000"]
CORS_ORIGIN_WHITELIST = (
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
)

AUTH_USER_MODEL = "users.User"
