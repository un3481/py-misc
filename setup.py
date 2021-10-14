
# Import Distutils
from distutils.core import setup

setup(
    name='py_misc',
    version='1.8.2',
    license='MIT',
    description='Python Miscellaneous Library',
    author='anthony',
    url='https://github.com/anthony-freitas/py-misc',
    packages=[
        'py_misc',
        'py_misc/_call',
        'py_misc/_threading',
        'py_misc/_time'
    ]
)