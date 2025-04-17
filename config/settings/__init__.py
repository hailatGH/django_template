import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "DEV")

if ENV == "STG":
    from config.settings.stg import *
elif ENV == "PROD":
    from config.settings.prod import *
else:
    from config.settings.dev import *
