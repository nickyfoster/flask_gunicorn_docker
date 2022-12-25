from setuptools import find_packages
import os

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

dir_path = os.path.dirname(os.path.realpath(__file__))


class PostDevelopCommand(develop):
    """Post-installation for development mode."""

    def run(self):
        develop.run(self)


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)


setup(
    name='TestApp',
    url='none',
    description='none',
    keywords='',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        "Flask==1.1.1",
        "gunicorn==19.9.0",
    ],
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
)
