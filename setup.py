from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='drfauto',
    version='1.5.2',
    description='Package for auto creating serializers, filters and views for Django models',
    author='PasNA6713',
    author_email='diementros@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/PasNA6713/drf-auto',
    install_requires=[
        'django',
        'djangorestframework',
        'django-filter'
    ],
    entry_points={
    },
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)