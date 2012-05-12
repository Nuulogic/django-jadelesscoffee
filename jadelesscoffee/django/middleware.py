from django.conf import settings

class JadeLessCoffeeMiddleware(object):
    def __init__(JadeLessCoffeeMiddleware):
        #only run this guy if DEBUG is True
        if settings.DEBUG is not None and settings.DEBUG is False:
            raise django.core.exceptions.MiddlewareNotUsed
        else:
            print('JadeLessCoffee compiler will run at every request...\n');

    def process_request(self, request):
        #for each template directory look for a src dir
        if (isinstance(settings.TEMPLATE_DIRS, tuple)):
            for template_directory in settings.TEMPLATE_DIRS:
                self.compile(template_directory + '/src', template_directory)
        else:
            self.compile(settings.TEMPLATE_DIRS + '/src', settings.TEMPLATE_DIRS)

        #same with settings.STATICFILES_DIRS
        if (isinstance(settings.STATICFILES_DIRS, tuple)):
            for template_directory in settings.STATICFILES_DIRS:
                self.compile(template_directory + '/src', template_directory)
        else:
            self.compile(settings.STATICFILES_DIRS + '/src', settings.STATICFILES_DIRS)

        #settings.STATIC_ROOT shouldn't be left out.
        self.compile(settings.STATIC_ROOT + '/src', settings.STATIC_ROOT)
            

    def compile(self, source_directory, output_directory):
        from subprocess import call
        call(['jlc', '--quiet', '--incremental', '--out', output_directory, source_directory])
