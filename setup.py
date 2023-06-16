from setuptools import setup, find_packages

setup(name='read_matrix_counterclock_wise',
      version='0.1',
      url='https://github.com/desm80/avitoPythonTest.git',
      license='MIT',
      author='Denis Smirnov',
      author_email='jr-01@rambler.ru',
      description='Read matrix counterclock-wise from text file',
      packages=find_packages(exclude=['test']),
      long_description=open('README.md', encoding="utf-8").read(),
      zip_safe=False)
