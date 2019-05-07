import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='rblwatch',
    packages=['rblwatch'],
    scripts=['bin/rblcheck', 'bin/rblwatch'],
    version='0.3.1',
    description='RBL lookups with Python',
    author='James Polera',
    author_email='james@uncryptic.com',
    maintainer='Thomas Merkel',
    maintainer_email='tm@core.io',
    license='BSD',
    classifiers=[
        'License :: OSI Approved :: BSD License',
    ],
    url='https://github.com/drscream/rblwatch',
    keywords=['rbl', 'blacklist', 'mail'],
    install_requires=['IPy', 'dnspython'],
)
