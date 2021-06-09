from decouple import config

from settings.base_settings import *

env = config("ENVIRONMENT", "DEV")

if env == "DEV":
    from settings.local_settings import *
elif env == "PROD":
    from settings.prod_settings import *
