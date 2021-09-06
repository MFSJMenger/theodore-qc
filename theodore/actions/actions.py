from colt.tools.actions import create_action
from .theotools import timeit_named
from .. import theo_header


run, Action, action = create_action('Action')




run.description = {
            'description': theo_header.ret_header(),
            'logo': None,
            'error_order': ['logo', 'description', 'args', 'usage', 'space', 'comment', 'space', 'error'],
            'arg_format': {
                'name': 20,
                'comment': 50,
                'seperator': ' | ',
            },
            'subparser_args': {
                'title': 'Actions: %s',
            },
            'subparser_format': {
                'name': 20,
                'comment': 50,
                },
}
