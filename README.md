django-jadelesscoffee
=====================

JadeLessCoffee for Node.js is a quick compiler for Jade, LessCSS, and CoffeeScript. This is a Django middleware for processing templates/src on the fly using it.

IMPORTANT
=========

django-jadelesscoffee is *not* meant for a production environment. **It is slow.** Consequently, this middleware will only run on the Django development server.

Requirements
------------

**JadeLessCoffee** Node.js module. (Note that this is currently in a closed alpha state until it can be a proven technique.)


Installation
------------

`$ pip install git+https://github.com/Nuulogic/django-jadelesscoffee.git`

Then in your Django application, include this middleware:
`MIDDLEWARE_CLASSES = (
    ...
    'jadelesscoffee.django.middleware.JadeLessCoffeeMiddleware'
)`

Then add a 'src' folder in any of the TEMPLATE_DIRS and STATICFILES_DIRS entries you want to have .jade, .less, or .coffee files in.

The following commands will run at each request and will only compile files that have changed.
`jlc --quiet --incremental --output {{TEMPLATE_DIRS}} + '/src' {{TEMPLATE_DIRS}}`
`jlc --quiet --incremental --output {{STATICFILES_DIRS}} + '/src' {{STATICFILES_DIRS}}`

