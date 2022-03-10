from setuptools import setup

setup(
    name='pkg1',
    version='0.1.0',
    author='An Awesome Coder',
    author_email='edwardbafford@go.rmc.edu',
    packages=['pkg1', 'pkg1.test'],
    scripts=['scripts/script.py'],
    license='LICENSE.txt',
    description='An awesome package that does nothing',
    long_description=open('README.md').read(),
    install_requires=[
        "pytest"
    ],
)
