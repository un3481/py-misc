
# Import Distutils
from distutils.core import setup

setup(
    name='py_misc',
    version='2.1.1',
    license='MIT',
    description='Python Miscellaneous Library',
    author='anthony',
    url='https://github.com/melon-yellow/py-misc',
    packages=[
        'py_misc',
        'py_misc/call',
        'py_misc/threading'
    ],
    install_requires=[
        'flask',
        'flask_httpauth',
        'schedule'
    ]
)