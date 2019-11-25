# Old way until 1.6
# But this works only

import os

__version__ = '1.1.1'


def setup(app):
    app.add_html_theme(
        'groundwork',
        os.path.abspath(os.path.dirname(__file__))
    )
    return {
        'version': __version__,
        'parallel_read_safe': True
    }
