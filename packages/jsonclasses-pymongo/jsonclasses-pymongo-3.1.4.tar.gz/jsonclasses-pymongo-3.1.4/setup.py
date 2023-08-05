import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name='jsonclasses-pymongo',
      version='3.1.4',
      description='jsonclasses integration with pymongo',
      long_description=README,
      long_description_content_type="text/markdown",
      author='Fillmula Inc.',
      author_email='victor.teo@fillmula.com',
      license='MIT',
      packages=find_packages(exclude=("tests")),
      package_data={'jsonclasses_pymongo': ['py.typed']},
      zip_safe=False,
      url='https://github.com/fillmula/jsonclasses-pymongo',
      include_package_data=True,
      python_requires='>=3.10',
      install_requires=[
            'pymongo>=3.12.0,<4.0.0',
            'inflection>=0.5.1,<1.0.0'
      ])
