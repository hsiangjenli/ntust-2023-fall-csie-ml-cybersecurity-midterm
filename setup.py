from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='ntust-pyvs',
    entry_points={
        'console_scripts': [
            'pyvs = src.cli:cli',
        ]
    }
)