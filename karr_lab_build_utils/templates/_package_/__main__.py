""" {{ name }} command line interface

:Author: Name <email>
:Date: {{ date }}
:Copyright: {{ year }}, Karr Lab
:License: MIT
"""

from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
import {{name}}
import {{name}}.core


class BaseController(CementBaseController):
    """ Base controller for command line application """

    class Meta:
        label = 'base'
        description = "{{ name }}"

    @expose(help='command_1 description')
    def command_1(self):
        """ command_1 description """
        print('command_1 output')

    @expose(help='command_2 description')
    def command_2(self):
        """ command_2 description """
        print('command_2 output')

    @expose(help='Get version')
    def get_version(self):
        """ Get version """
        print({{name}}.__version__)


class Command3WithArgumentsController(CementBaseController):
    """ Command3 description """

    class Meta:
        label = 'command-3'
        description = 'Command3 description'
        stacked_on = 'base'
        stacked_type = 'nested'
        arguments = [
            (['arg_1'], dict(
                type=str, help='Description of arg_1')),
            (['arg_2'], dict(
                type=str, help='Description of arg_2')),
            (['--opt-arg-3'], dict(
                type=str, default='default value of opt-arg-1', help='Description of opt-arg-3')),
            (['--opt-arg-4'], dict(
                type=float, default=float('nan'), help='Description of opt-arg-4')),
        ]

    @expose(hide=True)
    def default(self):
        args = self.app.pargs
        args.arg_1
        args.arg_2
        args.opt_arg_3
        args.opt_arg_4


class App(CementApp):
    """ Command line application """
    class Meta:
        label = '{{ name }}'
        base_controller = 'base'
        handlers = [
            BaseController,
            Command3WithArgumentsController,
        ]


def main():
    with App() as app:
        app.run()
