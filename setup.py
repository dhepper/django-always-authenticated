import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-always-authenticated',
    version='0.1.0',
    packages=['always_authenticated'],
    include_package_data=True,
    license='Simplified BSD License',
    description='A Django middleware that ensures every request has an' +
                'authenticated user.',
    long_description=README,
    url='https://github.com/dhepper/django-always-authenticated',
    author='Daniel Hepper',
    author_email='daniel@hepper.net',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    setup_requires=['pytest-runner', 'Django'],
    tests_require=['pytest', 'pytest-django'],
)
