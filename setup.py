from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='drf-serializer-cache',
    version='0.3.3',
    description='Django REST framework (DRF) serializer speedup',
    license='BSD',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/K0Te/drf-serializer-cache',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='drf cache performance',
    install_requires=['django', 'djangorestframework'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'pytest-django'],
    test_suite='tests.functional',
    packages=find_packages(exclude=['tests']),  # Required
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/K0Te/drf-serializer-cache/issues',
        'Source': 'https://github.com/K0Te/drf-serializer-cache',
    },
)
