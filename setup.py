
# Import Distutils
from distutils.core import setup

setup(
    name='py_misc',
    version='2.2.0',
    license='MIT',
    description='Python Miscellaneous Library',
    author='anthony',
    url='https://github.com/un3481/py-misc',
    packages=[
        'py_misc',
        'py_misc/call',
        'py_misc/threading'
    ],
    install_requires=[
        'schedule'
    ]
)