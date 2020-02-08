__author__ = 'Paul Severance'

from setuptools import setup

setup(
    name='charles-auth',
    version='0.0.1',
    author='Paul Severance',
    author_email='paul.severance@gmail.com',
    url='https://github.com/sugarush/charles-auth',
    packages=[
        'charles_auth'
    ],
    description='Dr Chuck\'s authentication method.',
    install_requires=[
        'python-dateutil'
    ]
)
