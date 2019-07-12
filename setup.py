"""
groundwork-sphinx-theme
=======================
"""
from setuptools import setup, find_packages
from io import open
import re
import os

with open('README.rst', 'rt', encoding='utf8') as doc_file:
    doc = doc_file.read()

with open(os.path.join('groundwork_sphinx_theme', '__init__.py'), 'rt', encoding='utf8') as f:
    version = re.search(r'^__version__ = \'(\d+\.(?:\d+\.)*\d+)\'', f.read(), re.M).group(1)

setup(
    name='groundwork-sphinx-theme',
    version=version,
    url='https://github.com/useblocks/groundwork-sphinx-theme',
    license='MIT',
    author='team useblocks',
    author_email='info@useblocks.com',
    description="Sphinx theme for groundwork projects (Based on flask_theme)",
    long_description=doc,
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    package_data={
            'groundwork_sphinx_theme': [
                'theme.conf',
            ],
            os.path.join('groundwork_sphinx_theme', 'static'): [
                'groundwork.css_t',
                'gw_logo.png',
                'small_groundwork.css'
            ],
            os.path.join('groundwork_sphinx_theme', 'templates'): [
                'contribute.html',
                'layout.html',
                'relations.html',
                'searchbox.html',
            ],
        },
    include_package_data=True,
    platforms='any',
    setup_requires=[],
    tests_require=[],
    install_requires=["Sphinx>=1.6.1"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'sphinx.html_themes': [
            'groundwork = groundwork_sphinx_theme',
        ],
    },
)
