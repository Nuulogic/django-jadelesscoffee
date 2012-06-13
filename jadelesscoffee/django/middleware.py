from django.conf import settings
from os import path
import sys
import os

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
                self.compile(path.normpath(template_directory + '/src'), template_directory)
        else:
            self.compile(path.normpath(settings.TEMPLATE_DIRS + '/src'), settings.TEMPLATE_DIRS)

        #same with settings.STATICFILES_DIRS
        if (isinstance(settings.STATICFILES_DIRS, tuple)):
            for template_directory in settings.STATICFILES_DIRS:
                self.compile(path.normpath(template_directory + '/src'), template_directory)
        else:
            self.compile(path.normpath(settings.STATICFILES_DIRS + '/src'), settings.STATICFILES_DIRS)

        #settings.STATIC_ROOT shouldn't be left out.
        self.compile(path.normpath(settings.STATIC_ROOT + '/src'), settings.STATIC_ROOT)
            

    def compile(self, source_directory, output_directory):
        if not path.exists(source_directory):
            #print('No such file or directory: "%s"' % source_directory)
            return
        if not path.exists(output_directory):
            #print('No such file or directory: "%s"' % output_directory)
            return

        # subprocess suddenly stopped working...
        #from subprocess import Popen, call, PIPE
        #shell=True is necessary on windows due to jlc being provided by environment variables in node
        #call(['jlc', '--incremental', '--out', output_directory, source_directory], shell=True)#, stdout=PIPE, stderr=PIPE)
        os.system('jlc --quiet --incremental --out "%s" "%s"' % (output_directory, source_directory))
