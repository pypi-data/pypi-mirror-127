===============
Frontadmin
===============

Frontadmin is a django app to conduct web-based frontend admin. This is not replace your actual admin however you can build admin like functionality in frontend.

Quick start
-----------

1. Add "frontadmin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        'frontadmin', #Add this exactly in top
        ...
        'django.contrib.humanize', #Add this exactly in last
    ]

2. Add below commands in your settings.py::

    SITE_NAME = 'YOUR_SITE_NAME'

3. Include the frontadmin URLconf in your project urls.py like this::

    path('', include('frontadmin.urls')),

4. Run below command::
    
    python manage.py migrate

5. Start the development server and visit http://127.0.0.1:8000/

I publish this package for my personal use to minimize the common task 
however if someone found this usefull and want to know how it works please create 
issue in project github.