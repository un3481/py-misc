
# Import Distutils
from distutils.core import setup

setup(
    name='py_misc',
    version='2.0.1',
    license='MIT',
    description='Python Miscellaneous Library',
    author='anthony',
    url='https://github.com/anthony-freitas/py-misc',
    packages=[
        'py_misc',
        'py_misc/modules',
        'py_misc/modules/call',
        'py_misc/modules/threading'
    ],
    install_requires=[
        'flask',
        'flask_httpauth',
        'schedule'
    ]
)