"""
Project's setuptool configuration.

This should eggify and in theory upload to pypi without problems.

Oisin Mulvihill
2008-12-23

"""
import os
import os.path
from setuptools import setup, find_packages

Name = 'evasion-director'
ProjectUrl = "http://github.com/oisinmulvihill/evasion-director/tarball/master#egg=evasion_director"
Version = '1.1.6'
Author = 'Oisin Mulvihill'
AuthorEmail = 'oisinmulvihill at gmail dot com'
Maintainer = ' Oisin Mulvihill'
Summary = 'The evasion-director allows the creation of programs from configuration.'
License = 'Evasion Project CDDL License'
ShortDescription = Summary

# Add the README text if the file is present (not in egg).
detailed = Summary
if os.path.isfile("README.rst"):
    with file("README.rst", "r") as fd:
        detailed = fd.read()

Description = detailed

TestSuite = 'nose.collector'

needed = [
    # third party deps:
    'configobj',
    'mako',
]

SETUP_REQUIRES = [
    'nose>=1.0',
]

TEST_REQUIRES = [
    'nose>=1.0',
    'evasion-messenger',
]


#  find lib/director/viewpoint -type d -exec touch {}//__init__.py \;
#
# If new directories are added then I'll need to rerun this command.
#
EagerResources = [
    'evasion',
]

ProjectScripts = [
    'scripts/director',
    'scripts/morbidsvr',
]

PackageData = {
    # If any package contains *.txt or *.rst files, include them:
    '': ['*.*'],
}

# Make exe versions of the scripts:
EntryPoints = {
    'console_scripts': [
        'director = evasion.director.scripts.main:main',
        'viewpointdirect = evasion.director.viewpointdirect:main',
    ]
}


setup(
    url=ProjectUrl,
    zip_safe=False,
    name=Name,
    version=Version,
    author=Author,
    author_email=AuthorEmail,
    description=ShortDescription,
    long_description=Description,
    license=License,
    test_suite=TestSuite,
    scripts=ProjectScripts,
    install_requires=needed,
    setup_requires=SETUP_REQUIRES,
    tests_require=TEST_REQUIRES,
    packages=find_packages('lib'),
    package_data=PackageData,
    package_dir={'': 'lib'},
    eager_resources=EagerResources,
    entry_points=EntryPoints,
    namespace_packages=['evasion'],
)
