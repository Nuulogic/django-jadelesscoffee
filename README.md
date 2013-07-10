django-jadelesscoffee
=====================

JadeLessCoffee for Node.js is a quick compiler for Jade, LessCSS, and CoffeeScript. This is a Django middleware for processing templates/src on the fly using it.

IMPORTANT
=========

django-jadelesscoffee is *not* meant for a production environment. **It is slow.** Consequently, this middleware will only run on the Django development server.

Requirements
------------

**JadeLessCoffee** Node.js module. (Note that this is currently in beta until it can be a proven technique.)


Installation
------------

`$ pip install django-jadelesscoffee`

Then in your Django application, include this middleware:
`MIDDLEWARE_CLASSES = (
    ...
    'jadelesscoffee.django.middleware.JadeLessCoffeeMiddleware'
)`

Then add a 'src' folder in any of the TEMPLATE_DIRS and STATICFILES_DIRS entries you want to have .jade, .less, or .coffee files in.

The following commands will run at each request and will only compile files that have changed.
`jlc --quiet --incremental --python --out {{TEMPLATE_DIRS}} + '/src' {{TEMPLATE_DIRS}}`
`jlc --quiet --incremental --python --out {{STATICFILES_DIRS}} + '/src' {{STATICFILES_DIRS}}`

