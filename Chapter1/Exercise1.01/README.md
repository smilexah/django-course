If django-admin not found, set this script in your cmd:

    $ setx PATH "%PATH%;C:\Users\Meiirzhan\AppData\Roaming\Python\Python313\Scripts"

    SUCCESS: Specified value was saved.

Then you can use django-admin instead of:

    python -m django startproject bookr

To create project use command:

    django-admin startproject bookr

To run the server use command:

    python manage.py runserver

Before creating new app use command:

    cd bookr/

To create new app into the project execute the command:

    python manage.py startapp reviews
