from setuptools import setup, find_packages

setup(
    name='modelstorage',
    version='0.0.1',
    description="Simple model storage solution ",
    author='Bradley Hartlove',
    author_email='bradleyhartlovecodes@gmail.com',
    packages=find_packages(include=['modelstorage', 'modelstorage.*']),
    install_requires=[
        'Flask'
    ],
    #extras_require={'plotting': ['matplotlib>=2.2.0', 'jupyter']},
    #setup_requires=['pytest-runner', 'flake8'],
    #tests_require=['pytest'],
    zip_safe=False,
    include_package_data=True,
    entry_points={
        'console_scripts': ['modelstorage=modelstorage.cli:main']
    },
    #package_data={'modelstorage': ['modelstorage/server/templates/*']}
    #package_data={'exampleproject': ['data/schema.json']}
)

