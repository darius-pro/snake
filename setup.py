from setuptools import setup, find_packages


setup(
    name='Snake',  # Required
    version='0.0.1',  # Required
    description='A simple python snake game',  # Optional
    url='https://github.com/darius-pro/snake',  # Optional
    author='Darius',  # Optional
    scripts=['snake'],
    classifiers=[
        'Programming Language :: Python :: 3.6', 
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent",
    ],
    keywords='snake',  # Optional
    packages=find_packages(exclude=['tests']),  # Required
    python_requires='==3.6*,==3.7*',
    install_requires=['pygame'],  # Optional
    extras_require={  # Optional
        'test': ['coverage'],
    }
)
