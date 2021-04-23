from setuptools import setup


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(name='scipy-tweaks',
      version=get_version("scipy_tweaks/__init__.py"),
      description='Utility functions for scipy.',
      long_description='README.rst',
      url='http://github.com/ulf1/scipy-tweaks',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='Apache License 2.0',
      packages=['scipy_tweaks'],
      install_requires=[
          'scipy>=1.5.4,<2'],
      python_requires='>=3.6',
      zip_safe=True)
