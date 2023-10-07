import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the directory containing your Django project to the Python path
project_home = '/home/myusername/JUSTGYM'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate your virtual environment
activate_this = os.path.join(project_home, 'mysite-virtualenv/bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Set the DJANGO_SETTINGS_MODULE to your project's settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

# Create the WSGI application
application = get_wsgi_application()
