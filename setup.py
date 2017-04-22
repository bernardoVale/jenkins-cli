import os
import codecs
import re
from setuptools import setup
from setuptools import find_packages

def read(*parts):
    path = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(path, encoding='utf-8') as fobj:
        return fobj.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

tests_require = [
    'pytest',
]

with open('requirements.txt') as infile:
    install_requires = infile.read().splitlines()
    if not install_requires:
        print("Unable to read requirements from the requirements.txt file")
        sys.exit(2)


setup(
    name='jenkins',
    version=find_version("jenkins", "__init__.py"),
    description='Simple Jenkins CLI',
    author='Bernardo Vale',
    license='Apache License 2.0',
    packages=find_packages(exclude=['tests.*', 'tests']),
    include_package_data=True,
    test_suite='nose.collector',
    install_requires=install_requires,
    tests_require=tests_require,
    scripts=[
        'bin/jenkins'
    ],
    # entry_points="""
    # [console_scripts]
    # jenkins=jenkins.cli.main:main
    # """,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)