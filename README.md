# Django User Registration Demo

Django site with user registration functionality powered by
[Userena](http://docs.django-userena.org/en/latest/).

Copyright (C) 2013 Daniel Jonsson,
[@DanielJonss](https://twitter.com/DanielJonss)  
Licensed under [GNU GPL version 3 or later](LICENSE)

## Setup

1. Open [setup.sh](setup.sh) and add your Linux username to `USER=''`.
2. Run `$ sudo ./setup.sh` to install dependencies, populate the database,
   config the settings file, etc. Note: It's configured to use pacman for
installing packages, but this can easily be changed.

## Run local server

1. `$ source env/bin/activate`
2. `$ ./manage.py runserver`
3. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a web browser to
   play with the app.

## Libraries & frameworks

* [Django](https://www.djangoproject.com/) licensed under the [Modified BSD
  License](https://github.com/django/django/blob/master/LICENSE)
* [Userena](http://docs.django-userena.org/en/latest/) licensed under the
  [Modified BSD
License](https://github.com/bread-and-pepper/django-userena/blob/master/LICENSE)
* [Django REST framework](http://django-rest-framework.org/) licensed under [a
  modified BSD License](http://django-rest-framework.org/#license).
* [Django Breadcrumbs](https://github.com/chronossc/django-breadcrumbs)
  licensed under the [Modified BSD
License](https://github.com/chronossc/django-breadcrumbs/blob/master/LICENSE)
* [django-widget-tweaks](https://github.com/kmike/django-widget-tweaks/)
  licensed under the [MIT
License](https://github.com/kmike/django-widget-tweaks/blob/master/LICENSE)
* [Twitter Bootstrap](http://getbootstrap.com/) licensed under [Apache License
  2.0](http://getbootstrap.com/getting-started/)
* [jQuery](http://jquery.com/) licensed under the [MIT
  License](https://jquery.org/license/)
* [Font Awesome](http://fontawesome.io/) licensed under [SIL OFL 1.1 and MIT
  License](http://fontawesome.io/license/)
