from settings import *

class JadeLessCoffeeMiddleware(object):
    def __init__(JadeLessCoffeeMiddleware):
        if DEBUG is not None and DEBUG is False:
            raise django.core.exceptions.MiddlewareNotUsed
        else:
            print('JadeLessCoffee compiler will run at every request...\n');

    def process_request(self, request):
        #For the safety of your /real/ server, we're only going to do the jlc compile on development servers.
        server = request.META.get('wsgi.file_wrapper', None)
        if server is not None and server.__module__ == 'django.core.servers.basehttp':
            #for each template directory look for a src dir
            if (isinstance(TEMPLATE_DIRS, tuple)):
                for template_directory in TEMPLATE_DIRS:
                    self.compile(template_directory + '/src', template_directory)
            else:
                self.compile(TEMPLATE_DIRS + '/src', TEMPLATE_DIRS)

            #same with STATICFILES_DIRS
            if (isinstance(STATICFILES_DIRS, tuple)):
                for template_directory in STATICFILES_DIRS:
                    self.compile(template_directory + '/src', template_directory)
            else:
                self.compile(STATICFILES_DIRS + '/src', STATICFILES_DIRS)
            

    def compile(self, source_directory, output_directory):
        from subprocess import call
        call(['jlc', '--quiet', '--incremental', '--out', output_directory, source_directory])
