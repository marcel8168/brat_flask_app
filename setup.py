from setuptools import find_packages, setup

setup(
    name='brat_flask_app',
    version='1.0',
    description='Test module for nlp project',
    author='Marcel Hiltner',
    author_email='marcel.hiltner@fau.de',
    packages=find_packages(),
    install_requires=[
        'flask==2.3.2',
    ]
)
