import sys
import site

site.addsitedir('/var/www/flaskapp/lib/python3.6/site-packages')
site.addsitedir('/home/ec2-user/my_app/env/lib64/python3.6/site-packages')

sys.path.insert(0, '/var/www/Boaz_DE')

from app import app as application
