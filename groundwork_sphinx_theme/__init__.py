# Old way until 1.6
# But this works only

import os

__version__ = '1.0.5'


def get_path():
    return os.path.abspath(os.path.dirname(__file__))


def setup(app):
    return {
        'version': __version__,
        'parallel_read_safe': True
    }

# New way since sphinx 1.6
# Used for http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
# but not working.

# from os import path
# def setup(app):
#     app.add_html_theme('groundwork', path.abspath(path.join(path.dirname(__file__), "groundwork")))
