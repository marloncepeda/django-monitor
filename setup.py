from setuptools import setup, find_packages

VERSION = '0.0.2'

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("Warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name='django-monitor',
    version=VERSION,
    description='Reusable Django app that provides event monitoring',
    long_description=read_md('README.md'),
    author='Andrew Cutler',
    author_email='andrew@voltgrid.com',
    url='https://github.com/voltgrid/django-monitor',
    package_dir={'monitor': 'monitor'},
    packages=find_packages(),
    package_data={
        # If any package contains *.txt etc include
        '': ['*.txt', ],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: System :: Monitoring'
    ],
    install_requires=[
        'Django',
        'djangorestframework',
        'requests'
    ],
)
