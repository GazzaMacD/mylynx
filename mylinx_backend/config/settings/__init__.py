# your_project_name/settings/__init__.py
import os

if os.getenv("DJANGO_SETTINGS_MODULE_ENV") == "production":
    from .production import *
else:
    from .dev_gareth import *
